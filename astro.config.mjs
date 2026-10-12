import { defineConfig } from 'astro/config';

// Il sito è pubblicato su lascatoladilatta.it (GitHub Pages con dominio
// personalizzato: vedi public/CNAME).
export default defineConfig({
  site: 'https://lascatoladilatta.it',
  base: '/',
  trailingSlash: 'always',
  build: { format: 'directory' },
  // il sito è tutto statico: nessuna barra di sviluppo, nessuna telemetria nelle pagine
  devToolbar: { enabled: false },
});
