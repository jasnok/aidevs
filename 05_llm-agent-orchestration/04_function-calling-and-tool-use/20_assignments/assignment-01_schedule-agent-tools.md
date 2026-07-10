# Assignment 01. Schedule Agent Tools

## 과제 목표

일정 조정 Agent가 사용할 Tool을 설계합니다.

## 작성 항목

1. Agent가 해결할 문제
2. 필요한 Tool 목록
3. 각 Tool의 입력값
4. 각 Tool의 출력값
5. 실패할 수 있는 상황
6. Retry 또는 Fallback 전략

## 작성 형식 예시

```text
1. Agent가 해결할 문제
- 회의 가능한 시간을 찾고 후보 일정을 추천한다.

2. Tool 목록
| Tool 이름 | 역할 | 입력값 | 출력값 |
| --- | --- | --- | --- |
| get_user_calendar | 사용자 일정 조회 | user_id, date_range | 일정 목록 |
| find_available_slots | 가능한 시간 계산 | calendars, duration | 후보 시간 목록 |
| create_schedule_summary | 일정 요약 생성 | selected_slot, participants | 요약 문장 |

3. 실패 상황
| 상황 | 대응 |
| --- | --- |
| 일정 데이터 없음 | 추가 정보 요청 |
| 후보 시간이 없음 | 대체 날짜 제안 |
| 외부 API 실패 | 재시도 또는 수동 확인 안내 |

4. Fallback 전략
- 1차 재시도
- 대체 Tool 사용
- 사용자에게 추가 질문
```

## 평가 기준

- Tool 책임이 명확한가
- 입력/출력 구조가 구체적인가
- 실패 상황을 고려했는가
- 일정 조정 Agent의 실제 실행 흐름과 연결되는가
