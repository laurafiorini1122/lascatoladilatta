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
- **Enforce HTTPS** attivato da Laura nelle impostazioni Pages (il dominio personalizzato lascatoladilatta.it c'era già, con il controllo DNS riuscito). Ora http://lascatoladilatta.it, http://www.lascatoladilatta.it e https://www.lascatoladilatta.it portano tutti a https://lascatoladilatta.it.
- **Pagine dei volumi**: la parte da "Il quaderno" in giù era appoggiata al bordo sinistro, con un grande vuoto a destra. Ora è una colonna al centro della pagina, con il testo allineato a sinistra (scartato il testo tutto centrato, che nei paragrafi lunghi e nell'elenco dei giochi si legge peggio). Sul telefono non cambia niente.

### 15 ottobre 2026

- **Controllo finale prima della pubblicazione dei quaderni**: tutte le pagine, le immagini, la sitemap, il robots.txt e il PDF della pagina di prova rispondono in https; http, www e l'indirizzo github.io portano a https://lascatoladilatta.it. Il sottotitolo "Anni '50 e '60. Da colorare e raccontare" è giusto in tutte le pagine e nelle tre anteprime per i social. Sul telefono (360 px) nessuna pagina scorre di lato e il testo resta ad almeno 20 px. Sitemap e robots.txt sono corretti e ogni pagina indica il proprio indirizzo ufficiale: il sito è pronto per Google Search Console.
- **Correzioni dopo il controllo**: nelle Note legali il collegamento all'informativa sulla privacy di GitHub porta alla versione inglese (quella italiana non esiste più), con "(in inglese)"; i nomi dei giochi nelle pagine dei volumi sono quelli stampati nel libro (Excel e bozze), per esempio "La barchetta e l'aeroplanino di carta" e "I pattini a rotelle di ferro"; l'indirizzo email nei Contatti è un collegamento alto almeno 48 px; la pagina non trovata non dichiara più un indirizzo per i social.
- **Pubblicazione**: le correzioni del 15 ottobre (commit `c278dcf`) sono online. Controllato che tutte le pagine, la sitemap e il robots.txt online siano uguali alla versione corretta e che il nuovo collegamento all'informativa di GitHub funzioni.
- **Titolo dei volumi senza numero** (deciso da Laura): "Calzoni corti" e "Trecce e fiocchi", come su copertina, frontespizio e scheda KDP. Sul sito cambiati il titolo delle pagine dei volumi, delle tessere, dei titoli per i motori di ricerca e delle anteprime per i social (rigenerate con `scripts/prepara_immagini.py`). Gli indirizzi delle pagine restano `/quaderni/calzoni-corti-1/` e `/quaderni/trecce-e-fiocchi-1/`, come nel documento di progetto (paragrafo 5); il numero 1 resta anche nei nomi dei file. I secondi volumi avranno il titolo con il 2.
- **File definitivi dei libri** in `materiali`: Excel aggiornati, interni definitivi `Interno_Calzoni_corti_1.pdf` e `Interno_Trecce_e_fiocchi_1.pdf`, `Scheda_KDP_volumi_1.md` e documento di progetto aggiornato. Le `Bozza_*.pdf` sono superate. Ricontrollati: frontespizio e colophon degli Excel e degli interni hanno il sottotitolo nuovo e il colophon chiude con lascatoladilatta.it; i quindici giochi del sito sono identici a quelli degli Excel e degli interni; il tamburello nel foglio Archivio di `Giochi_quattro_quaderni.xlsx` è segnato come usato per la pagina di prova del sito, "non va nei quaderni".

### 16 ottobre 2026

- **Quaderni in preparazione** (deciso da Laura): nella pagina I quaderni, sotto le schede dei due volumi, un paragrafo con il testo di Laura "In preparazione altri quaderni: la scuola, la casa, la cucina, le feste e altri giochi." Solo l'elenco dei temi, senza promesse di date, senza pulsanti e senza collegamenti.

## Testi da rivedere (proposte di Claude)

- Testi della home, della pagina I quaderni, della pagina Esempi colorati e una pagina da provare, di Contatti, delle Note legali e della pagina non trovata.
- Titoli e descrizioni per i motori di ricerca di tutte le pagine.
- Testi alternativi delle immagini.

## Da fare

- [ ] Laura: su GitHub, Settings → Emails, attivare "Keep my email addresses private" e "Block command line pushes that expose my email".
- [ ] Laura: rivedere i testi proposti.
- [ ] Quando i quaderni saranno di più: rimpicciolire i disegni colorati nelle tessere dei volumi (in home e nella pagina I quaderni), che con tanti volumi diventano troppo grandi.
- [ ] Decidere se nelle note legali va indicato chi cura il sito (il nome di Laura o solo la collana).
- [x] PDF della pagina di prova del tamburello, in formato A4 (preparato da Laura).
- [x] Tre versioni colorate della pagina del tamburello: matite, pennarelli, sfondo decorativo.
- [x] Indirizzo del sito nel colophon dei quaderni: c'è, nel foglio "Pagine fisse" degli Excel e negli interni definitivi. Controllato il 15 ottobre 2026.
- [x] Sottotitolo nuovo "Da colorare e raccontare" nel frontespizio e nel colophon degli Excel e degli interni definitivi. Controllato il 15 ottobre 2026.
- [x] Titolo dei volumi: senza numero su copertina, Amazon e sito (deciso da Laura il 15 ottobre 2026).
- [x] Tamburello nel foglio Archivio di `Giochi_quattro_quaderni.xlsx`: segnato come usato per la pagina di prova del sito ed escluso dai quaderni. Controllato il 15 ottobre 2026.
- [x] Creare il repository su GitHub e fare il primo push.
- [x] Attivare GitHub Pages con origine "GitHub Actions".
- [ ] Collegamenti Amazon dei due volumi, quando sono pubblicati.
- [x] Comprare lascatoladilatta.it su Register.it e impostare i DNS, `public/CNAME`, `site` in `astro.config.mjs` e la verifica del dominio su GitHub.
- [x] Inserire lascatoladilatta.it come dominio personalizzato nelle impostazioni Pages del repository e attivare "Enforce HTTPS" quando GitHub ha emesso il certificato. Fatto il 14 ottobre 2026.
- [x] Attivare la casella info@lascatoladilatta.it su Register.it (12 ottobre 2026: casella creata nel pacchetto del dominio, 2 GB; la password l'ha scelta e inserita Laura). Server: IMAP pop.securemail.pro porta 993 SSL, SMTP authsmtp.securemail.pro porta 465 SSL, nome utente l'indirizzo completo; webmail su webmail.register.it.
- [x] Posta della collana: inoltro attivo verso la casella personale di Laura (webmail Register.it → Impostazioni → Inoltro, "Invia copia a"), con l'originale che resta anche in info@. L'indirizzo personale non va scritto in questo repository pubblico.
- [ ] Laura: mandare un messaggio di prova a info@lascatoladilatta.it e controllare che arrivi anche nella casella personale.
- [ ] Facoltativo: in Gmail, "Invia messaggio come" info@lascatoladilatta.it (server authsmtp.securemail.pro, porta 465 SSL), per rispondere senza mostrare l'indirizzo personale.
- [x] Correzioni dei testi del 13 ottobre 2026 (home, Prova una pagina, pagine e retro dei volumi): pubblicate il 14 ottobre 2026.
- [x] Sottotitolo cambiato il 14 ottobre 2026 in "Anni '50 e '60. Da colorare e raccontare" (tolto il secondo "da"), anche nei sottotitoli lunghi e nella prima riga del retro. Testi già corretti da Claude in src/sito.ts, src/layouts/Base.astro, src/pages/index.astro, src/pages/contatti/index.astro, src/content/volumi/*.json e scripts/prepara_immagini.py. Claude Code: rigenerare con scripts/prepara_immagini.py le anteprime per i social (condivisione/*.jpg), che contengono ancora il sottotitolo vecchio, controllare e pubblicare. Copertine nuove in materiali/copertine. Fatto e pubblicato il 14 ottobre 2026.
