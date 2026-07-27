import os
from pathlib import Path

import streamlit as st

from parser import ResumeParser
from validator import CandidateValidator
from job_loader import load_job
from matcher import CandidateMatcher
from reporter import ReportGenerator
from exceptions import ValidationError

import matplotlib.pyplot as plt

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

job_files = sorted(
    [
        file
        for file in os.listdir("jobs")
        if file.endswith(".json")
    ]
)

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

        resume_text = uploaded_file.read().decode("utf-8")

        parser = ResumeParser(resume_text)

        candidate = parser.parse()

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

        # ---------------------------------------------
        # Success Message
        # ---------------------------------------------

        st.success("Resume analyzed successfully!")

        log_success("Single resume analyzed successfully.")

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
            label="Overall Score",
            value=f"{result.score:.2f}%",
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

        # ---------------------------------------------
        # Report
        # ---------------------------------------------

        st.subheader("📄 Generated Report")

        st.text_area(
            "Preview",
            report,
            height=300,
        )

        st.download_button(
            label="⬇ Download TXT Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain",
        )
        log_success("Single resume analyzed successfully.")

    except ValidationError as error:
        log_error(str(error))
        st.error(f"Validation Error: {error}")

    except Exception as error:
        log_error(str(error))
        st.exception(error)