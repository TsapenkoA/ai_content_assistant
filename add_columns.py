from sqlalchemy import create_engine, text

# Параметри підключення до твоєї бази
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/ai_content_db"

# Підключаємося
engine = create_engine(DATABASE_URL)

# SQL для додавання колонок
alter_sql = """
ALTER TABLE user_requests
ADD COLUMN IF NOT EXISTS prompt TEXT,
ADD COLUMN IF NOT EXISTS request_type TEXT,
ADD COLUMN IF NOT EXISTS input_data TEXT,
ADD COLUMN IF NOT EXISTS result TEXT;
"""

# Виконання
with engine.connect() as conn:
    conn.execute(text(alter_sql))
    conn.commit()

print("Колонки успішно додані!")
