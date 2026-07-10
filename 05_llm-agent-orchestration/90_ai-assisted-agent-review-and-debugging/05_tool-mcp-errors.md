# 05 Tool and MCP Errors

## Tool 오류 확인

Tool은 LLM이 직접 실행하는 것이 아니라 Python 코드가 실행합니다.

확인할 것:

- Tool 이름이 명확한가?
- 입력값 schema가 실제 함수 인자와 맞는가?
- Tool 결과가 문자열 또는 JSON으로 정리되는가?
- 외부 API 실패 시 Fallback이 있는가?

## MCP 오류 확인

05 과정의 MCP는 선택 심화입니다.

확인할 것:

- MCP 서버가 실행 중인가?
- 클라이언트가 같은 실행 방식으로 연결하는가?
- Tool 이름과 입력 schema가 일치하는가?
- MCP가 꼭 필요한 실습인지, 일반 Tool 함수로도 충분한지 구분했는가?

## AI에게 질문할 때

```text
Tool 정의
Tool 입력값
Tool 실행 결과
LLM이 선택한 Tool 이름
MCP 서버 실행 명령
전체 오류 메시지
```
