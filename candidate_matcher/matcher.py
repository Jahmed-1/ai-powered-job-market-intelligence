from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from candidate_matcher.semantic_matcher import calculate_semantic_similarity
from preprocessing.text_cleaner import clean_text
from skill_extractor.extractor import extract_skills
from candidate_matcher.language_normalizer import normalize_german_english_terms


def calculate_similarity(text1, text2):
    documents = [text1, text2]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)


def analyze_candidate_match(job_description, cv_text, cover_letter_text):
    job_description = clean_text(job_description)
    cv_text = clean_text(cv_text)
    cover_letter_text = clean_text(cover_letter_text)

    job_description = normalize_german_english_terms(job_description)

    jd_skills = extract_skills(job_description)
    cv_skills = extract_skills(cv_text)
    cover_letter_skills = extract_skills(cover_letter_text)
    job_description = normalize_german_english_terms(job_description)
    cv_text = normalize_german_english_terms(cv_text)
    cover_letter_text = normalize_german_english_terms(cover_letter_text)
    matched_skills = list(set(jd_skills) & set(cv_skills))
    missing_skills = list(set(jd_skills) - set(cv_skills))

    cv_tfidf_score = calculate_similarity(job_description, cv_text)
    cover_letter_tfidf_score = calculate_similarity(job_description, cover_letter_text)

    cv_semantic_score = calculate_semantic_similarity(job_description, cv_text)
    cover_letter_semantic_score = calculate_semantic_similarity(job_description, cover_letter_text)

    if len(jd_skills) > 0:
        skill_match_score = round((len(matched_skills) / len(jd_skills)) * 100, 2)
    else:
        skill_match_score = 0

    cv_match_score = round(
        (cv_semantic_score * 0.5) +
        (skill_match_score * 0.3) +
        (cv_tfidf_score * 0.2),
        2
    )

    cover_letter_match_score = round(
        (cover_letter_semantic_score * 0.6) +
        (cover_letter_tfidf_score * 0.4),
        2
    )

    overall_score = round(
        (cv_match_score * 0.7) +
        (cover_letter_match_score * 0.3),
        2
    )

    result = {
        "overall_score": overall_score,
        "cv_match_score": cv_match_score,
        "cover_letter_match_score": cover_letter_match_score,
        "cv_tfidf_score": cv_tfidf_score,
        "cover_letter_tfidf_score": cover_letter_tfidf_score,
        "cv_semantic_score": cv_semantic_score,
        "cover_letter_semantic_score": cover_letter_semantic_score,
        "skill_match_score": skill_match_score,
        "job_required_skills": jd_skills,
        "cv_skills": cv_skills,
        "cover_letter_skills": cover_letter_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    return result

    