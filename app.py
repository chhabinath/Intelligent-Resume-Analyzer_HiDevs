import os
from pathlib import Path

import streamlit as st

from file_manager import read_text_file
from job_loader import load_job
from matcher import CandidateMatcher
from parser import ResumeParser
from reporter import ReportGenerator
from validator import CandidateValidator

st.set_page_config(
    page_title="Intelligent Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Intelligent Resume Analyzer")

st.write(
    "Analyze resumes against job descriptions."
)

uploaded_resume = st.file_uploader(
    "Upload Resume (.txt)",
    type=["txt"],
)

job_files = [
    file
    for file in os.listdir("jobs")
    if file.endswith(".json")
]

selected_job = st.selectbox(
    "Select Job Description",
    job_files,
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    resume_text = uploaded_resume.read().decode("utf-8")

    candidate = ResumeParser(
        resume_text
    ).parse()

    CandidateValidator.validate(candidate)

    job = load_job(
        f"jobs/{selected_job}"
    )

    matcher = CandidateMatcher()

    result = matcher.match(
        candidate,
        job,
    )

    reporter = ReportGenerator()

    report = reporter.generate_report(
        candidate,
        job,
        result,
    )

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Candidate")

        st.write(
            f"**Name:** {candidate.name}"
        )

        st.write(
            f"**Email:** {candidate.email}"
        )

        st.write(
            f"**Experience:** {candidate.experience} years"
        )

        st.write(
            f"**Education:** {candidate.education}"
        )

    with col2:

        st.metric(
            "Match Score",
            f"{result.score}%"
        )

        st.write(
            f"**Recommendation:** {result.recommendation}"
        )

    st.subheader("Matched Skills")

    st.success(
        ", ".join(result.matched_skills)
    )

    st.subheader("Missing Skills")

    st.error(
        ", ".join(result.missing_skills)
    )

    st.download_button(
        "Download Report",
        report,
        file_name="resume_report.txt",
        mime="text/plain",
    )