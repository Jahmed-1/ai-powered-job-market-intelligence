import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px

from candidate_matcher.matcher import analyze_candidate_match
from candidate_matcher.file_reader import read_uploaded_file


st.set_page_config(
    page_title="AI-Powered Job Market Intelligence",
    layout="wide"
)


st.title("AI-Powered Job Market Intelligence System")

st.write(
    "This dashboard analyzes German job postings, shows demanded skills and job roles, "
    "and also checks how well a CV and cover letter match a job description."
)


jobs_df = pd.read_csv("data/filtered_jobs.csv")
skills_df = pd.read_csv("data/top_skills.csv")
roles_df = pd.read_csv("data/top_roles.csv")


st.subheader("Project Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Relevant Jobs", len(jobs_df))
col2.metric("Top Skills Found", len(skills_df))
col3.metric("Job Role Categories", len(roles_df))


st.subheader("Top Demanded Skills")

fig_skills = px.bar(
    skills_df,
    x="skill",
    y="count",
    title="Most Demanded Skills"
)

st.plotly_chart(fig_skills, use_container_width=True)


st.subheader("Top Job Roles")

fig_roles = px.bar(
    roles_df,
    x="role",
    y="count",
    title="Most Common Job Roles"
)

st.plotly_chart(fig_roles, use_container_width=True)


st.subheader("Filtered Job Postings")

st.dataframe(
    jobs_df[["title", "company", "location", "predicted_role", "extracted_skills"]],
    use_container_width=True
)


st.divider()


st.subheader("CV + Cover Letter Match Analyzer")

st.write("You can either upload files or paste text manually.")

job_description_file = st.file_uploader(
    "Upload Job Description file",
    type=["pdf", "docx", "txt"]
)

cv_file = st.file_uploader(
    "Upload CV / Resume file",
    type=["pdf", "docx", "txt"]
)

cover_letter_file = st.file_uploader(
    "Upload Cover Letter file",
    type=["pdf", "docx", "txt"]
)

job_description_input = st.text_area(
    "Or paste Job Description",
    height=150
)

cv_input = st.text_area(
    "Or paste CV / Resume Text",
    height=150
)

cover_letter_input = st.text_area(
    "Or paste Cover Letter",
    height=150
)


job_description_text = (
    read_uploaded_file(job_description_file)
    if job_description_file
    else job_description_input
)

cv_text = (
    read_uploaded_file(cv_file)
    if cv_file
    else cv_input
)

cover_letter_text = (
    read_uploaded_file(cover_letter_file)
    if cover_letter_file
    else cover_letter_input
)


if st.button("Analyze Candidate Match"):
    if job_description_text and cv_text and cover_letter_text:
        result = analyze_candidate_match(
            job_description_text,
            cv_text,
            cover_letter_text
        )

        st.subheader("Candidate Match Result")

        score_col1, score_col2, score_col3 = st.columns(3)

        score_col1.metric("Overall Match Score", f"{result['overall_score']}%")
        score_col2.metric("CV Match Score", f"{result['cv_match_score']}%")
        score_col3.metric("Cover Letter Match Score", f"{result['cover_letter_match_score']}%")

        st.subheader("Score Breakdown")

        detail_col1, detail_col2, detail_col3 = st.columns(3)

        detail_col1.metric("CV TF-IDF Score", f"{result['cv_tfidf_score']}%")
        detail_col2.metric("CV Semantic Score", f"{result['cv_semantic_score']}%")
        detail_col3.metric("Skill Match Score", f"{result['skill_match_score']}%")

        detail_col4, detail_col5 = st.columns(2)

        detail_col4.metric(
            "Cover Letter TF-IDF Score",
            f"{result['cover_letter_tfidf_score']}%"
        )

        detail_col5.metric(
            "Cover Letter Semantic Score",
            f"{result['cover_letter_semantic_score']}%"
        )

        st.write("### Job Required Skills")
        st.write(result["job_required_skills"])

        st.write("### CV Skills")
        st.write(result["cv_skills"])

        st.write("### Cover Letter Skills")
        st.write(result["cover_letter_skills"])

        st.write("### Matched Skills")
        st.write(result["matched_skills"])

        st.write("### Missing Skills")
        st.write(result["missing_skills"])

    else:
        st.warning("Please provide Job Description, CV, and Cover Letter by upload or paste.")