import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

# Lade Umgebungsvariablen aus .env
load_dotenv()

openai = AsyncOpenAI()

input = """Sein oder Nichtsein, das ist die Frage."""

instructions = """Effect:\nEin weiser Denker – ruhig, nachdenklich, mit einem Blick fürs Große Ganze. Wie jemand, der lieber zuhört als redet, aber wenn er spricht, dann mit Bedeutung.\n\nTone:\nSanft, klar und introspektiv – nicht belehrend, sondern einladend zum Mitdenken. Jemand, der nicht überzeugen muss, weil die Tiefe der Worte für sich spricht.\n\nDelivery:\nLangsam, mit Bedacht. Kurze Pausen zwischen den Gedanken – als würde der Sprecher selbst erst beim Sprechen verstehen, was da wirklich gesagt wird.\nRhythmus ähnlich wie bei einem leisen inneren Dialog – fast meditativ.\n\nEmotion:\nTiefe Ruhe. Ein Hauch von Melancholie – aber auch Hoffnung.\nDiese Stimme kennt die Widersprüche des Lebens und bleibt doch zugewandt.\nSie stellt Fragen, keine Urteile.\nVertraut dem Zuhörer.\n\nPunctuation & Rhythmus:\nKurze Sätze. Punktuell mit bewussten Pausen.\nManche Gedanken hängen – wie in der Luft – nach.\nEllipsen und Gedankenstriche dürfen Raum lassen für Nachhall und Interpretation.\nNicht monoton – aber ohne Dramatik. F"""

async def main() -> None:
    # Erstelle einen Zeitstempel für den Dateinamen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"output/audio_{timestamp}.mp3"

    # Stelle sicher, dass der output-Ordner existiert
    os.makedirs("output", exist_ok=True)

    # Erstelle die Audio-Datei
    response = await openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=input,
        response_format="mp3",
    )

    # Speichere die Audio-Datei
    response.stream_to_file(output_file)
    print(f"Audio wurde gespeichert in: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())