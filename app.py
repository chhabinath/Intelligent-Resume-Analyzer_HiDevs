from pathlib import Path

import streamlit as st


from utils.logger_utils import log_page_visit

log_page_visit("Home")


# --------------------------------------------------
# Initialize Required Folders
# --------------------------------------------------

REQUIRED_FOLDERS = [
    "jobs",
    "reports",
    "resumes",
]

for folder in REQUIRED_FOLDERS:
    Path(folder).mkdir(exist_ok=True)

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

st.sidebar.success("Select a page from the navigation menu.")

st.sidebar.markdown("---")

st.sidebar.subheader("Project Modules")

st.sidebar.markdown("""
- 📄 Single Resume Analysis
- 📂 Batch Resume Analysis
- 📑 Reports Dashboard
- ℹ️ About Project
""")

st.sidebar.markdown("---")

st.sidebar.caption("Milestone 12 - Analytics Dashboard")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📄 Intelligent Resume Analyzer")

st.subheader("AI-Powered Resume Screening & Candidate Matching System")

st.write("""
Welcome to the **Intelligent Resume Analyzer**.

This application automatically analyzes resumes against job
descriptions, evaluates candidate suitability, identifies
skill gaps, and generates professional reports.

Use the navigation menu on the left to explore each module.
""")

st.markdown("---")

# --------------------------------------------------
# Features
# --------------------------------------------------

st.header("🚀 Features")

left, right = st.columns(2)

with left:
    st.success("Resume Parsing")
    st.success("Candidate Validation")
    st.success("Skill Matching")
    st.success("Fuzzy Skill Matching")
    st.success("ATS-style Candidate Scoring")

with right:
    st.success("Batch Resume Processing")
    st.success("PDF Report Generation")
    st.success("Excel Summary Export")
    st.success("Analytics Dashboard")
    st.success("Interactive Charts")

st.markdown("---")

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.header("📋 Workflow")

st.markdown("""
1. Upload or select a resume

2. Select a job description

3. Parse resume information

4. Validate candidate profile

5. Match skills against job requirements

6. Generate ATS score

7. Produce TXT / PDF / Excel reports

8. Visualize analytics
""")

st.markdown("---")

# --------------------------------------------------
# Quick Navigation
# --------------------------------------------------

st.header("⚡ Quick Navigation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link(
        "pages/1_Single_Resume.py",
        label="Single Resume",
        icon="📄",
    )

with col2:
    st.page_link(
        "pages/2_Batch_Analysis.py",
        label="Batch Analysis",
        icon="📂",
    )

with col3:
    st.page_link(
        "pages/3_Reports.py",
        label="Reports",
        icon="📑",
    )

with col4:
    st.page_link(
        "pages/4_About.py",
        label="About",
        icon="ℹ️",
    )

st.markdown("---")

# --------------------------------------------------
# Dashboard Statistics
# --------------------------------------------------

jobs = len(list(Path("jobs").glob("*.json")))
reports = len(list(Path("reports").glob("*")))
resumes = len(list(Path("resumes").glob("*.txt")))

st.header("📊 Dashboard Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Job Profiles",
        jobs,
    )

with c2:
    st.metric(
        "Sample Resumes",
        resumes,
    )

with c3:
    st.metric(
        "Reports Generated",
        reports,
    )

with c4:
    st.metric(
        "Supported Format",
        "TXT",
    )

st.markdown("---")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------

st.header("📈 Project Overview")

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.metric(
        "Report Formats",
        "4",
        delta="TXT • PDF • Excel • Summary",
    )

with a2:
    st.metric(
        "Matching Engine",
        "RapidFuzz",
    )

with a3:
    st.metric(
        "Visualization",
        "Matplotlib",
    )

with a4:
    st.metric(
        "Framework",
        "Streamlit",
    )

st.markdown("---")

# --------------------------------------------------
# System Status
# --------------------------------------------------

st.header("🟢 System Status")

if jobs == 0:

    st.error("No job descriptions found. Add JSON files to the 'jobs' folder.")

elif resumes == 0:

    st.warning("No resumes found. Add TXT resumes to the 'resumes' folder.")

else:

    st.success("System is ready for resume analysis.")

st.markdown("---")

# --------------------------------------------------
# Project Components
# --------------------------------------------------

st.header("🧩 Project Components")

components = {
    "Resume Parser": "Ready",
    "Candidate Validator": "Ready",
    "Skill Matcher": "Ready",
    "Batch Processor": "Ready",
    "Report Generator": "Ready",
    "Analytics Dashboard": "Ready",
    "Charts": "Ready",
}

for component, status in components.items():
    st.write(f"✅ **{component}** — {status}")

st.markdown("---")

# --------------------------------------------------
# Project Directory Information
# --------------------------------------------------

with st.expander("📂 Project Directory Information"):

    st.code(f"""
Jobs Folder
{Path("jobs").resolve()}

Resumes Folder
{Path("resumes").resolve()}

Reports Folder
{Path("reports").resolve()}
""")

st.markdown("---")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption(
    "🚀 Intelligent Resume Analyzer | "
    "Built with Python, Streamlit, ReportLab, OpenPyXL, Matplotlib, and RapidFuzz."
)
