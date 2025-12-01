from pydantic import BaseModel

# --- Text ---
class TextRequest(BaseModel):
    prompt: str

class TextResponse(BaseModel):
    id: int
    prompt: str
    result: str

    class Config:
        from_attributes = True

# --- Image ---
class ImageRequest(BaseModel):
    filename: str 

class ImageResponse(BaseModel):
    id: int
    result: str

    class Config:
        from_attributes = True

# --- Voice ---
class VoiceRequest(BaseModel):
    filename: str  # або file: UploadFile

class VoiceResponse(BaseModel):
    id: int
    result: str

    class Config:
        from_attributes = True

