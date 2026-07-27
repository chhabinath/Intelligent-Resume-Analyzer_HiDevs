from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font


class ExcelExporter:
    """
    Export batch resume analysis summary to an Excel workbook.
    """

    def export_summary(
        self,
        results: list[dict],
        output_file: str,
    ) -> None:

        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Resume Summary"

        headers = [
            "Candidate",
            "Score",
            "Recommendation",
            "Matched Skills",
            "Missing Skills",
        ]

        worksheet.append(headers)

        # Make headers bold
        for cell in worksheet[1]:
            cell.font = Font(bold=True)

        # Add candidate rows
        for result in sorted(
            results,
            key=lambda x: x["score"],
            reverse=True,
        ):
            worksheet.append([
                result["name"],
                result["score"],
                result["recommendation"],
                ", ".join(result["matched_skills"]),
                ", ".join(result["missing_skills"]),
            ])

        # Auto-fit column widths
        for column_cells in worksheet.columns:
            length = max(
                len(str(cell.value or ""))
                for cell in column_cells
            )
            worksheet.column_dimensions[
                column_cells[0].column_letter
            ].width = length + 2

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        workbook.save(output_file)