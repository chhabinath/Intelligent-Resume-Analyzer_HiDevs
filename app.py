import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Intelligent Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📄 Resume Analyzer")

st.sidebar.success(
    "Select a page above."
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project Modules**

    • Single Resume Analysis

    • Batch Resume Analysis

    • Reports Dashboard

    • About Project
    """
)

# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.title("📄 Intelligent Resume Analyzer")

st.subheader(
    "AI-Powered Resume Screening & Candidate Matching System"
)

st.write(
    """
Welcome to the **Intelligent Resume Analyzer**.

This application analyzes resumes against job descriptions,
calculates candidate-job match scores, identifies skill gaps,
and generates professional reports.

Use the navigation menu on the left to access different features.
"""
)

st.markdown("---")

# --------------------------------------------------
# Project Features
# --------------------------------------------------

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("Resume Parsing")

    st.success("Candidate Validation")

    st.success("Skill Matching")

    st.success("Fuzzy Skill Matching")

    st.success("Job Description Matching")

with col2:

    st.success("Batch Resume Processing")

    st.success("PDF Reports")

    st.success("Excel Summary")

    st.success("Analytics Dashboard")

    st.success("Interactive Charts")

st.markdown("---")

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.header("📋 Workflow")

st.markdown(
    """
1. Upload Resume

2. Select Job Description

3. Analyze Resume

4. View Match Score

5. Review Skill Gaps

6. Download Reports
"""
)

st.markdown("---")

# --------------------------------------------------
# Project Statistics
# --------------------------------------------------

st.header("📊 Project Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Supported Resume Formats",
        value="TXT",
    )

with col2:
    st.metric(
        label="Report Formats",
        value="4",
        delta="TXT • JSON • PDF • Excel",
    )

with col3:
    st.metric(
        label="Matching Engine",
        value="Fuzzy",
    )

with col4:
    st.metric(
        label="Framework",
        value="Streamlit",
    )

st.markdown("---")

# --------------------------------------------------
# Folder Status
# --------------------------------------------------

st.header("📁 Project Status")

jobs = len(list(Path("jobs").glob("*.json")))

reports = len(list(Path("reports").glob("*")))

resumes = len(list(Path("resumes").glob("*")))

c1, c2, c3 = st.columns(3)

with c1:
    st.info(f"Job Profiles\n\n{jobs}")

with c2:
    st.info(f"Reports Generated\n\n{reports}")

with c3:
    st.info(f"Sample Resumes\n\n{resumes}")

st.markdown("---")

st.caption(
    "Developed using Python, Streamlit, ReportLab, OpenPyXL and RapidFuzz."
)