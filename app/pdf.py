from config import PDFConfig

def create_pdf_with_unicode(text, output_path):
    """Create PDF with Unicode. support"""
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()

    # Добавление шрифта с поддержкой Unicode
    font_path = PDFConfig.FONT_PATH
    pdf.add_font("FreeSans", "", font_path, uni=True)
    pdf.set_font("FreeSans", size=12)

    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)