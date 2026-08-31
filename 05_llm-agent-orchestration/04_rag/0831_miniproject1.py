"""LawMate: Ollama 분류 + pgvector 기반 가상 법률 사례 검색 예제.

이 파일의 데이터와 검색 결과는 AI 오케스트레이션 학습용이며,
실제 판례 또는 법률 자문이 아닙니다.
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any

import httpx

from _pgvector_store import (
    EMBEDDING_MODEL,
    OLLAMA_BASE_URL,
    delete_collection,
    similarity_search,
    upsert_text,
)


COLLECTION = "lawmate_mock_cases"
CHAT_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
LOW_RELEVANCE_THRESHOLD = float(os.getenv("LAWMATE_LOW_RELEVANCE_THRESHOLD", "0.45"))
DISCLAIMER = (
    "본 결과는 AI 오케스트레이션 학습을 위한 가상 법률 사례를 기반으로 한 "
    "검색 결과이며 실제 판례나 법률 자문이 아닙니다."
)
CASE_TYPES = ("임대차", "거래", "계약", "손해배상", "형사", "기타")

MOCK_CASES: list[dict[str, Any]] = [
    {
        "id": "CASE-001", "case_type": "임대차", "title": "전세 계약 종료 후 보증금 반환",
        "situation": "임차인이 전세 계약기간 종료 후 주택을 반환했으나 임대인이 새 임차인을 구하지 못했다는 이유로 보증금 반환을 지연하는 상황.",
        "facts": "임대차계약 기간이 종료되었고 임차인은 목적물을 반환했다. 임대인은 후속 임차인을 구하지 못했다는 이유로 보증금 반환을 미루고 있다.",
        "issue": "임대인이 새로운 임차인을 구하지 못했다는 이유만으로 계약 종료 후 보증금 반환을 계속 지연할 수 있는지 여부.",
        "conclusion": "계약 종료와 목적물 반환 등 구체적인 사실관계에 따라 보증금 반환 문제가 발생할 수 있다. 새 임차인을 구하지 못했다는 사정만으로 단순 판단할 수는 없다.",
        "keywords": ["전세보증금", "보증금반환", "임대차계약", "계약종료"],
    },
    {
        "id": "CASE-002", "case_type": "임대차", "title": "월세 연체에 따른 임대차계약 해지",
        "situation": "임차인이 여러 차례 월세를 연체하였고 임대인이 계약 해지를 요구하는 상황.",
        "facts": "임차인의 차임 지급이 반복적으로 지연되었으며 임대인이 계약 해지를 통보했다.",
        "issue": "월세 연체가 발생한 경우 임대차계약을 해지할 수 있는지 여부.",
        "conclusion": "차임 연체의 정도와 계약 내용 등 구체적인 사실관계를 확인해야 하며, 한 번의 연체만으로 모든 경우를 동일하게 판단해서는 안 된다.",
        "keywords": ["월세연체", "차임", "임대차계약", "계약해지"],
    },
    {
        "id": "CASE-003", "case_type": "임대차", "title": "임대차 종료 후 수리비 공제",
        "situation": "임차인이 퇴거한 뒤 임대인이 벽지와 시설 수리비를 보증금에서 공제하겠다고 주장하는 상황.",
        "facts": "임대인은 수리비를 요구하고 있고 임차인은 일반적인 사용으로 인한 손상이라고 주장한다.",
        "issue": "임대차 종료 후 어떤 수리비를 임차인에게 부담시킬 수 있는지 여부.",
        "conclusion": "손상의 원인과 정도, 통상적인 사용에 따른 마모인지 여부 등 구체적인 사실관계를 확인해야 한다.",
        "keywords": ["원상회복", "수리비", "보증금공제", "임대차"],
    },
    {
        "id": "CASE-004", "case_type": "임대차", "title": "계약 갱신 후 임대인의 퇴거 요구",
        "situation": "임차인이 계약 갱신을 요구했으나 임대인이 퇴거를 요구하는 상황.",
        "facts": "임대차계약 갱신과 관련하여 당사자 간 주장이 서로 다르다.",
        "issue": "계약 갱신 여부와 임대인의 퇴거 요구가 적법한지 판단해야 한다.",
        "conclusion": "계약 내용과 갱신 의사표시, 관련 법령 및 구체적인 사실관계를 종합적으로 확인해야 한다.",
        "keywords": ["계약갱신", "갱신요구", "임대인", "임차인", "퇴거"],
    },
    {
        "id": "CASE-005", "case_type": "거래", "title": "중고거래 대금 지급 후 물품 미배송",
        "situation": "구매자가 중고거래 대금을 송금했지만 판매자가 물품을 보내지 않고 연락을 끊은 상황.",
        "facts": "구매자는 대금을 지급했고 판매자는 물품을 보내겠다고 약속했으나 이후 연락이 되지 않는다.",
        "issue": "단순한 거래상 분쟁인지 형사상 문제가 될 가능성이 있는지 여부.",
        "conclusion": "거래 당시의 의사와 실제 행동, 대화 내용, 송금 내역 등 구체적인 자료를 확인해야 한다.",
        "keywords": ["중고거래", "물품미배송", "거래사기", "송금"],
    },
    {
        "id": "CASE-006", "case_type": "계약", "title": "계약금 지급 후 계약 취소",
        "situation": "계약금을 지급한 이후 상대방이 계약을 취소하겠다고 주장하는 상황.",
        "facts": "계약금이 지급되었으며 이후 계약 당사자 중 한쪽이 계약을 취소하려고 한다.",
        "issue": "계약금 지급 이후 계약을 해제할 수 있는지 여부.",
        "conclusion": "계약의 내용과 계약금의 성격, 당사자의 의사표시 등 구체적인 내용을 확인해야 한다.",
        "keywords": ["계약금", "계약해제", "계약취소", "매매계약"],
    },
    {
        "id": "CASE-007", "case_type": "손해배상", "title": "주차장에서 발생한 차량 파손",
        "situation": "주차된 차량을 다른 차량이 충돌하여 파손한 상황.",
        "facts": "주차장에서 차량 간 접촉이 발생했고 차량 소유자 사이에 손해배상 책임 다툼이 발생했다.",
        "issue": "사고의 과실 정도와 손해배상 범위를 어떻게 판단할 것인지 여부.",
        "conclusion": "사고 당시 상황과 각 차량의 행동, 손해 정도 및 과실 비율 등을 종합적으로 확인해야 한다.",
        "keywords": ["차량파손", "주차장", "교통사고", "손해배상", "과실"],
    },
    {
        "id": "CASE-008", "case_type": "형사", "title": "술자리에서 발생한 폭행",
        "situation": "술자리에서 두 사람이 말다툼을 하다가 서로 신체적 충돌이 발생한 상황.",
        "facts": "양측이 서로 폭행을 주장하고 있으며 한쪽은 상해를 입었다고 주장한다.",
        "issue": "폭행 또는 상해와 관련된 법적 책임을 어떻게 판단할 것인지 여부.",
        "conclusion": "실제 폭행 행위, 피해 정도, 당시 상황, 증거 및 당사자들의 행동 등을 구체적으로 확인해야 한다.",
        "keywords": ["폭행", "상해", "음주", "쌍방폭행", "합의"],
    },
    {
        "id": "CASE-009", "case_type": "형사", "title": "온라인 게시글에 의한 명예훼손",
        "situation": "인터넷 커뮤니티에 특정인을 대상으로 한 게시글이 작성되어 당사자가 피해를 주장하는 상황.",
        "facts": "온라인에 특정인을 지칭하거나 특정인을 알아볼 수 있는 내용의 게시글이 작성되었다.",
        "issue": "게시글의 내용과 작성 방식에 따라 명예훼손 문제가 발생할 수 있는지 여부.",
        "conclusion": "구체적인 표현, 사실의 적시 여부, 공개 범위, 작성 목적 등 다양한 요소를 확인해야 한다.",
        "keywords": ["명예훼손", "인터넷", "게시글", "온라인"],
    },
    {
        "id": "CASE-010", "case_type": "임대차", "title": "전세 계약 전 중요 사실을 알리지 않은 경우",
        "situation": "임차인이 계약 체결 이후 계약 전에 알지 못했던 중요한 사실을 발견한 상황.",
        "facts": "계약 체결 당시 당사자 사이에 중요한 사실에 대한 설명 여부를 두고 분쟁이 발생했다.",
        "issue": "계약 체결 과정에서 중요한 사실을 알리지 않은 경우 어떤 법적 문제가 발생할 수 있는지 여부.",
        "conclusion": "계약 당시 당사자가 알고 있었던 사실과 고지 여부, 계약 내용 및 관련 법령 등을 종합적으로 확인해야 한다.",
        "keywords": ["전세계약", "고지의무", "계약취소", "임대차"],
    },
]

TEST_QUESTIONS = [
    ("전세 계약이 끝났는데 집주인이 보증금을 안 돌려줘요.", "CASE-001"),
    ("월세를 몇 달 밀렸는데 집주인이 계약을 끝낼 수 있나요?", "CASE-002"),
    ("퇴거했는데 집주인이 보증금에서 벽지 수리비를 빼겠다고 해요.", "CASE-003"),
    ("중고거래로 돈을 보냈는데 판매자가 물건을 안 보내요.", "CASE-005"),
    ("술집에서 서로 싸웠는데 폭행으로 처벌받을 수 있나요?", "CASE-008"),
    ("인터넷에 제 이야기를 올렸는데 명예훼손인가요?", "CASE-009"),
]


def build_content(case: dict[str, Any]) -> str:
    """키워드뿐 아니라 사례 전체 문맥을 임베딩할 검색 본문으로 결합합니다."""
    return "\n".join(
        [
            f"사건 유형: {case['case_type']}", f"제목: {case['title']}",
            f"상황: {case['situation']}", f"사실관계: {case['facts']}",
            f"쟁점: {case['issue']}", f"결론: {case['conclusion']}",
            f"키워드: {', '.join(case['keywords'])}",
        ]
    )


def seed_mock_cases(*, reset: bool = True) -> None:
    """10개 가상 사례를 실제 Ollama 임베딩과 함께 멱등적으로 저장합니다."""
    if reset:
        delete_collection(COLLECTION)
    for index, case in enumerate(MOCK_CASES):
        metadata = {**case, "is_mock": True}
        upsert_text(
            collection=COLLECTION,
            title=case["title"],
            content=build_content(case),
            source=case["id"],
            chunk_index=index,
            metadata=metadata,
        )
        print(f"저장 완료: {case['id']} | {case['case_type']} | {case['title']}")


def classify_question(query: str) -> dict[str, str]:
    """Ollama가 질문을 검색용 사건 유형 하나로 분류합니다."""
    response = httpx.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json={
            "model": CHAT_MODEL,
            "stream": False,
            "format": "json",
            "options": {"temperature": 0},
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "당신은 검색 라우터입니다. 법률 판단이나 자문을 하지 마세요. "
                        f"질문을 다음 중 하나로만 분류하세요: {', '.join(CASE_TYPES)}. "
                        "반드시 {\"case_type\":\"...\",\"reason\":\"짧은 이유\"} JSON만 출력하세요. "
                        "전세·월세·보증금·퇴거는 임대차, 중고매매·물품 미배송은 거래, "
                        "폭행·명예훼손은 형사입니다. 질문에 해당 단서가 있으면 기타를 선택하지 마세요."
                    ),
                },
                {"role": "user", "content": "중고거래 판매자가 물건을 보내지 않아요."},
                {"role": "assistant", "content": '{"case_type":"거래","reason":"중고 물품 거래 분쟁"}'},
                {"role": "user", "content": "인터넷 글 때문에 명예훼손 문제가 생겼어요."},
                {"role": "assistant", "content": '{"case_type":"형사","reason":"온라인 명예훼손 문제"}'},
                {"role": "user", "content": query},
            ],
        },
        timeout=120,
    )
    response.raise_for_status()
    try:
        parsed = json.loads(response.json()["message"]["content"])
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError("Ollama 분류 응답을 JSON으로 해석할 수 없습니다.") from exc
    case_type = str(parsed.get("case_type", "기타")).strip()
    if case_type not in CASE_TYPES:
        case_type = "기타"
    return {"case_type": case_type, "reason": str(parsed.get("reason", ""))}


def search_similar_cases(query: str, top_k: int = 3) -> dict[str, Any]:
    """Agent/MCP Tool로 옮기기 쉬운 JSON 직렬화 가능 검색 인터페이스입니다."""
    if not query.strip():
        raise ValueError("query는 비어 있을 수 없습니다.")
    classification_error = None
    try:
        classification = classify_question(query)
    except (httpx.HTTPError, ValueError) as exc:
        classification = {"case_type": "기타", "reason": "분류 실패로 전체 검색"}
        classification_error = str(exc)

    metadata_filter = None
    if classification["case_type"] != "기타":
        metadata_filter = {"case_type": classification["case_type"], "is_mock": True}

    raw_results = similarity_search(
        query, collection=COLLECTION, top_k=top_k, metadata_filter=metadata_filter
    )
    # 분류 필터에 결과가 없으면 잘못된 라우팅으로 간주하고 전체 사례를 검색합니다.
    if not raw_results and metadata_filter:
        raw_results = similarity_search(
            query, collection=COLLECTION, top_k=top_k, metadata_filter={"is_mock": True}
        )
        classification["reason"] += " (해당 유형 데이터가 없어 전체 검색으로 전환)"

    results = []
    for item in raw_results:
        meta = item["metadata"]
        results.append(
            {
                "id": meta["id"], "title": item["title"],
                "case_type": meta["case_type"], "situation": meta["situation"],
                "conclusion": meta["conclusion"], "content": item["content"],
                "similarity": round(item["score"], 4), "is_mock": bool(meta["is_mock"]),
            }
        )
    low_relevance = not results or results[0]["similarity"] < LOW_RELEVANCE_THRESHOLD
    return {
        "query": query,
        "classification": classification,
        "classification_error": classification_error,
        "results": results,
        "low_relevance": low_relevance,
        "status": "관련성이 낮은 사례만 검색되었습니다" if low_relevance else "검색 완료",
        "disclaimer": DISCLAIMER,
    }


def run_tests(top_k: int = 3) -> bool:
    """프롬프트의 6개 질문에서 예상 사례가 Top-K에 드는지 확인합니다."""
    all_passed = True
    for query, expected in TEST_QUESTIONS:
        payload = search_similar_cases(query, top_k=top_k)
        ids = [item["id"] for item in payload["results"]]
        passed = expected in ids
        all_passed &= passed
        print(f"\n[{'PASS' if passed else 'FAIL'}] {query}")
        print(f"분류: {payload['classification']['case_type']} | 예상: {expected} | 검색: {ids}")
        for item in payload["results"]:
            print(f"  {item['similarity']:.4f} | {item['id']} | {item['title']}")
        print(f"상태: {payload['status']}")
    print(f"\n테스트 결과: {'전체 통과' if all_passed else '실패 있음'}")
    print(DISCLAIMER)
    return all_passed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LawMate 가상 법률 사례 Vector Search")
    parser.add_argument("--seed", action="store_true", help="가상 사례 10개를 재색인")
    parser.add_argument("--test", action="store_true", help="예상 질문 6개 자동 테스트")
    parser.add_argument("--query", help="검색할 질문")
    parser.add_argument("--top-k", type=int, default=3, help="검색 결과 수(기본 3)")
    args = parser.parse_args()
    if not (args.seed or args.test or args.query):
        args.seed = args.test = True
    return args


def main() -> int:
    args = parse_args()
    print(f"Ollama chat={CHAT_MODEL}, embedding={EMBEDDING_MODEL}, collection={COLLECTION}")
    if args.seed:
        seed_mock_cases()
    passed = True
    if args.test:
        passed = run_tests(args.top_k)
    if args.query:
        print(json.dumps(search_similar_cases(args.query, args.top_k), ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
