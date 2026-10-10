// Schema dei volumi: ogni file in src/content/volumi/ descrive un quaderno.
// Se manca un campo o un testo supera la lunghezza consentita, la costruzione
// del sito si ferma con un errore che dice quale file e quale campo correggere.
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const immagine = z.object({
  // percorso dentro la cartella materiali, usato solo dallo script delle immagini
  sorgente: z.string(),
  alt: z.string().min(10),
});

const volumi = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/volumi' }),
  schema: z.object({
    titolo: z.string(),
    ordine: z.number().int(),
    sottotitolo: z.string(),
    seo: z.object({
      titolo: z.string().max(60),
      descrizione: z.string().max(155),
    }),
    retro: z.array(z.string()).min(1),
    giochi: z.array(z.string()).length(15),
    // vuoto finché il libro non è pubblicato: la pagina dice "Presto su Amazon"
    amazon: z.union([z.literal(''), z.url()]),
    immagini: z.object({
      copertina: immagine,
      disegno: immagine.extend({ didascalia: z.string() }),
    }),
  }),
});

export const collections = { volumi };
