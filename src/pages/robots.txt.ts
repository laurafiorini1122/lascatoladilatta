// robots.txt: tutto il sito è aperto ai motori di ricerca.
// Nota: con l'indirizzo provvisorio (…github.io/lascatoladilatta/) i motori
// leggono solo il robots.txt alla radice del dominio, quindi questo file
// conta davvero quando colleghiamo lascatoladilatta.it.
import type { APIRoute } from 'astro';
import { assoluto } from '../sito';

export const GET: APIRoute = () =>
  new Response(`User-agent: *\nAllow: /\n\nSitemap: ${assoluto('/sitemap.xml')}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
