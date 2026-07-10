# 03 Ops Dashboard Streamlit

이 실습은 Streamlit으로 간단한 운영 대시보드를 만듭니다.

## 표시할 정보

- 서비스 상태
- 최근 이벤트 로그
- 성공/실패 수
- 장애 유형별 건수
- 복구 성공 여부
- 최근 실행 요청 목록

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
streamlit run .\03_ops-dashboard-streamlit\01_ops-dashboard.py --server.port 8803
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8803
```

## 확인할 것

- failed 이벤트를 추가하면 지표가 바뀌는가?
- 최근 이벤트가 표로 보이는가?
- 운영자가 다음 행동을 판단할 수 있는 정보가 있는가?
