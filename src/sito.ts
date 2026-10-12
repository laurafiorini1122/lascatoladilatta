// Impostazioni comuni a tutto il sito.

export const NOME = 'La scatola di latta';
export const SOTTOTITOLO = "Anni '50 e '60. Da colorare e da raccontare";

// L'indirizzo email è diviso in due parti e viene ricomposto nella pagina da un
// piccolo script, così i programmi che raccolgono indirizzi non lo trovano.
export const EMAIL = { utente: 'info', dominio: 'lascatoladilatta.it' };

// Percorso del PDF della pagina di prova dentro public/, oppure null finché
// il file non è pronto.
export const PAGINA_DI_PROVA: string | null = '/tamburello-pagina-da-provare.pdf';

// Voci del menu principale.
export const MENU = [
  { href: '/', testo: 'Home' },
  { href: '/quaderni/', testo: 'I quaderni' },
  { href: '/prova/', testo: 'Prova una pagina' },
  { href: '/contatti/', testo: 'Contatti' },
];

// Aggiunge al percorso la parte iniziale dell'indirizzo provvisorio
// (/lascatoladilatta). Con il dominio vero la parte iniziale sparisce da sola.
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
export const url = (percorso: string) => `${BASE}${percorso}`;
export const assoluto = (percorso: string) => new URL(url(percorso), import.meta.env.SITE).href;
