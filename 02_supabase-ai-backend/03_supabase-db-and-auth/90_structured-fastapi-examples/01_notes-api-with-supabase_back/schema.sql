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
  created_at timestamptz not null default now()
);
