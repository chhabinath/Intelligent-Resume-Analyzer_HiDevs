from pathlib import Path
import json

import pandas as pd
import streamlit as st

from candidate_repository import CandidateRepository

from utils.logger_utils import (
    log_page_visit,
    log_error,
)

log_page_visit("Candidate Database")

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Candidate Database",
    page_icon="🗄️",
    layout="wide",
)

st.title("🗄️ Candidate Database")

repo = CandidateRepository()

try:

    # -------------------------------------------------
    # Dashboard Metrics
    # -------------------------------------------------

    stats = repo.get_statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Candidates",
        stats["total"] or 0,
    )

    col2.metric(
        "Average Score",
        f'{(stats["average_score"] or 0):.2f}%',
    )

    col3.metric(
        "Highest Score",
        f'{(stats["highest_score"] or 0):.2f}%',
    )

    col4.metric(
        "Lowest Score",
        f'{(stats["lowest_score"] or 0):.2f}%',
    )

    st.markdown("---")

    # -------------------------------------------------
    # Search & Filters
    # -------------------------------------------------

    st.subheader("🔎 Search & Filter")

    left, right = st.columns(2)

    with left:

        keyword = st.text_input(
            "Search",
            placeholder="Name, Email or Skill",
        )

        recommendation = st.selectbox(
            "Recommendation",
            [
                "All",
                "Strongly Recommend",
                "Recommend",
                "Consider",
                "Reject",
            ],
        )

    with right:

        min_score = st.slider(
            "Minimum Score",
            0,
            100,
            0,
        )

        min_experience = st.slider(
            "Minimum Experience",
            0,
            30,
            0,
        )

    sort_by = st.selectbox(
        "Sort By",
        [
            "score",
            "experience",
            "name",
            "created_at",
        ],
    )

    candidates = repo.filter_candidates(
        keyword=keyword,
        recommendation=recommendation,
        min_score=min_score,
        min_experience=min_experience,
        sort_by=sort_by,
    )

    st.markdown("---")

    # -------------------------------------------------
    # Candidate Table
    # -------------------------------------------------

    if not candidates:

        st.info("No candidates found.")

    else:

        df = pd.DataFrame(candidates)

        display_df = df[
            [
                "id",
                "name",
                "email",
                "experience",
                "score",
                "recommendation",
                "created_at",
            ]
        ]

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

        # -------------------------------------------------
        # CSV Export
        # -------------------------------------------------

        csv = display_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Export Filtered Results",
            data=csv,
            file_name="filtered_candidates.csv",
            mime="text/csv",
        )

        st.markdown("---")

        # -------------------------------------------------
        # Candidate Details
        # -------------------------------------------------

        st.subheader("👤 Candidate Details")

        names = [
            f'{c["id"]} - {c["name"]}'
            for c in candidates
        ]

        selected = st.selectbox(
            "Select Candidate",
            names,
        )

        candidate_id = int(
            selected.split("-")[0].strip()
        )

        candidate = repo.get_candidate(
            candidate_id
        )

        left, right = st.columns(2)

        with left:

            st.write(
                f"**Name:** {candidate['name']}"
            )

            st.write(
                f"**Email:** {candidate['email']}"
            )

            st.write(
                f"**Phone:** {candidate['phone']}"
            )

            st.write(
                f"**Experience:** {candidate['experience']} Years"
            )

        with right:

            st.write(
                f"**Score:** {candidate['score']:.2f}%"
            )

            st.write(
                f"**Recommendation:** {candidate['recommendation']}"
            )

            st.write(
                f"**Created:** {candidate['created_at']}"
            )

        st.markdown("---")

        # -------------------------------------------------
        # Report
        # -------------------------------------------------

        st.subheader("📄 Report")

        report_path = candidate["report_path"]

        st.write(report_path)

        if report_path and Path(report_path).exists():

            with open(report_path, "rb") as report_file:

                st.download_button(
                    "⬇ Download Report",
                    data=report_file,
                    file_name=Path(report_path).name,
                    mime="text/plain",
                )

        else:

            st.warning(
                "Report file not found."
            )

        st.markdown("---")

        # -------------------------------------------------
        # Skills
        # -------------------------------------------------

        left, right = st.columns(2)

        matched = candidate["matched_skills"]
        missing = candidate["missing_skills"]

        try:

            matched = json.loads(
                matched
            ) if matched else []

        except Exception:

            matched = []

        try:

            missing = json.loads(
                missing
            ) if missing else []

        except Exception:

            missing = []

        with left:

            st.subheader(
                "✅ Matched Skills"
            )

            if matched:

                for skill in matched:

                    st.success(skill)

            else:

                st.info(
                    "No matched skills."
                )

        with right:

            st.subheader(
                "❌ Missing Skills"
            )

            if missing:

                for skill in missing:

                    st.error(skill)

            else:

                st.success(
                    "No missing skills."
                )

        st.markdown("---")

        # -------------------------------------------------
        # Delete Candidate
        # -------------------------------------------------

        if st.button(
            "🗑 Delete Candidate",
            type="primary",
        ):

            repo.delete_candidate(
                candidate_id
            )

            st.success(
                "Candidate deleted successfully."
            )

            st.rerun()

except Exception as error:

    log_error(str(error))

    st.error(
        "Unable to load candidate database."
    )

    st.caption(str(error))

finally:

    repo.close()