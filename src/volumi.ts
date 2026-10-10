import { getCollection } from 'astro:content';

// Tutti i volumi, nell'ordine indicato dal campo "ordine".
export async function volumiInOrdine() {
  const volumi = await getCollection('volumi');
  return volumi.sort((a, b) => a.data.ordine - b.data.ordine);
}
