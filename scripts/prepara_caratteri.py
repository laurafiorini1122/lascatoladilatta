"""Converte i tre file del carattere AHN da TTF a WOFF2 per il web.

Legge da materiali/fonts e scrive in src/fonts; la licenza sta in public/fonts/OFL.txt. Il carattere non viene
modificato: cambia solo il formato del file. Va rilanciato solo se cambiano i
file in materiali/fonts.

    C:\\Users\\Scuola\\.venvs\\lascatoladilatta\\Scripts\\python.exe scripts\\prepara_caratteri.py
"""
from pathlib import Path

from fontTools.ttLib import TTFont

RADICE = Path(__file__).resolve().parent.parent
SORGENTE = RADICE / "materiali" / "fonts"
DESTINAZIONE = RADICE / "src" / "fonts"

FILE = {
    "AHN-Regular.ttf": "ahn-regular.woff2",
    "AHN-Bold.ttf": "ahn-bold.woff2",
    "AHN-Italic.ttf": "ahn-italic.woff2",
}


def main() -> None:
    DESTINAZIONE.mkdir(parents=True, exist_ok=True)
    for ttf, woff2 in FILE.items():
        font = TTFont(SORGENTE / ttf)
        font.flavor = "woff2"
        font.save(DESTINAZIONE / woff2)
        kb = (DESTINAZIONE / woff2).stat().st_size / 1024
        print(f"{woff2}: {kb:.0f} KB")


if __name__ == "__main__":
    main()

