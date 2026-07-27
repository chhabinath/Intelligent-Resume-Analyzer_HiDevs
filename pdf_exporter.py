from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class PDFExporter:
    """
    Export candidate analysis report to PDF.
    """

    def export_report(
        self,
        candidate,
        job,
        match_result,
        output_file: str,
    ) -> None:

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document = SimpleDocTemplate(output_file)
        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph("Resume Analysis Report", styles["Title"])
        )
        elements.append(Spacer(1, 12))

        elements.append(
            Paragraph(
                f"<b>Candidate:</b> {candidate.name}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Email:</b> {candidate.email}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Experience:</b> {candidate.experience} years",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Education:</b> {candidate.education}",
                styles["BodyText"],
            )
        )

        elements.append(Spacer(1, 12))

        elements.append(
            Paragraph(
                f"<b>Job Role:</b> {job.title}",
                styles["Heading2"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Match Score:</b> {match_result.score}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Recommendation:</b> {match_result.recommendation}",
                styles["BodyText"],
            )
        )

        elements.append(Spacer(1, 12))

        elements.append(
            Paragraph(
                "<b>Matched Skills</b>",
                styles["Heading2"],
            )
        )

        for skill in match_result.matched_skills:
            elements.append(
                Paragraph(f"• {skill}", styles["BodyText"])
            )

        elements.append(Spacer(1, 12))

        elements.append(
            Paragraph(
                "<b>Missing Skills</b>",
                styles["Heading2"],
            )
        )

        for skill in match_result.missing_skills:
            elements.append(
                Paragraph(f"• {skill}", styles["BodyText"])
            )

        document.build(elements)