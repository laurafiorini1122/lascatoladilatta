// robots.txt: tutto il sito è aperto ai motori di ricerca e la sitemap è
// indicata con l'indirizzo completo.
import type { APIRoute } from 'astro';
import { assoluto } from '../sito';

export const GET: APIRoute = () =>
  new Response(`User-agent: *\nAllow: /\n\nSitemap: ${assoluto('/sitemap.xml')}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
