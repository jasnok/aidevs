# 04 LangGraph State Errors

LangGraph 오류는 대부분 State 구조, Node 반환값, Edge 연결에서 시작됩니다.

## 확인할 것

- State에 필요한 필드가 모두 있는가?
- Node 함수가 dict를 반환하는가?
- Node 이름과 Edge 이름이 정확히 일치하는가?
- Conditional Edge 함수가 실제 등록된 Node 이름을 반환하는가?
- START와 END 연결이 있는가?
- Retry 조건이 무한 반복을 만들지 않는가?

## AI에게 질문할 때

아래 내용을 함께 전달합니다.

```text
State 타입 정의
Node 함수 코드
Edge 연결 코드
실행한 initial_state
전체 오류 메시지
```

## 디버깅 팁

각 Node 시작과 끝에 현재 State를 출력하면 흐름을 이해하기 쉽습니다.

```python
print("[node name] input:", state)
```
