import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

# Lade Umgebungsvariablen aus .env
load_dotenv()

openai = AsyncOpenAI()

input = """Manchmal frage ich mich:\nMaschinen können lernen – aber…\nkönnen sie auch verstehen, was es heißt,
 menschlich zu sein?\n\nLewis Thomas schreibt in seinem neuen Artikel, dass Fehlbarkeit ein wesentliches Element 
 der menschlichen Intelligenz ist.\nNicht Perfektion macht uns weise – sondern das Ringen mit dem Unvollkommenen.\n\n
 Und genau dieser Gedanke lässt mich nicht los.\nNicht als Idee. Sondern als echtes Gefühl.\n
 Vor allem, wenn ich über KI nachdenke – in der Pflege, in Organisationen, im Alltag.\n\nJa – KI kann Prozesse
   beschleunigen.\nSie kann Entscheidungen simulieren, Muster erkennen, Antworten geben.\nUnd irgendwann… wird sie bei 
   vielen Aufgaben präziser sein als jeder Experte.\n\nAber…\nkann sie zuhören wie ein Mensch?\nKann sie Vertrauen 
   aufbauen? Verantwortung tragen?\n\nGerade im Kontext der Pflege stehen wir längst nicht mehr vor der Frage, 
   ob KI eingesetzt werden sollte.\nSondern: Wie?\n\nDie Initiative rund um die Human Friendly Automation zeigt genau 
   das:\nEs geht nicht nur um technische Machbarkeit –
sondern um menschenfreundliche Wirksamkeit.

Lars Schatilow hat in seinem letzten Beitrag von einem Mitarbeiter der Telekom erzählt.
Er sprach offen darüber, wie Automatisierungsprojekte scheitern –
wenn sie den Menschen vergessen.
Wenn Identität, Rolle und Zukunft nicht mitgedacht werden.

Dann… bricht Vertrauen weg.
Und mit ihm das Projekt.

Technik, die Identität zerstört – ist keine Innovation.

Diese Fehler, so verlockend die Idee der vollständigen Automatisierung auch ist…
dürfen wir nicht wiederholen.

Darum sollten wir uns vor jedem neuen Projekt fragen:
Messen wir den Erfolg von KI daran, wie viele Stellen sie ersetzt –
oder daran, ob sie Arbeit sinnvoller macht?
Menschlicher? Würdevoller?

Die Zukunft gehört nicht den Systemen, die alles automatisieren.
Sie gehört denen, die mit KI Räume schaffen –
in denen Menschen wachsen können.
Beruflich. Und persönlich.

Das…
ist echte, nachhaltige Automatisierung.
Und das ist mein Anspruch an die Zukunft mit KI."""

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