from pathlib import Path
from typing import Any


class PDFTools:
    async def create_pdf(self, content: str, output_path: str = "output.pdf", **kwargs: Any) -> str:
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas

            p = Path(output_path).expanduser().resolve()
            p.parent.mkdir(parents=True, exist_ok=True)
            c = canvas.Canvas(str(p), pagesize=letter)
            y = 750
            for line in content.split("\n"):
                c.drawString(50, y, line[:80])
                y -= 15
                if y < 50:
                    c.showPage()
                    y = 750
            c.save()
            return f"✓ PDF created: {p}"
        except Exception as e:
            return f"✗ Failed to create PDF: {e}"
