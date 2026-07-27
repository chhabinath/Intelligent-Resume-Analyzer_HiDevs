import streamlit as st

from utils.logger_utils import log_page_visit

log_page_visit("About")


st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
)

st.title("ℹ️ About Intelligent Resume Analyzer")

st.markdown("""
The **Intelligent Resume Analyzer** is an AI-assisted resume screening
application that evaluates resumes against job descriptions and produces
detailed analysis reports.

It combines resume parsing, validation, skill matching, scoring,
analytics, and report generation into a single application.
""")

st.markdown("---")

# ----------------------------------------------------
# Features
# ----------------------------------------------------

st.header("🚀 Features")

features = [
    "Resume Parsing",
    "Candidate Validation",
    "Job Description Loading",
    "Skill Matching",
    "Resume Scoring",
    "Single Resume Analysis",
    "Batch Resume Analysis",
    "TXT Report Generation",
    "PDF Report Generation",
    "Excel Summary Export",
    "Analytics Dashboard",
    "Charts & Visualizations",
]

for feature in features:
    st.markdown(f"✅ {feature}")

st.markdown("---")

# ----------------------------------------------------
# Workflow
# ----------------------------------------------------

st.header("🔄 Workflow")

st.code(
    """
Resume
   │
   ▼
Resume Parser
   │
   ▼
Candidate Validator
   │
   ▼
Job Loader
   │
   ▼
Candidate Matcher
   │
   ▼
Report Generator
   │
   ▼
TXT / PDF / Excel Reports
   │
   ▼
Analytics Dashboard
""",
    language="text",
)

st.markdown("---")

# ----------------------------------------------------
# Project Structure
# ----------------------------------------------------

st.header("📁 Project Structure")

st.code(
    """
Intelligent-Resume-Analyzer_HiDevs/

app.py

pages/
    1_Single_Resume.py
    2_Batch_Analysis.py
    3_Reports.py
    4_About.py

utils/
    charts.py

parser.py
matcher.py
reporter.py
validator.py
batch_processor.py
excel_exporter.py
pdf_exporter.py
job_loader.py
skill_matcher.py
logger.py
exceptions.py
models.py

jobs/
reports/
resumes/
""",
    language="text",
)

st.markdown("---")

# ----------------------------------------------------
# Technology Stack
# ----------------------------------------------------

st.header("🛠 Technology Stack")

tech = {
    "Language": "Python 3.12",
    "Framework": "Streamlit",
    "Visualization": "Matplotlib",
    "Spreadsheet Export": "OpenPyXL",
    "PDF Export": "ReportLab",
    "Skill Matching": "RapidFuzz",
}

for key, value in tech.items():
    st.write(f"**{key}:** {value}")

st.markdown("---")

# ----------------------------------------------------
# Metrics
# ----------------------------------------------------

st.header("📊 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Pages", "4")
c2.metric("Core Modules", "10+")
c3.metric("Export Formats", "3")
c4.metric("Analytics", "4 Charts")

st.markdown("---")

# ----------------------------------------------------
# Future Enhancements
# ----------------------------------------------------

st.header("🔮 Future Enhancements")

future = [
    "Resume upload with drag-and-drop",
    "Support for PDF and DOCX resumes",
    "Interactive ATS score dashboard",
    "Candidate comparison",
    "Keyword heatmap",
    "Recruiter login",
    "Database integration",
    "REST API",
    "Cloud deployment",
]

for item in future:
    st.markdown(f"- {item}")

st.markdown("---")

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.success("Intelligent Resume Analyzer • Milestone 12 • Analytics Dashboard")
