from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def calculate_semantic_similarity(text1, text2):
    embeddings = model.encode(
        [text1, text2],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(embeddings[0], embeddings[1])

    score = similarity.item() * 100

    return round(score, 2)