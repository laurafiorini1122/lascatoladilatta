// Sitemap per i motori di ricerca: si aggiorna da sola quando si aggiunge un volume.
import type { APIRoute } from 'astro';
import { volumiInOrdine } from '../volumi';
import { assoluto } from '../sito';

const PAGINE_FISSE = ['/', '/quaderni/', '/prova/', '/contatti/', '/note-legali/'];

export const GET: APIRoute = async () => {
  const volumi = await volumiInOrdine();
  const percorsi = [...PAGINE_FISSE, ...volumi.map((v) => `/quaderni/${v.id}/`)];
  const voci = percorsi.map((p) => `  <url><loc>${assoluto(p)}</loc></url>`).join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${voci}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
