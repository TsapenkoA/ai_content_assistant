import openai

def generate_text(prompt: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"OpenAI Error: {str(e)}"
    except Exception as e:
        return f"Other error: {str(e)}"

def process_image(image_data: bytes) -> str:
    return "[MOCK] Image processed"

def voice_to_text(audio_data: bytes) -> str:
    return "[MOCK] Transcribed text"
