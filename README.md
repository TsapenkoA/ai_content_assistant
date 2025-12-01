# AI Content Assistant (FastAPI · OpenAI · PostgreSQL/SQLite)

AI Content Assistant is a lightweight API service designed to handle text generation, basic image processing, and voice-to-text transcription.  
It demonstrates a clean backend architecture based on **FastAPI**, **SQLAlchemy**, **Pydantic**, and optional integration with **OpenAI API**.

The service provides a unified interface for working with different AI-related tasks while storing request history in a relational database.

---

## ⭐ Features

### 🔹 Text Processing
- Generate text responses using OpenAI (or fallback mock mode).
- Store each request and result in the database.
- Centralized error handling for API failures or quota issues.

### 🔹 Image Processing
- Upload and process images (mock mode or extendable real processing).
- Automatic temporary file storage.
- Database logging of every operation.

### 🔹 Voice Transcription
- Upload audio files and receive transcribed text (mock mode or extendable Whisper integration).
- Works with multipart/form-data uploads.
- All requests stored in DB.

### 🔹 Additional Features
- Interactive API documentation via Swagger (`/docs`).
- Modular and extendable project structure.
- Fully asynchronous FastAPI endpoints.

---

## 🛠️ Technologies Used

### **Backend**
- **FastAPI** — high-performance asynchronous Python framework.
- **Uvicorn** — ASGI server for running the application.

### **AI / Processing**
- **OpenAI API** (Chat Completions, Whisper, Vision) — optional integration.
- **Pillow** (optional) — for image manipulation.
- **FFmpeg + Whisper** (optional) — for audio transcription.

### **Database**
- **SQLAlchemy ORM** — database modeling and queries.
- **PostgreSQL** — primary recommended database.
- **SQLite** — local fallback for simple setups.

### **Data Models & Validation**
- **Pydantic v2** — input/output schemas.

---
