-- 01_notes-api-with-supabase 예제에서 사용하는 테이블입니다.
--
-- 이 예제의 목표:
-- 1. FastAPI 구조를 router/schema/service로 나눕니다.
-- 2. service 계층에서 Supabase 테이블을 CRUD합니다.
-- 3. 인증/RLS 없이 가장 단순한 DB 연결 흐름부터 확인합니다.

create table if not exists ex90_notes (
  -- id는 각 노트를 구분하는 고유값입니다.
  -- gen_random_uuid()는 Supabase/PostgreSQL이 자동으로 uuid를 만들어 줍니다.
  id uuid primary key default gen_random_uuid(),

  -- title/content는 사용자가 입력하는 필수 텍스트입니다.
  title text not null,
  content text not null,

  -- created_at은 row가 만들어진 시간을 자동 기록합니다.
  created_at timestamp not null default now()
);

-- 학습 및 API 테스트에 사용할 샘플 노트 10개입니다.
-- 고정 UUID와 on conflict를 사용하므로 이 파일을 다시 실행해도 중복되지 않습니다.
insert into ex90_notes (id, title, content)
values
  ('00000000-0000-4000-8000-000000000001', 'FastAPI 시작하기', 'FastAPI 프로젝트를 만들고 개발 서버를 실행하는 방법을 정리했습니다.'),
  ('00000000-0000-4000-8000-000000000002', '라우터의 역할', '라우터는 요청 URL과 HTTP 메서드를 서비스 로직에 연결합니다.'),
  ('00000000-0000-4000-8000-000000000003', 'Pydantic 스키마', '요청 데이터 검증과 응답 데이터 형식을 Pydantic 모델로 정의합니다.'),
  ('00000000-0000-4000-8000-000000000004', 'Supabase 연결', '프로젝트 URL과 서비스 키를 환경 변수로 관리하여 Supabase에 연결합니다.'),
  ('00000000-0000-4000-8000-000000000005', '노트 생성 API', 'POST 요청으로 제목과 내용을 전달해 새로운 노트를 생성합니다.'),
  ('00000000-0000-4000-8000-000000000006', '노트 목록 조회', 'GET 요청으로 저장된 노트 목록을 최신 순서로 조회합니다.'),
  ('00000000-0000-4000-8000-000000000007', '노트 상세 조회', 'UUID를 경로 매개변수로 전달해 특정 노트 한 건을 조회합니다.'),
  ('00000000-0000-4000-8000-000000000008', '노트 수정 API', 'PUT 요청으로 기존 노트의 제목과 내용을 수정합니다.'),
  ('00000000-0000-4000-8000-000000000009', '노트 삭제 API', 'DELETE 요청으로 더 이상 필요하지 않은 노트를 삭제합니다.'),
  ('00000000-0000-4000-8000-000000000010', 'API 테스트', 'Swagger UI와 pytest를 사용해 Notes API의 동작을 확인합니다.')
on conflict (id) do nothing;
