# AI Content Assistant

## Purpose of the Project
The **AI Content Assistant** is a demonstration service designed to showcase a practical integration of AI, backend, and web development.  
Its purpose is to provide a fully functional API where users can:

- Generate text based on a prompt.
- Process images for basic analysis.
- Convert audio files into text via transcription.

All user requests and AI-generated results are stored in a database for further reference.

---

## Project Description
This project demonstrates a complete workflow for an AI-powered content assistant:

1. **Text generation** – Users provide a prompt, and the service returns AI-generated text.  
2. **Image processing** – Users upload an image, and the service returns a processed result (currently a mock).  
3. **Voice transcription** – Users upload an audio file, and the service returns transcribed text (currently a mock).  
4. **Database logging** – All requests and responses are saved in PostgreSQL or SQLite using SQLAlchemy ORM.

The project is structured to clearly separate concerns: API routes, database models, AI services, and validation schemas.

---

## Technologies Used
- **Python** – core programming language for backend logic and AI integration.
- **FastAPI** – handles REST API endpoints, routing, and request validation.
- **SQLAlchemy** – ORM for database models and interaction.
- **PostgreSQL / SQLite** – relational database for storing user requests and AI results.
- **Artificial Intelligence (AI)** – integration with OpenAI GPT models for text generation.
- **Machine Learning (ML)** – project structure allows adding ML-based image and audio processing.
- **Web Development** – REST API design with Swagger UI for interactive testing.

---
