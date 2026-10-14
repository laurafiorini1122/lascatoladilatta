"""Prepara le immagini del sito a partire dai file in materiali.

Per ogni volume in src/content/volumi/*.json legge le immagini indicate nel
campo "sorgente" e scrive in public/immagini:

- volumi/<volume>/copertina-480.webp e -960.webp, il disegno colorato;
- volumi/<volume>/disegno-600.webp e -1200.webp, il disegno da colorare;
- condivisione/<volume>.jpg, l'anteprima per Facebook e gli altri social;
- condivisione/sito.jpg, l'anteprima delle pagine generali;
- prova/tamburello-<versione>-600.webp e -1200.webp, le tre versioni colorate
  della pagina di prova, e copia il PDF della pagina in public/.

Le immagini restano a risoluzione da schermo: non bastano per stampare.

    C:\\Users\\Scuola\\.venvs\\lascatoladilatta\\Scripts\\python.exe scripts\\prepara_immagini.py
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RADICE = Path(__file__).resolve().parent.parent
MATERIALI = RADICE / "materiali"
VOLUMI = RADICE / "src" / "content" / "volumi"
USCITA = RADICE / "public" / "immagini"
FONTS = MATERIALI / "fonts"

CREMA = (0xF4, 0xEC, 0xDB)
ROSSO = (0x9E, 0x38, 0x29)
TESTO = (0x2B, 0x26, 0x21)
SOTTOTITOLO_COPERTINA = "Anni '50 e '60. Da colorare e raccontare"


def larghezza(img: Image.Image, w: int) -> Image.Image:
    h = round(img.height * w / img.width)
    return img.resize((w, h), Image.LANCZOS)


def salva_webp(img: Image.Image, percorso: Path, qualita: int) -> None:
    percorso.parent.mkdir(parents=True, exist_ok=True)
    img.save(percorso, "WEBP", quality=qualita, method=6)
    print(f"  {percorso.relative_to(RADICE)}: {percorso.stat().st_size / 1024:.0f} KB")


def rifila(img: Image.Image) -> Image.Image:
    """Toglie il bordo trasparente intorno al disegno colorato."""
    box = img.getchannel("A").getbbox()
    return img.crop(box) if box else img


def font(nome: str, punti: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / nome), punti)


def testata(disegno: ImageDraw.ImageDraw, x: int, y: int, punti: int) -> int:
    """Scrive LA SCATOLA DI LATTA in rosso con la riga sotto, come in copertina."""
    f = font("AHN-Bold.ttf", punti)
    disegno.text((x, y), "LA SCATOLA DI LATTA", font=f, fill=ROSSO)
    w = disegno.textlength("LA SCATOLA DI LATTA", font=f)
    riga_y = y + round(punti * 1.45)
    disegno.line((x, riga_y, x + w, riga_y), fill=ROSSO, width=max(2, punti // 12))
    return riga_y


def a_capo(disegno, testo, f, massimo):
    righe, riga = [], ""
    for parola in testo.split():
        prova = f"{riga} {parola}".strip()
        if disegno.textlength(prova, font=f) <= massimo:
            riga = prova
        else:
            righe.append(riga)
            riga = parola
    righe.append(riga)
    return righe


def anteprima_volume(titolo: str, colorato: Image.Image, destinazione: Path) -> None:
    tela = Image.new("RGB", (1200, 630), CREMA)
    d = ImageDraw.Draw(tela)
    figura = colorato.copy()
    figura.thumbnail((420, 540), Image.LANCZOS)
    tela.paste(figura, (1200 - 70 - figura.width, (630 - figura.height) // 2), figura)

    y = testata(d, 70, 120, 30) + 60
    f_titolo = font("AHN-Bold.ttf", 76)
    for riga in a_capo(d, titolo, f_titolo, 1200 - 70 - figura.width - 140):
        d.text((70, y), riga, font=f_titolo, fill=TESTO)
        y += 92
    f_sotto = font("AHN-Italic.ttf", 34)
    spazio = 1200 - 70 - figura.width - 140
    if d.textlength(SOTTOTITOLO_COPERTINA, font=f_sotto) <= spazio:
        righe_sotto = [SOTTOTITOLO_COPERTINA]
    else:
        # Se non sta su una riga si va a capo dopo il punto, non a metà frase.
        prima, seconda = SOTTOTITOLO_COPERTINA.split(". ", 1)
        righe_sotto = [f"{prima}.", *a_capo(d, seconda, f_sotto, spazio)]
    for riga in righe_sotto:
        d.text((70, y + 16), riga, font=f_sotto, fill=TESTO)
        y += 46
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    tela.save(destinazione, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"  {destinazione.relative_to(RADICE)}: {destinazione.stat().st_size / 1024:.0f} KB")


def anteprima_sito(colorati: list[Image.Image], destinazione: Path) -> None:
    tela = Image.new("RGB", (1200, 630), CREMA)
    d = ImageDraw.Draw(tela)
    f = font("AHN-Bold.ttf", 64)
    testo = "La scatola di latta"
    w = d.textlength(testo, font=f)
    d.text(((1200 - w) / 2, 60), testo, font=f, fill=ROSSO)
    d.line(((1200 - w) / 2, 150, (1200 + w) / 2, 150), fill=ROSSO, width=4)
    f2 = font("AHN-Italic.ttf", 34)
    w2 = d.textlength(SOTTOTITOLO_COPERTINA, font=f2)
    d.text(((1200 - w2) / 2, 175), SOTTOTITOLO_COPERTINA, font=f2, fill=TESTO)
    # i primi due volumi della collana, uno a sinistra e uno a destra
    primi = colorati[:2]
    spazio = 1200 // max(1, len(primi))
    for i, img in enumerate(primi):
        figura = img.copy()
        figura.thumbnail((360, 330), Image.LANCZOS)
        x = (spazio * i) + (spazio - figura.width) // 2
        tela.paste(figura, (x, 630 - 35 - figura.height), figura)
    tela.save(destinazione, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"  {destinazione.relative_to(RADICE)}: {destinazione.stat().st_size / 1024:.0f} KB")


# Le versioni colorate della pagina di prova: nome nel sito -> file in materiali.
TAMBURELLO = {
    "matite": "PROVA_tamburello_colorato_matita_web.jpg",
    "pennarelli": "PROVA_tamburello_colorato_pennarello_decorato_web.jpg",
    "sfondo": "PROVA_tamburello_colorato_sfondo_righe_web.jpg",
}


def pagina_di_prova() -> None:
    print("Pagina di prova")
    cartella = MATERIALI / "pagina-di-prova"
    for nome, sorgente in TAMBURELLO.items():
        img = Image.open(cartella / sorgente).convert("RGB")
        for w in (600, 1200):
            salva_webp(larghezza(img, w), USCITA / "prova" / f"tamburello-{nome}-{w}.webp", 82)
    pdf = RADICE / "public" / "tamburello-pagina-da-provare.pdf"
    pdf.write_bytes((cartella / "PROVA_tamburello.pdf").read_bytes())
    print(f"  {pdf.relative_to(RADICE)}: {pdf.stat().st_size / 1024:.0f} KB")


def main() -> None:
    volumi = sorted(
        (json.loads(p.read_text(encoding="utf-8")) | {"slug": p.stem} for p in VOLUMI.glob("*.json")),
        key=lambda v: v["ordine"],
    )
    colorati = []
    for v in volumi:
        print(v["titolo"])
        cartella = USCITA / "volumi" / v["slug"]
        imm = v["immagini"]

        colorato = rifila(Image.open(MATERIALI / imm["copertina"]["sorgente"]).convert("RGBA"))
        colorati.append(colorato)
        for w in (480, 960):
            salva_webp(larghezza(colorato, w), cartella / f"copertina-{w}.webp", 82)

        tratto = Image.open(MATERIALI / imm["disegno"]["sorgente"]).convert("L")
        for w in (600, 1200):
            salva_webp(larghezza(tratto, w), cartella / f"disegno-{w}.webp", 80)

        anteprima_volume(v["titolo"], colorato, USCITA / "condivisione" / f"{v['slug']}.jpg")

    anteprima_sito(colorati, USCITA / "condivisione" / "sito.jpg")
    pagina_di_prova()


if __name__ == "__main__":
    main()
