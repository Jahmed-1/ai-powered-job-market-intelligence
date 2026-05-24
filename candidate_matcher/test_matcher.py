from candidate_matcher.matcher import analyze_candidate_match


job_description = """
We are looking for a Data Analyst with strong SQL, Python, Excel, and Power BI skills.
The candidate should have experience in data cleaning, dashboards, reporting, and business analysis.
AWS knowledge is a plus.
"""

cv_text = """
I have experience in Python, SQL, Excel, and data analysis.
I built dashboards and worked on reporting projects using Power BI.
I also have basic knowledge of machine learning.
"""

cover_letter_text = """
I am interested in this Data Analyst role because I enjoy working with data,
creating dashboards, and using Python and SQL to solve business problems.
"""


result = analyze_candidate_match(job_description, cv_text, cover_letter_text)

print("Overall Score:", result["overall_score"])
print("CV Match Score:", result["cv_match_score"])
print("Cover Letter Match Score:", result["cover_letter_match_score"])

print("CV TF-IDF Score:", result["cv_tfidf_score"])
print("Cover Letter TF-IDF Score:", result["cover_letter_tfidf_score"])

print("CV Semantic Score:", result["cv_semantic_score"])
print("Cover Letter Semantic Score:", result["cover_letter_semantic_score"])

print("Skill Match Score:", result["skill_match_score"])

print("Job Required Skills:", result["job_required_skills"])
print("CV Skills:", result["cv_skills"])
print("Cover Letter Skills:", result["cover_letter_skills"])
print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])