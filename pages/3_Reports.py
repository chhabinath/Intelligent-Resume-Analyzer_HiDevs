from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Generated Reports")

st.write("View and download generated TXT, PDF, and Excel reports.")

st.markdown("---")

reports_dir = Path("reports")

if not reports_dir.exists():
    st.warning("Reports folder does not exist.")
    st.stop()

txt_reports = sorted(reports_dir.glob("*.txt"))
pdf_reports = sorted(reports_dir.glob("*.pdf"))
excel_reports = sorted(reports_dir.glob("*.xlsx"))

c1, c2, c3 = st.columns(3)

c1.metric("TXT Reports", len(txt_reports))
c2.metric("PDF Reports", len(pdf_reports))
c3.metric("Excel Reports", len(excel_reports))

st.markdown("---")

# -------------------------------
# Text Reports
# -------------------------------

st.header("📝 Text Reports")

if txt_reports:

    selected = st.selectbox(
        "Select a report",
        txt_reports,
        format_func=lambda p: p.name,
    )

    text = selected.read_text(encoding="utf-8")

    st.subheader("Preview")

    st.text_area(
        "",
        value=text,
        height=400,
    )

    st.download_button(
        "⬇ Download TXT",
        data=text,
        file_name=selected.name,
        mime="text/plain",
    )

else:
    st.info("No text reports available.")

st.markdown("---")

# -------------------------------
# PDF Reports
# -------------------------------

st.header("📕 PDF Reports")

if pdf_reports:

    for pdf in pdf_reports:

        with open(pdf, "rb") as f:

            st.download_button(
                label=f"⬇ {pdf.name}",
                data=f.read(),
                file_name=pdf.name,
                mime="application/pdf",
            )

else:
    st.info("No PDF reports available.")

st.markdown("---")

# -------------------------------
# Excel Reports
# -------------------------------

st.header("📗 Excel Reports")

if excel_reports:

    for excel in excel_reports:

        with open(excel, "rb") as f:

            st.download_button(
                label=f"⬇ {excel.name}",
                data=f.read(),
                file_name=excel.name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

else:
    st.info("No Excel reports available.")