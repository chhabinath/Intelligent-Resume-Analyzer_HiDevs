import os
from pathlib import Path

import streamlit as st

from parser import ResumeParser
from validator import CandidateValidator
from job_loader import load_job
from matcher import CandidateMatcher
from reporter import ReportGenerator
from exceptions import ValidationError

from candidate_repository import CandidateRepository

from utils.charts import (
    create_skill_pie,
    create_skill_bar,
)

from utils.logger_utils import (
    log_page_visit,
    log_success,
    log_error,
)

log_page_visit("Single Resume")

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Single Resume Analysis",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Single Resume Analysis")

st.write(
    "Upload one resume and compare it with a selected job description."
)

st.markdown("---")

# -------------------------------------------------
# Upload Resume
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (.txt)",
    type=["txt"],
)

# -------------------------------------------------
# Job Selection
# -------------------------------------------------

jobs_dir = Path("jobs")
jobs_dir.mkdir(exist_ok=True)

job_files = sorted(
    [
        file
        for file in os.listdir(jobs_dir)
        if file.endswith(".json")
    ]
)

if not job_files:
    st.warning("No job description files found in the 'jobs' folder.")
    st.stop()

selected_job = st.selectbox(
    "Select Job Description",
    job_files,
)

st.markdown("---")

# -------------------------------------------------
# Analyze Button
# -------------------------------------------------

if st.button("Analyze Resume"):

    if uploaded_file is None:

        st.warning("Please upload a resume.")
        st.stop()

    try:

        # ---------------------------------------------
        # Parse Resume
        # ---------------------------------------------

        resume_text = uploaded_file.read().decode("utf-8")

        parser = ResumeParser(resume_text)

        candidate = parser.parse()

        CandidateValidator.validate(candidate)

        # ---------------------------------------------
        # Load Job Description
        # ---------------------------------------------

        job = load_job(
            str(jobs_dir / selected_job)
        )

        # ---------------------------------------------
        # Match Resume
        # ---------------------------------------------

        matcher = CandidateMatcher()

        result = matcher.match(
            candidate,
            job,
        )

        # ---------------------------------------------
        # Generate Report
        # ---------------------------------------------

        reporter = ReportGenerator()

        report = reporter.generate_report(
            candidate,
            job,
            result,
        )

        # ---------------------------------------------
        # Save Report
        # ---------------------------------------------

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        safe_name = candidate.name.replace(" ", "_")

        report_path = reports_dir / f"{safe_name}_report.txt"

        reporter.save_text_report(
            report,
            str(report_path),
        )

        # ---------------------------------------------
        # Save Candidate to Database
        # ---------------------------------------------

        repository = CandidateRepository()

        try:

            repository.add_candidate(
                candidate,
                result,
                str(report_path),
            )

        finally:

            repository.close()

        # ---------------------------------------------
        # Success Message
        # ---------------------------------------------

        st.success("Resume analyzed successfully!")

        log_success(
            f"Resume analyzed successfully: {candidate.name}"
        )

        st.markdown("---")

        # ---------------------------------------------
        # Candidate Information
        # ---------------------------------------------

        st.subheader("👤 Candidate Information")

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"""
**Name**

{candidate.name}

**Email**

{candidate.email}
"""
            )

        with col2:

            st.info(
                f"""
**Experience**

{candidate.experience} Years

**Education**

{candidate.education}
"""
            )

        st.markdown("---")

        # ---------------------------------------------
        # Match Score
        # ---------------------------------------------

        st.subheader("📊 Match Score")

        st.metric(
            "Overall Score",
            f"{result.score:.2f}%",
        )

        st.progress(result.score / 100)

        st.markdown("---")

        # ---------------------------------------------
        # Recommendation
        # ---------------------------------------------

        st.subheader("💡 Recommendation")

        recommendation = result.recommendation.lower()

        if "strong" in recommendation:

            st.success(result.recommendation)

        elif "recommend" in recommendation:

            st.warning(result.recommendation)

        else:

            st.error(result.recommendation)

        st.markdown("---")

        # ---------------------------------------------
        # Skills
        # ---------------------------------------------

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matched Skills")

            if result.matched_skills:

                for skill in result.matched_skills:
                    st.success(skill)

            else:

                st.info("No matched skills.")

        with right:

            st.subheader("❌ Missing Skills")

            if result.missing_skills:

                for skill in result.missing_skills:
                    st.error(skill)

            else:

                st.success("No missing skills.")

        st.markdown("---")

        # ---------------------------------------------
        # Charts
        # ---------------------------------------------

        st.subheader("📊 Skill Match Visualization")

        col1, col2 = st.columns(2)

        with col1:

            st.pyplot(
                create_skill_pie(
                    result.matched_skills,
                    result.missing_skills,
                )
            )

        with col2:

            st.pyplot(
                create_skill_bar(
                    result.matched_skills,
                    result.missing_skills,
                )
            )

        st.markdown("---")

        # ---------------------------------------------
        # Report Preview
        # ---------------------------------------------

        st.subheader("📄 Generated Report")

        st.text_area(
            "Preview",
            value=report,
            height=300,
        )

        st.download_button(
            label="⬇ Download TXT Report",
            data=report,
            file_name=report_path.name,
            mime="text/plain",
        )

    except ValidationError as error:

        log_error(str(error))

        st.error(f"Validation Error: {error}")

    except Exception as error:

        log_error(str(error))

        st.error(
            "An unexpected error occurred while analyzing the resume."
        )

        st.caption(str(error))