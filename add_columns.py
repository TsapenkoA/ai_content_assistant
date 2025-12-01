from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/ai_content_db"

engine = create_engine(DATABASE_URL)

alter_sql = """
ALTER TABLE user_requests
ADD COLUMN IF NOT EXISTS prompt TEXT,
ADD COLUMN IF NOT EXISTS request_type TEXT,
ADD COLUMN IF NOT EXISTS input_data TEXT,
ADD COLUMN IF NOT EXISTS result TEXT;
"""

with engine.connect() as conn:
    conn.execute(text(alter_sql))
    conn.commit()

print("Колонки успішно додані!")

