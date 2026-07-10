r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\06_feedback-loop-result-review

Run command:
    python .\01_feedback_loop_result_review.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 결과 검증과 Feedback Loop를 구현하는 예제입니다."""

from dataclasses import dataclass, field


@dataclass
class ReviewResult:
    """Agent 응답 검증 결과입니다."""

    passed: bool
    score: int
    feedback: str


@dataclass
class FeedbackState:
    """Feedback Loop 실행 상태입니다."""

    request: str
    attempts: int = 0
    responses: list[str] = field(default_factory=list)
    reviews: list[ReviewResult] = field(default_factory=list)


def answer_agent(request: str, feedback: str = "") -> str:
    """요청과 피드백을 바탕으로 응답을 생성하는 Mock Agent입니다."""

    if not feedback:
        return f"문제를 확인했습니다. 요청: {request}"
    return f"요청 원인, 복구 절차, 검증 방법을 포함해 답변합니다. 피드백 반영: {feedback}"


def reviewer_agent(response: str) -> ReviewResult:
    """응답에 필수 운영 요소가 있는지 검증합니다."""

    required_keywords = ["원인", "복구", "검증"]
    matched = [keyword for keyword in required_keywords if keyword in response]
    score = int(len(matched) / len(required_keywords) * 100)
    passed = score >= 80

    if passed:
        feedback = "품질 기준 통과"
    else:
        missing = sorted(set(required_keywords) - set(matched))
        feedback = f"누락된 항목을 보강하세요: {', '.join(missing)}"

    return ReviewResult(passed=passed, score=score, feedback=feedback)


def run_feedback_loop(request: str, max_attempts: int = 3) -> FeedbackState:
    """응답 생성, 검증, 재시도 과정을 실행합니다."""

    state = FeedbackState(request=request)
    feedback = ""

    while state.attempts < max_attempts:
        state.attempts += 1
        response = answer_agent(request, feedback)
        review = reviewer_agent(response)
        state.responses.append(response)
        state.reviews.append(review)

        if review.passed:
            break

        feedback = review.feedback

    return state


def main() -> None:
    """Feedback Loop 실행 결과를 출력합니다."""

    state = run_feedback_loop("backend 장애가 발생했을 때 운영자에게 안내할 답변을 작성해줘.")
    print(f"request={state.request}")
    for index, (response, review) in enumerate(zip(state.responses, state.reviews), start=1):
        print(f"\n=== Attempt {index} ===")
        print(f"response={response}")
        print(f"review={review}")


if __name__ == "__main__":
    main()
