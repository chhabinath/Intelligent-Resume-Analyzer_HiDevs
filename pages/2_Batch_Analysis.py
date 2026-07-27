from pathlib import Path

import pandas as pd
import streamlit as st

from batch_processor import BatchProcessor
from utils.charts import (
    create_candidate_ranking,
    create_score_distribution,
)

from utils.logger_utils import (
    log_page_visit,
    log_success,
)

log_page_visit("Batch Analysis")

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Batch Resume Analysis",
    page_icon="📂",
    layout="wide",
)

st.title("📂 Batch Resume Analysis")

st.write("Analyze all resumes inside the resumes folder.")

st.markdown("---")

processor = BatchProcessor()

job_files = sorted([file.name for file in Path("jobs").glob("*.json")])

selected_job = st.selectbox(
    "Select Job Description",
    job_files,
)

st.markdown("---")

if st.button("Analyze All Resumes"):

    with st.spinner("Processing resumes..."):

        results = processor.process(
            "resumes",
            f"jobs/{selected_job}",
        )

    if not results:

        st.warning("No valid resumes found.")

        st.stop()

    st.success("Batch processing completed!")
    log_success(f"{len(results)} resumes processed.")

    st.markdown("---")

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    total = len(results)

    average = sum(item["score"] for item in results) / total

    highest = max(item["score"] for item in results)

    lowest = min(item["score"] for item in results)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Candidates", total)

    c2.metric("Average Score", f"{average:.2f}%")

    c3.metric("Highest", f"{highest:.2f}%")

    c4.metric("Lowest", f"{lowest:.2f}%")

    st.markdown("---")

    # ----------------------------------------
    # Ranking
    # ----------------------------------------

    st.subheader("🏆 Candidate Ranking")

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True,
    )

    ranking = []

    for index, result in enumerate(results, start=1):

        ranking.append(
            {
                "Rank": index,
                "Candidate": result["candidate"],
                "Score": result["score"],
                "Recommendation": result["recommendation"],
            }
        )

    dataframe = pd.DataFrame(ranking)

    st.dataframe(
        dataframe,
        use_container_width=True,
    )

    st.markdown("---")

    # ----------------------------------------
    # Charts
    # ----------------------------------------

    st.subheader("📊 Analytics")

    left, right = st.columns(2)

    with left:

        st.pyplot(create_candidate_ranking(results))

    with right:

        st.pyplot(create_score_distribution(results))

    st.markdown("---")

    # ----------------------------------------
    # Candidate Details
    # ----------------------------------------

    st.subheader("📄 Candidate Details")

    for result in results:

        with st.expander(result["candidate"]):

            st.write(f"Score : {result['score']:.2f}%")

            st.write(f"Recommendation : {result['recommendation']}")

            st.write("Matched Skills")

            st.success(", ".join(result["matched_skills"]))

            st.write("Missing Skills")

            st.error(", ".join(result["missing_skills"]))

    st.markdown("---")

    # ----------------------------------------
    # Downloads
    # ----------------------------------------

    st.subheader("📥 Reports")

    summary = Path("reports/summary.txt")

    if summary.exists():

        st.download_button(
            "Download Summary Report",
            summary.read_text(),
            file_name="summary.txt",
        )

    excel = Path("reports/summary.xlsx")

    if excel.exists():

        with open(excel, "rb") as file:

            st.download_button(
                "Download Excel Report",
                file,
                file_name="summary.xlsx",
            )
