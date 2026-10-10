# Decisioni e cose da fare

## Decisioni

### 10 ottobre 2026

- **Strumento**: il sito si costruisce con Astro 7. Ogni volume è un file di dati in `src/content/volumi/`; pagina, tessera in home e sitemap si creano da sole.
- **Pubblicazione**: GitHub Pages dal repository pubblico `laurafiorini1122/lascatoladilatta`, con costruzione automatica tramite GitHub Actions. Vercel era già stato scartato.
- **Condizioni di GitHub Pages**: vietano i siti "rivolti principalmente a facilitare transazioni commerciali". Un sito vetrina che non vende nulla e rimanda ad Amazon, secondo l'interpretazione più comune, è ammesso, ma GitHub non lo scrive in modo esplicito. Per prudenza: collegamenti Amazon semplici, senza affiliazione. In caso di problemi il sito si sposta su un altro servizio statico (per esempio Cloudflare Pages) tenendo il dominio.
- **Indirizzo provvisorio**: `https://laurafiorini1122.github.io/lascatoladilatta/`.
- **Identità git**: `Laura Fiorini` con l'indirizzo noreply di GitHub, impostata solo in questo progetto.
- **Colori**: quelli dei PDF delle copertine. Fondo `#f4ecdb`, rosso `#9e3829`, testo `#2b2621` (non il nero pieno).
- **Carattere**: AHN, convertito in WOFF2, con la licenza OFL in `public/fonts/OFL.txt`. La licenza non dichiara nomi riservati.
- **Disegni sul sito**: un solo disegno da colorare per volume, il numero 1 (le biglie, la campana), che compare comunque nell'anteprima di Amazon. Risoluzione da schermo, non da stampa.
- **Campana**: `TF1_01_campana_v3.png` è la versione definitiva, anche se il nome non finisce in `_def`.
- **Email**: info@lascatoladilatta.it, ricomposto nella pagina da un piccolo script. Senza script compare scritto a parole ("info (chiocciola) lascatoladilatta.it").
- **Pagine**: home, I quaderni, una pagina per volume, Esempi, Pagina da provare, Contatti, Note legali, Pagina non trovata.
- **Telemetria di Astro**: disattivata sul computer e nella costruzione su GitHub.
- **Vercel ricontrollato e confermato escluso**: le sue regole (aggiornate al 14 settembre 2026) riservano il piano gratuito all'uso non commerciale e contano come commerciale anche "pubblicizzare la vendita di un prodotto", quindi un sito che rimanda ad Amazon richiederebbe il piano Pro a pagamento. Si resta su GitHub Pages; l'alternativa gratuita che ammette l'uso commerciale è Cloudflare Pages.

## Testi da rivedere (proposte di Claude)

- Testi della home, della pagina I quaderni, di Esempi, della Pagina da provare, di Contatti, delle Note legali e della pagina non trovata.
- Titoli e descrizioni per i motori di ricerca di tutte le pagine.
- Nomi dei giochi negli elenchi dei volumi, ricavati dai nomi dei file e dai testi del retro: da confrontare con i titoli degli Excel.
- Testi alternativi delle immagini.

## Da fare

- [ ] Laura: su GitHub, Settings → Emails, attivare "Keep my email addresses private" e "Block command line pushes that expose my email".
- [ ] Laura: rivedere i testi proposti.
- [ ] Decidere se nelle note legali va indicato chi cura il sito (il nome di Laura o solo la collana).
- [ ] Immagini delle pagine colorate per la pagina Esempi (preparate da Laura).
- [ ] PDF della pagina di prova, in formato A4 (preparato da Laura).
- [ ] Creare il repository su GitHub e fare il primo push, quando Laura lo chiede.
- [ ] Attivare GitHub Pages con origine "GitHub Actions".
- [ ] Collegamenti Amazon dei due volumi, quando sono pubblicati.
- [ ] Comprare lascatoladilatta.it su Register.it e collegarlo: DNS, `public/CNAME`, `site` e `base` in `astro.config.mjs`, verifica del dominio su GitHub, HTTPS.
- [ ] Attivare la casella info@lascatoladilatta.it su Register.it.
