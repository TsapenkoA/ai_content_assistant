from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import UserRequest
from database import Base, engine
from schemas import TextRequest, TextResponse, ImageResponse, VoiceResponse
from ai_services import generate_text, process_image, voice_to_text

# --- Створюємо таблиці, якщо їх ще немає
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Content Assistant")

@app.get("/")
def read_root():
    return {"message": "AI Content Assistant is running!"}

# ---------------------------
# TEXT
# ---------------------------
@app.post("/generate_text", response_model=TextResponse)
def create_text(request_data: TextRequest, db: Session = Depends(get_db)):
    result_text = generate_text(request_data.prompt)

    db_request = UserRequest(
        request_type="text",
        prompt=request_data.prompt,
        input_data="",
        result=result_text or ""
    )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return TextResponse(
        id=db_request.id,
        prompt=db_request.prompt,
        result=db_request.result
    )

# ---------------------------
# IMAGE
# ---------------------------
@app.post("/process_image", response_model=ImageResponse)
def create_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        data = file.file.read()
        result = process_image(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    db_request = UserRequest(
        request_type="image",
        prompt=None,
        input_data=file.filename,
        result=result
    )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return ImageResponse(id=db_request.id, result=db_request.result)

# ---------------------------
# VOICE
# ---------------------------
@app.post("/voice_to_text", response_model=VoiceResponse)
def create_voice(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        data = file.file.read()
        result = voice_to_text(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    db_request = UserRequest(
        request_type="voice",
        prompt=None,
        input_data=file.filename,
        result=result
    )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return VoiceResponse(id=db_request.id, result=db_request.result)
