-- conversation_id별 멀티턴 대화 기록을 저장합니다.
create table if not exists ex90_multi_turn_chat_logs (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid not null,
  user_message text not null,
  assistant_message text not null,
  model text not null,
  created_at timestamptz not null default now()
);

create index if not exists ex90_multi_turn_chat_logs_conversation_created_idx
on ex90_multi_turn_chat_logs (conversation_id, created_at);
