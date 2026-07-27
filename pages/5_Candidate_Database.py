import streamlit as st
import pandas as pd

from candidate_repository import CandidateRepository

from utils.logger_utils import (
    log_page_visit,
    log_error,
)

log_page_visit("Candidate Database")

st.set_page_config(
    page_title="Candidate Database",
    page_icon="🗄️",
    layout="wide",
)

st.title("🗄️ Candidate Database")

repo = CandidateRepository()

try:

    stats = repo.get_statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Candidates",
        stats["total"] or 0
    )

    col2.metric(
        "Average Score",
        f'{(stats["average_score"] or 0):.2f}%'
    )

    col3.metric(
        "Highest Score",
        f'{(stats["highest_score"] or 0):.2f}%'
    )

    col4.metric(
        "Lowest Score",
        f'{(stats["lowest_score"] or 0):.2f}%'
    )

    st.markdown("---")

    keyword = st.text_input(
        "🔍 Search Candidate"
    )

    if keyword:

        candidates = repo.search_candidates(keyword)

    else:

        candidates = repo.get_all_candidates()

    if not candidates:

        st.info("No candidates found.")

    else:

        df = pd.DataFrame(candidates)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        st.markdown("---")

        st.subheader("Candidate Details")

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

        candidate = repo.get_candidate(candidate_id)

        left, right = st.columns(2)

        with left:

            st.write(f"**Name:** {candidate['name']}")
            st.write(f"**Email:** {candidate['email']}")
            st.write(f"**Phone:** {candidate['phone']}")
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
                f"**Report:** {candidate['report_path']}"
            )

            st.write(
                f"**Created:** {candidate['created_at']}"
            )

        st.markdown("---")

        if st.button(
            "🗑 Delete Candidate",
            type="primary",
        ):

            repo.delete_candidate(candidate_id)

            st.success("Candidate deleted.")

            st.rerun()

finally:

    repo.close()