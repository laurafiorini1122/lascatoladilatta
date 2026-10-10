import { defineConfig } from 'astro/config';

// Indirizzo provvisorio di GitHub Pages. Quando colleghiamo lascatoladilatta.it
// queste due righe diventano:
//   site: 'https://lascatoladilatta.it',
//   base: '/',
export default defineConfig({
  site: 'https://laurafiorini1122.github.io',
  base: '/lascatoladilatta',
  trailingSlash: 'always',
  build: { format: 'directory' },
  // il sito è tutto statico: nessuna barra di sviluppo, nessuna telemetria nelle pagine
  devToolbar: { enabled: false },
});
