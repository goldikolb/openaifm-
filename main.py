import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

# Lade Umgebungsvariablen aus .env
load_dotenv()

openai = AsyncOpenAI()

input = """Hier gebe den Text ein, den du als Audio erzeugen willst"""

instructions = """Beschreibe hier den Klang der Stimme"""

async def main() -> None:
    # Erstelle einen Zeitstempel für den Dateinamen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"output/audio_{timestamp}.mp3"

    # Stelle sicher, dass der output-Ordner existiert
    os.makedirs("output", exist_ok=True)

    # Erstelle die Audio-Datei mit Streaming
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="sage", #alloy ash ballad coral echo fable onyx nova sage shimmer
        input=input,
        instructions=instructions,
        response_format="mp3",
    ) as response:
        # Speichere die Audio-Datei
        await response.stream_to_file(output_file)
        print(f"Audio wurde gespeichert in: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())