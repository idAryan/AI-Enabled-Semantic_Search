from sentence_transformers import SentenceTransformer, util
from .data.nco_data import nco_data
model = SentenceTransformer('all-MiniLM-L6-v2')


# Precompute embeddings once
corpus = [f"{item['title']}. {item['description']}" for item in nco_data]
corpus_embeddings = model.encode(corpus, normalize_embeddings=True)

def get_similar_occupations(query, top_k=5):
    query_embedding = model.encode(query, normalize_embeddings=True)
    similarities = util.cos_sim(query_embedding, corpus_embeddings)[0]
    top_hits = similarities.topk(k=top_k)

    results = []
    for score, idx in zip(top_hits.values, top_hits.indices):
        item = nco_data[idx]
        results.append({
            "code": item["code"],
            "title": item["title"],
            "description": item["description"],
            "score": f"{(score.item() * 100):.2f}"
        })
    return results
