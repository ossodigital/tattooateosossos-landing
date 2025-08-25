from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 16)
        self.cell(0, 10, "Códigos do Projeto Osso Digital", ln=True, align="C")
        self.ln(5)

    def add_code_section(self, title, content):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.set_font("DejaVu", "", 10)
        self.multi_cell(0, 5, content)
        self.ln(5)

# Criar PDF
pdf = PDF()
pdf.add_page()

# Adicionar suporte a UTF-8 com fonte DejaVu
pdf.add_font("DejaVu", "", "fonts/DejaVuSansMono.ttf", uni=True)

# Arquivos para incluir
files = {
    "index.html": "public/index.html",
    "style.css": "public/style.css",
    "main.js": "script/main.js"
}

# Adicionar conteúdo dos arquivos
for title, path in files.items():
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            pdf.add_code_section(title, f.read())
    else:
        pdf.add_code_section(title, f"Arquivo {path} não encontrado.")

# Salvar PDF
pdf.output("osso-digital-codigos.pdf")
print("✅ PDF gerado com sucesso!")

