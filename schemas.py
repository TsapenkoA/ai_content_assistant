from pydantic import BaseModel

class TextRequest(BaseModel):
    prompt: str

class TextResponse(BaseModel):
    id: int
    prompt: str
    result: str

    class Config:
        from_attributes = True

class ImageRequest(BaseModel):
    filename: str 

class ImageResponse(BaseModel):
    id: int
    result: str

    class Config:
        from_attributes = True

class VoiceRequest(BaseModel):
    filename: str 

class VoiceResponse(BaseModel):
    id: int
    result: str

    class Config:
        from_attributes = True
