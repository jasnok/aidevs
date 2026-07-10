# 02 GitHub Actions Debugging

## 확인할 위치

GitHub repository에서:

```text
Actions -> 실패한 workflow -> 실패한 job -> 실패한 step
```

## 자주 보는 실패

| 실패 step | 확인할 것 |
| --- | --- |
| Checkout | repository 권한, branch 이름 |
| Set up Python | Python version |
| Python syntax check | 문법 오류 파일 경로 |
| Docker Compose config | workflow에서 이동한 폴더 경로 |
| Docker build | Dockerfile 위치, requirements, COPY 경로 |

## Codex 질문 예시

```text
GitHub Actions의 Docker build step이 실패했습니다.
workflow 파일:
...
실패 로그:
...
repository 구조:
...
어떤 경로 또는 Dockerfile 설정을 고쳐야 하는지 알려줘.
```

## Secret 주의

AWS Access Key, OpenAI API Key가 로그에 출력되면 안 됩니다.
