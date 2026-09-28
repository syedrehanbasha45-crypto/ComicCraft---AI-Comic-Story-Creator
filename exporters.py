import os, time
from fpdf import FPDF

def save_pdf(layout):
    os.makedirs("app/static/exports", exist_ok=True)
    filename = f"comic_{int(time.time())}.pdf"
    path = os.path.join("app/static/exports", filename)

    pdf = FPDF()
    for panel in layout:
        pdf.add_page()
        pdf.set_font("Arial", "B", 18)
        pdf.cell(0, 12, f"Panel {panel['panel_number']}: {panel['title']}", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, panel["scene_description"])
        img = panel["image_path"].lstrip("/")
        if os.path.exists(img):
            pdf.image(img, x=15, y=55, w=180)
        pdf.set_y(170)
        pdf.multi_cell(0, 7, panel["text"])
    pdf.output(path)
    return "/static/exports/" + filename
