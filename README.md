# OpenAI Text-to-Speech und Transkription

Dieses Projekt enthält zwei Python-Skripte, die die OpenAI API für Text-to-Speech und Audio-Transkription nutzen.

## Funktionen

- `main.py`: Konvertiert Text in Sprache (Text-to-Speech)
- `transkr.py`: Transkribiert Audio-Dateien in Text

## Voraussetzungen

- Python 3.8 oder höher
- OpenAI API-Key
- Virtuelle Python-Umgebung (empfohlen)

## Installation

1. Klonen Sie das Repository:
```bash
git clone https://github.com/goldikolb/openaifm-.git
cd openaifm-
```

2. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie diese:
```bash
python -m venv myenv
# Unter Windows:
.\myenv\Scripts\activate
# Unter Linux/Mac:
source myenv/bin/activate
```

3. Installieren Sie die erforderlichen Pakete:
```bash
pip install -r requirements.txt
```

4. Erstellen Sie eine `.env`-Datei im Hauptverzeichnis und fügen Sie Ihren OpenAI API-Key hinzu:
```
OPENAI_API_KEY=ihr-api-key-hier
```

## Verwendung

### Text-to-Speech (main.py)

1. Öffnen Sie `main.py` und passen Sie den Text in der Variable `input` an
2. Führen Sie das Skript aus:
```bash
python main.py
```
3. Die generierte Audio-Datei wird im Ordner `output` gespeichert

### Audio-Transkription (transkr.py)

1. Legen Sie die zu transkribierende Audio-Datei im Ordner `audio` ab
2. Passen Sie in `transkr.py` den Dateipfad zur Audio-Datei an
3. Führen Sie das Skript aus:
```bash
python transkr.py
```
4. Die Transkription wird im Ordner `output` als Textdatei gespeichert

## Ordnerstruktur

```
.
├── main.py              # Text-to-Speech Skript
├── transkr.py          # Transkriptions-Skript
├── requirements.txt    # Python-Abhängigkeiten
├── .env               # OpenAI API-Key (nicht im Repository)
├── audio/             # Ordner für Audio-Dateien
└── output/            # Ordner für generierte Dateien
```

## Dateinamen-Konvention

- Audio-Dateien: `audio_YYYYMMDD_HHMMSS.mp3`
- Transkriptionen: `transcription_YYYYMMDD_HHMMSS.txt`

## Fehlerbehebung

- Stellen Sie sicher, dass Ihr OpenAI API-Key korrekt in der `.env`-Datei eingetragen ist
- Überprüfen Sie, ob die virtuelle Umgebung aktiviert ist
- Stellen Sie sicher, dass alle erforderlichen Pakete installiert sind

## Lizenz

MIT License

## Autor

Christian Kolb

## Kontakt

Wenn Sie Fragen haben oder einen Beitrag leisten möchten, zögern Sie nicht, uns über unsere Webseite zu kontaktieren: [pflege-ai.de](https://pflege-ai.de/).

[![Website](https://img.shields.io/badge/Pflege--AI-Webseite-%230f0122?style=flat&logo=Web&logoColor=ff8154)](https://pflege-ai.de/)

## Follow me on Social Media

[![Instagram](https://img.shields.io/badge/Instagram-Follow%20@pflege__ki-blue?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/pflege_ki/)

## Support my work

[![Buy me a coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Pflege_KI-FFDD00)](https://buymeacoffee.com/pflege_ki)