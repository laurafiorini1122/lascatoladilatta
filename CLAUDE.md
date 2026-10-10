# CLAUDE.md

Guida per Claude quando lavora a questo repository: il sito lascatoladilatta.it.

## Il progetto

La scatola di latta è una collana di quaderni da colorare e dei ricordi, autopubblicata su Amazon KDP. Ogni quaderno raccoglie 15 oggetti della vita quotidiana in Italia negli anni '50 e '60: a destra il disegno da colorare, a sinistra la pagina per scrivere il ricordo; il retro dei disegni è bianco. I primi volumi sono *Calzoni corti 1* e *Trecce e fiocchi 1*; seguiranno *Calzoni corti 2*, *Trecce e fiocchi 2* e una quindicina di temi.

I lettori hanno fra i 65 e gli 80 anni. Chi compra è spesso un figlio o un nipote che cerca un regalo, oppure un animatore di un centro diurno o di una residenza.

Il sito deve essere online prima della pubblicazione su Amazon, perché il retro di copertina rimanda a lascatoladilatta.it per gli esempi e la pagina di prova.

Il documento di progetto è `materiali/La_scatola_di_latta_progetto.md` (paragrafi 1, 3, 5, 9 e 10 per il sito). Per il sito valgono le sue decisioni; in caso di contrasto si chiede a Laura.

## Come lavorare con Laura

- Laura non è una programmatrice: ogni passaggio si spiega in italiano semplice, dicendo con precisione che cosa deve fare lei (creare account, cliccare, confermare).
- Davanti a una decisione si espongono le possibilità con i pro e i contro, in un discorso e non con un menu a scelta multipla, e si aspetta la risposta.
- Piccoli passi: dopo ogni passo si mostra il sito in anteprima, si fa un commit con il messaggio in italiano e **non si fa push né si pubblica senza che Laura lo chieda**.
- Ogni decisione presa e ogni cosa da fare si annota con la data in `docs/decisioni.md`.
- Ogni testo scritto da Claude è una proposta e va segnalato come tale. I testi del retro di copertina (`materiali/copertine/Retro_*.txt`) sono approvati e si usano così come sono.

## Regole che non si discutono

- **Repository pubblico.** Il sito si pubblica con GitHub Pages dall'account `laurafiorini1122`, quindi tutto quello che entra nel repository è leggibile da chiunque. Git è configurato in questo progetto con l'indirizzo noreply `284369532+laurafiorini1122@users.noreply.github.com`. Prima di ogni commit si controlla che nei file non ci siano email personali né documenti di lavoro.
- **La cartella `materiali` non entra mai nel repository** (è nel `.gitignore`, insieme a `Prompt_avvio_Claude_Code.md`). Si legge, non si modifica, e nel sito si copia solo ciò che serve già trasformato.
- **Niente dati personali.** Nessun modulo, nessun cookie, nessuno strumento di statistica o di tracciamento (neppure quelli dell'hosting), nessuna risorsa da server esterni: niente Google Fonts, CDN, video o mappe incorporati. I collegamenti verso altri siti sono ammessi; le risorse caricate dalla pagina no.
- **Nessun legame** con Stagione Autentica né con altri siti di Laura.
- **Sito statico**, senza database e senza server, a costo zero o quasi.
- **Accessibilità WCAG 2.2 AA almeno**: corpo base 20 px, contrasto alto, pulsanti e collegamenti grandi (almeno 48 px di altezza), navigazione completa da tastiera, testo alternativo per ogni immagine, `lang="it"`.
- **Leggerezza**: immagini ridimensionate e in WebP, nessuno script se non serve.
- **Ricerca e condivisione**: ogni pagina ha titolo (sotto i 60 caratteri), descrizione (sotto i 155), anteprima Open Graph con l'immagine giusta, ed è nella sitemap.
- **Amazon**: collegamenti semplici, senza programmi di affiliazione, per restare dentro le condizioni di GitHub Pages.

## Aspetto

- Colori presi dai PDF delle copertine: fondo crema `#f4ecdb`, rosso latta `#9e3829`, testo `#2b2621`. La carta dei disegni è bianca.
- Carattere: AHN, la versione modificata di Atkinson Hyperlegible Next (zero senza barra, "q" con la gamba dritta) che sta in `materiali/fonts`. Non si usa il carattere originale. Licenza SIL OFL 1.1: la licenza accompagna i caratteri in `public/fonts/OFL.txt`; i nomi degli autori originali non si usano per promuovere la versione modificata.
- Stile semplice, caldo e adulto: mai infantile, mai da "prodotto per anziani".

## Stile dei testi

- niente trattini lunghi: al loro posto due punti, virgole o punti;
- niente virgola prima di "e" e di "o" se non strettamente necessaria;
- registro né troppo formale né troppo informale; si dà del tu a chi visita;
- niente lessico clinico e nessuna promessa di benefici sulla memoria;
- il sito descrive i quaderni e non chi li userà: mai "per anziani", mai "per la demenza";
- i nipoti possono comparire come occasione d'uso ("da colorare anche insieme ai nipoti"), mai come destinatari.

## Comandi

```bash
npm run dev      # anteprima su http://localhost:4321/lascatoladilatta/
npm run build    # costruisce il sito in dist/
npm run check    # controllo dei tipi
```

L'anteprima si avvia con `npm run dev` in una scheda del terminale e poi si apre l'indirizzo nel browser: `preview_start` per nome tende a prendere la configurazione di un altro progetto.

Gli script Python usano l'ambiente `C:\Users\Scuola\.venvs\lascatoladilatta` (Pillow, fontTools, brotli), fuori dal repository:

```bash
C:\Users\Scuola\.venvs\lascatoladilatta\Scripts\python.exe scripts\prepara_immagini.py
C:\Users\Scuola\.venvs\lascatoladilatta\Scripts\python.exe scripts\prepara_caratteri.py
```

## Struttura

- `src/content/volumi/*.json`: un file per volume (titolo, sottotitolo, testo del retro, 15 giochi, collegamento Amazon, immagini). Lo schema in `src/content.config.ts` blocca la costruzione se manca un campo.
- `src/pages/`: home, `quaderni/` (elenco e una pagina per volume, creata da sola), `esempi/`, `prova/`, `contatti/`, `note-legali/`, `404`, `sitemap.xml`, `robots.txt`.
- `src/sito.ts`: nome, email, PDF della pagina di prova, voci del menu e la funzione `url()` da usare per **ogni** collegamento interno.
- `src/fonts/`: i caratteri in WOFF2. `public/immagini/`: le immagini già pronte.
- `scripts/`: preparazione di immagini e caratteri da `materiali`.
- `.github/workflows/pubblica.yml`: a ogni push su `main` GitHub costruisce e pubblica il sito.

### Aggiungere un volume

1. Mettere in `materiali` il disegno colorato e il disegno da mostrare.
2. Copiare un file di `src/content/volumi/` e cambiare i dati (il nome del file diventa l'indirizzo della pagina).
3. Lanciare `scripts/prepara_immagini.py`.
4. Controllare l'anteprima: la pagina, la tessera in home e la sitemap si aggiornano da sole.

## Indirizzo e dominio

Fino al collegamento del dominio il sito vive su `https://laurafiorini1122.github.io/lascatoladilatta/`. Per passare a lascatoladilatta.it si cambiano `site` e `base` in `astro.config.mjs` e si aggiunge `public/CNAME`. Le istruzioni per Register.it (DNS, verifica del dominio su GitHub, HTTPS, casella info@lascatoladilatta.it) vanno date a Laura passo per passo al momento giusto.
