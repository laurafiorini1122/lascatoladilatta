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
- **Pagine**: home, I quaderni, una pagina per volume, Pagina da provare, Contatti, Note legali, Pagina non trovata.
- **Telemetria di Astro**: disattivata sul computer e nella costruzione su GitHub.
- **Vercel ricontrollato e confermato escluso**: le sue regole (aggiornate al 14 settembre 2026) riservano il piano gratuito all'uso non commerciale e contano come commerciale anche "pubblicizzare la vendita di un prodotto", quindi un sito che rimanda ad Amazon richiederebbe il piano Pro a pagamento. Si resta su GitHub Pages; l'alternativa gratuita che ammette l'uso commerciale è Cloudflare Pages.

- **Home rifatta** dopo la revisione di Laura: niente disegni colorati in apertura, tutto centrato, in "Come funziona" le quattro pagine delle biglie con i testi del quaderno, carta avorio `#fbf7ee` al posto del bianco puro, tolto "a casa" dagli inviti a stampare.
- **Pagina da provare**: il soggetto è il tamburello, il gioco con la racchetta di pelle, che non compare in nessun quaderno (era fra le riserve dei giochi, "da chiarire"). Sotto il pulsante per scaricarla, la stessa pagina colorata in tre modi (matite, pennarelli, sfondo decorativo) e il collegamento agli Esempi.

- **Pagina Esempi tolta**: gli esempi colorati e la pagina da provare stanno insieme in `/prova/`, intitolata "Esempi colorati e una pagina da provare" (voce del menu "Prova una pagina"). Prima le versioni colorate del tamburello, poi il pulsante per scaricarlo. Il retro di copertina resta com'è: la pagina mantiene tutte e due le promesse.

### 12 ottobre 2026

- **Pagina di prova completa**: in `/prova/` le tre versioni colorate del tamburello (matite, pennarelli, sfondo decorativo) al posto dei segnaposto, intere e senza ritagli, e il pulsante "Scarica la pagina da provare (PDF, 2 pagine A4)". Il PDF ha due pagine A4 (testo con le righe e disegno), quindi si stampa su due fogli: corretti la frase della pagina e la descrizione per i motori di ricerca. Le immagini si preparano con `scripts/prepara_immagini.py` in WebP, il PDF è `public/tamburello-pagina-da-provare.pdf`.
- **Home**: il riquadro "Prima di scegliere" non ha un posto per un'immagine, quindi resta com'è.
- **Pubblicazione**: dominio lascatoladilatta.it comprato da Laura su Register.it (scadenza 12 ottobre 2027). Creato il repository pubblico `laurafiorini1122/lascatoladilatta`, attivato GitHub Pages con origine GitHub Actions, verificato il dominio nelle impostazioni dell'account GitHub. Nella zona DNS di Register.it: il record A di parcheggio (195.110.124.133) sostituito con i quattro indirizzi di GitHub Pages (185.199.108-111.153), il CNAME `www` puntato a `laurafiorini1122.github.io.`, aggiunto il TXT `_github-pages-challenge-laurafiorini1122`. I record della posta (MX, SPF, DKIM, autodiscover, autoconfig, authsmtp, pop, PEC) e il CNAME `ftp` sono rimasti com'erano. Nel pannello nuovo di Register.it il nome "@" non indica il dominio principale: crea "@.lascatoladilatta.it", va corretto in "lascatoladilatta.it" nella riga dopo il salvataggio.

### 13 ottobre 2026

- **Revisione dei testi con Laura** (fatta nella chat del Progetto, correzioni già scritte nei file): in home descrizione per i motori di ricerca senza "dell'Italia degli anni" ("con gli oggetti di tutti i giorni degli anni '50 e '60 in Italia"), a capo dopo "Ogni oggetto occupa quattro pagine.", frase finale di "Come funziona" riscritta ("Non c'è un ordine da seguire..." e "libro di ricordi da conservare"), "Scaricala, stampala e prova a completarla." in home e nelle pagine dei volumi (senza "Poi"). In `/prova/` l'introduzione dice che le pagine sono due, "simili a quelle del libro"; titolo "Ora tocca a te"; pulsante "Scarica le pagine da provare (PDF, 2 fogli A4)". "Nell'Italia degli anni '50 e '60" nell'apertura della home resta. Nel retro dei volumi "un libro di ricordi da conservare" (cambiato anche nelle copertine, rigenerate). Il disegno di esempio nelle pagine dei volumi resta. Niente terza pagina nella pagina da provare.

### 14 ottobre 2026

