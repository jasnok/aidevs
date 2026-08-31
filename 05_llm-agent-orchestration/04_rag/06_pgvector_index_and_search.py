"""문서를 Ollama로 Embedding하여 pgvector에 저장하고 검색합니다."""

from _pgvector_store import delete_collection, similarity_search, upsert_text


COLLECTION = "rag_test"
DOCUMENTS = [
    # ("호텔 환불", "체크인 3일 전까지 취소하면 전액 환불합니다.", "hotel-refund.md"),
    # ("호텔 환불", "당일 취소는 환불되지 않습니다.", "hotel-refund.md"),
    # ("수하물", "교육용 국내선의 위탁 수하물은 15kg까지 허용합니다.", "baggage.md"),
    # ("관광지", "바다 박물관은 매주 화요일에 휴관합니다.", "attraction-hours.md"),
    ("legal", "임차인은 최대한의 권한을 보호받는다.", "legal.md"),
    ("legal", "임차인은 임대인의 동의 없이 임대차계약을 해지할 수 있다.", "legal.md"),
]


def index_documents() -> None:
    delete_collection(COLLECTION)
    for index, (title, content, source) in enumerate(DOCUMENTS):
        upsert_text(
            collection=COLLECTION,
            title=title,
            content=content,
            source=source,
            chunk_index=index,
            metadata={"lesson": "04_rag"},
        )
        print(f"저장: {source} | {content}")


if __name__ == "__main__":
    index_documents()

    # question = "숙소를 당일 취소하면 돈을 돌려받을 수 있나요?"
    question = "나 임차인 계약 연장 문의"
    print("\n질문:", question)
    for item in similarity_search(question, collection=COLLECTION, top_k=3):
        print(f"{item['score']:.3f} | {item['source']} | {item['content']}")
