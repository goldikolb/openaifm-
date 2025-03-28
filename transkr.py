from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import os

# Lade Umgebungsvariablen aus .env
load_dotenv()

client = OpenAI()
audio_file = open("Pfad-zu-der-Audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe", 
    file=audio_file
)

# Erstelle einen Zeitstempel für den Dateinamen
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"output/transcription_{timestamp}.txt"

# Stelle sicher, dass der output-Ordner existiert
os.makedirs("output", exist_ok=True)

# Speichere den Transkriptionstext in einer Datei
with open(output_file, "w", encoding="utf-8") as f:
    f.write(transcription.text)

print(f"Transkription wurde gespeichert in: {output_file}")
print("\nTranskriptionstext:")
print(transcription.text)