- **Sottotitolo** cambiato in "Anni '50 e '60. Da colorare e raccontare" (tolto il secondo "da"), anche nei sottotitoli lunghi, nella prima riga del retro e nelle descrizioni per i motori di ricerca. Copertine nuove in materiali/copertine.
- **Anteprime per i social** rigenerate con `scripts/prepara_immagini.py`. Proposta di Claude: quando il sottotitolo non sta su una riga va a capo dopo il punto ("Anni '50 e '60." / "Da colorare e raccontare"), come succede nell'anteprima di *Calzoni corti 1*.
- **Pubblicazione**: le correzioni del 13 ottobre (commit `8005f66`) e quelle del 14 ottobre (commit `238136b`) sono online. Controllati sul sito online la home, le due pagine dei volumi e la pagina di prova.
- **Certificato HTTPS**: emesso da Let's Encrypt il 12 ottobre 2026 per lascatoladilatta.it e www.lascatoladilatta.it, scade il 10 gennaio 2027 e GitHub lo rinnova da solo. Il sito risponde già in https, ma l'indirizzo con http non viene ancora girato su https.

## Testi da rivedere (proposte di Claude)

- Testi della home, della pagina I quaderni, della pagina Esempi colorati e una pagina da provare, di Contatti, delle Note legali e della pagina non trovata.
- Titoli e descrizioni per i motori di ricerca di tutte le pagine.
- Nomi dei giochi negli elenchi dei volumi, ricavati dai nomi dei file e dai testi del retro: da confrontare con i titoli degli Excel.
- Testi alternativi delle immagini.

## Da fare

- [ ] Laura: su GitHub, Settings → Emails, attivare "Keep my email addresses private" e "Block command line pushes that expose my email".
- [ ] Laura: rivedere i testi proposti.
- [ ] Quando i quaderni saranno di più: rimpicciolire i disegni colorati nelle tessere dei volumi (in home e nella pagina I quaderni), che con tanti volumi diventano troppo grandi.
- [ ] Decidere se nelle note legali va indicato chi cura il sito (il nome di Laura o solo la collana).
- [x] PDF della pagina di prova del tamburello, in formato A4 (preparato da Laura).
- [x] Tre versioni colorate della pagina del tamburello: matite, pennarelli, sfondo decorativo.
- [ ] Decidere se aggiungere l'indirizzo del sito nel colophon dei quaderni, come prevede il documento di progetto: nelle bozze del 10 ottobre non c'è. Si corregge nel foglio "Pagine fisse" degli Excel e si rigenerano le bozze.
- [ ] Togliere il tamburello dalle riserve nel foglio Archivio di `Giochi_quattro_quaderni.xlsx` (lo fa Laura: l'Excel è un file di lavoro).
- [x] Creare il repository su GitHub e fare il primo push.
- [x] Attivare GitHub Pages con origine "GitHub Actions".
- [ ] Collegamenti Amazon dei due volumi, quando sono pubblicati.
- [x] Comprare lascatoladilatta.it su Register.it e impostare i DNS, `public/CNAME`, `site` in `astro.config.mjs` e la verifica del dominio su GitHub.
- [ ] Inserire lascatoladilatta.it come dominio personalizzato nelle impostazioni Pages del repository e attivare "Enforce HTTPS" quando GitHub ha emesso il certificato.
- [x] Attivare la casella info@lascatoladilatta.it su Register.it (12 ottobre 2026: casella creata nel pacchetto del dominio, 2 GB; la password l'ha scelta e inserita Laura). Server: IMAP pop.securemail.pro porta 993 SSL, SMTP authsmtp.securemail.pro porta 465 SSL, nome utente l'indirizzo completo; webmail su webmail.register.it.
- [x] Posta della collana: inoltro attivo verso la casella personale di Laura (webmail Register.it → Impostazioni → Inoltro, "Invia copia a"), con l'originale che resta anche in info@. L'indirizzo personale non va scritto in questo repository pubblico.
- [ ] Laura: mandare un messaggio di prova a info@lascatoladilatta.it e controllare che arrivi anche nella casella personale.
- [ ] Facoltativo: in Gmail, "Invia messaggio come" info@lascatoladilatta.it (server authsmtp.securemail.pro, porta 465 SSL), per rispondere senza mostrare l'indirizzo personale.
- [x] Correzioni dei testi del 13 ottobre 2026 (home, Prova una pagina, pagine e retro dei volumi): pubblicate il 14 ottobre 2026.
- [x] Sottotitolo cambiato il 14 ottobre 2026 in "Anni '50 e '60. Da colorare e raccontare" (tolto il secondo "da"), anche nei sottotitoli lunghi e nella prima riga del retro. Testi già corretti da Claude in src/sito.ts, src/layouts/Base.astro, src/pages/index.astro, src/pages/contatti/index.astro, src/content/volumi/*.json e scripts/prepara_immagini.py. Claude Code: rigenerare con scripts/prepara_immagini.py le anteprime per i social (condivisione/*.jpg), che contengono ancora il sottotitolo vecchio, controllare e pubblicare. Copertine nuove in materiali/copertine. Fatto e pubblicato il 14 ottobre 2026.
