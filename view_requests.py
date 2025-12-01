# view_requests.py

from database import SessionLocal
from models import UserRequest

def main():
    db = SessionLocal()
    try:
        # Вибираємо тільки текстові запити
        requests = db.query(UserRequest).filter(UserRequest.request_type == "text").all()
        if not requests:
            print("No text requests found.")
            return

        for r in requests:
            print("-" * 50)
            print(f"ID: {r.id}")
            print(f"Prompt: {r.prompt}")
            print(f"Result: {r.result}")
            print(f"Created at: {r.created_at}")
        print("-" * 50)

    finally:
        db.close()

if __name__ == "__main__":
    main()
