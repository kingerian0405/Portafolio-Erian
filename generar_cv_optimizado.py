import subprocess
import sys
import os

# ── Instalación automática de dependencias ──────────────────────────────────
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

try:
    from reportlab.lib.pagesizes import A4
except ImportError:
    print("Instalando reportlab...")
    install("reportlab")

# ── Imports principales ─────────────────────────────────────────────────────
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.platypus.flowables import Flowable

# ── Colores del diseño ───────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1a2a3a")
ACCENT_BLUE = colors.HexColor("#2980b9")
LIGHT_BLUE  = colors.HexColor("#3498db")
GRAY_TEXT   = colors.HexColor("#7f8c8d")
LIGHT_GRAY  = colors.HexColor("#bdc3c7")
BG_GRAY     = colors.HexColor("#ffffff")
WHITE       = colors.white

# ── Datos del curriculum ─────────────────────────────────────────────────────
NOMBRE      = "Erian Arrieche"
UBICACION   = "Barquisimeto, Venezuela (Remote Friendly / Disponibilidad inmediata)"
TELEFONO    = "+58-4120371426"
EMAIL       = "Kingerian0405@gmail.com"
PORTAFOLIO  = "https://6a3c6307faad110eda9abf58--chipper-chebakia-514042.netlify.app"

RESUMEN = (
    "<b>Senior Tech Lead | Especialista en Arquitectura & Evolución de Sistemas</b><br/>"
    "Especialista en la <b>supervivencia y transformación de sistemas críticos</b>. Con más de 7 años de trayectoria, he liderado la modernización de arquitecturas legacy hacia ecosistemas modernos en Node.js y Laravel, reduciendo la deuda técnica y garantizando alta disponibilidad (99.9%) en sectores gubernamentales y de movilidad inteligente. Mi enfoque une la excelencia técnica con la <b>rentabilidad del negocio</b>."
)

HABILIDADES = [
    "<b>Languages:</b> PHP 8.x (Expert), TypeScript, JavaScript, SQL, Python",
    "<b>Frameworks:</b> Laravel, Node.js (Express/NestJS), Angular, Next.js, Vue.js",
    "<b>Arquitectura:</b> Modular Monolith, Microservices, SOLID, Clean Arch",
    "<b>Databases:</b> PostgreSQL, MongoDB, MySQL, SQLite, Redis",
    "<b>DevOps:</b> Docker, AWS (S3/EC2), CI/CD (Bitbucket), Nginx",
    "<b>Product Thinking:</b> Agile/Scrum, Prototipado, UX/UI Glassmorphism",
]

IDIOMAS = [
    ("Castellano", "Nativo"),
    ("Inglés", "Técnico Avanzado (Lectura/Documentación/Arquitectura)"),
]

CERTIFICADOS = [
    "Ingeniería en Informática (Título Profesional)",
    "Arquitectura de Software y Sistemas Escalables",
    "Modernización de Aplicaciones Legacy",
]

EXPERIENCIA = [
    {
        "titulo":   "Lead Architect | Product Owner · SisPRES (ERP)",
        "empresa":  "Sistema de Gestión Financiera Pública (ONAPRE)",
        "fecha":    "01/2026 – Presente",
        "puntos": [
            "<b>Ingeniería de Reglas:</b> Desarrollé un Core Financiero bajo normativas gubernamentales, implementando un motor de reglas atómicas que garantiza el cumplimiento legal y bloquea transacciones sin disponibilidad presupuestaria.",
            "<b>Optimización UX:</b> Diseñé un Dashboard de Alta Densidad (Glassmorphism) que incrementó la eficiencia operativa de los analistas en un 50% frente a sistemas tradicionales.",
        ],
    },
    {
        "titulo":   "Senior Backend Engineer | Migration Lead",
        "empresa":  "Deepcompany (Smart Mobility / Parking Tech)",
        "fecha":    "02/2026 – 06/2026",
        "puntos": [
            "<b>Evolución Tecnológica:</b> Orquesté la migración de un sistema monolítico legacy a una arquitectura de Microservicios orientada a APIs en Node.js, escalando la capacidad de procesamiento de datos en tiempo real.",
            "<b>Modernización DevOps:</b> Implementé la contenerización con <b>Docker</b> y flujos de CI/CD en AWS, reduciendo los tiempos de despliegue en un 70%.",
        ],
    },
    {
        "titulo":   "Full Stack Architect | Product Lead",
        "empresa":  "Multi_Tienda (Ecosistema POS Portable)",
        "fecha":    "09/2025 – 02/2026",
        "puntos": [
            "<b>Ingeniería de Portabilidad:</b> Diseñé un ecosistema agnóstico a la conexión utilizando Electron y SQLite para garantizar la operatividad offline total de PyMEs en entornos de baja conectividad.",
        ],
    },
    {
        "titulo":   "Senior Software Engineer & Architect",
        "empresa":  "IOBPASEL (Gobierno / Infraestructura)",
        "fecha":    "02/2018 – 09/2020",
        "puntos": [
            "<b>Arquitectura Laravel:</b> Pionero en la digitalización de procesos regulatorios mediante Laravel, automatizando la gestión de licencias y el ciclo de facturación para supervisión institucional.",
        ],
    },
    {
        "titulo":   "Arquitecto de Sistemas ERP | Senior Software Engineer",
        "empresa":  "Sistema Multiservicios Casa Lai",
        "fecha":    "2018 – 2025",
        "puntos": [
            "<b>Arquitectura Core:</b> Diseñé y lideré el ciclo de vida (SDLC) de un ERP financiero multimoneda, automatizando la auditoría y conciliación de +5,000 transacciones mensuales.",
            "<b>Integridad de Datos:</b> Reduje en un 30% las discrepancias contables mediante el diseño de esquemas relacionales optimizados y lógica de negocio centralizada.",
        ],
    },
]

EDUCACION = [
    {
        "institucion": "Ingeniería en Informática",
        "descripcion": "Especialista en desarrollo web escalable y diseño de arquitecturas de software.",
    },
    {
        "institucion": "Formación Continua (Platzi/Self-taught)",
        "descripcion": "Next.js, Arquitectura Limpia, Docker y Seguridad en Aplicaciones Web.",
    },
]

# ── Estilos ──────────────────────────────────────────────────────────────────
def make_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles["name"] = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20, textColor=WHITE, spaceAfter=4, leading=24)
    styles["contact"] = ParagraphStyle("contact", fontName="Helvetica", fontSize=8, textColor=LIGHT_GRAY, spaceAfter=5, leading=11)
    styles["sidebar_title"] = ParagraphStyle("sidebar_title", fontName="Helvetica-Bold", fontSize=10, textColor=LIGHT_BLUE, spaceBefore=14, spaceAfter=6, leading=13)
    styles["sidebar_item"] = ParagraphStyle("sidebar_item", fontName="Helvetica", fontSize=8.5, textColor=LIGHT_GRAY, spaceAfter=3, leading=11, leftIndent=0)
    styles["main_title"] = ParagraphStyle("main_title", fontName="Helvetica-Bold", fontSize=13, textColor=DARK_BLUE, spaceBefore=12, spaceAfter=4, leading=16)
    styles["job_title"] = ParagraphStyle("job_title", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT_BLUE, spaceAfter=1, leading=14)
    styles["company"] = ParagraphStyle("company", fontName="Helvetica-Bold", fontSize=9.5, textColor=GRAY_TEXT, spaceAfter=1, leading=13)
    styles["date"] = ParagraphStyle("date", fontName="Helvetica-Oblique", fontSize=8.5, textColor=colors.HexColor("#95a5a6"), spaceAfter=3, leading=11)
    styles["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9, textColor=colors.HexColor("#444444"), spaceAfter=3, leading=12, leftIndent=12, bulletIndent=2)
    styles["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, textColor=colors.HexColor("#333333"), spaceAfter=6, leading=14, alignment=TA_LEFT)
    return styles

def build_sidebar(styles):
    items = []
    items.append(Paragraph(NOMBRE, styles["name"]))
    items.append(Paragraph(f"📍 {UBICACION}", styles["contact"]))
    items.append(Paragraph(f"📞 {TELEFONO}", styles["contact"]))
    items.append(Paragraph(f"✉  {EMAIL}", styles["contact"]))
    items.append(Paragraph(f"🌐 {PORTAFOLIO}", styles["contact"]))
    items.append(Spacer(1, 10))
    
    items.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#34495e"), spaceAfter=4))
    items.append(Paragraph("HABILIDADES", styles["sidebar_title"]))
    for h in HABILIDADES:
        items.append(Paragraph(f"• {h}", styles["sidebar_item"]))

    items.append(Spacer(1, 10))
    items.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#34495e"), spaceAfter=4))
    items.append(Paragraph("IDIOMAS", styles["sidebar_title"]))
    for idioma, nivel in IDIOMAS:
        items.append(Paragraph(f"<b>{idioma}:</b> {nivel}", styles["sidebar_item"]))

    items.append(Spacer(1, 10))
    items.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#34495e"), spaceAfter=4))
    items.append(Paragraph("CERTIFICADOS", styles["sidebar_title"]))
    for c in CERTIFICADOS:
        items.append(Paragraph(f"• {c}", styles["sidebar_item"]))

    return items

def build_main(styles):
    items = []
    items.append(Paragraph("PERFIL PROFESIONAL", styles["main_title"]))
    items.append(HRFlowable(width="100%", thickness=2, color=DARK_BLUE, spaceAfter=6))
    items.append(Paragraph(RESUMEN, styles["body"]))
    items.append(Spacer(1, 4))

    items.append(Paragraph("EXPERIENCIA PROFESIONAL", styles["main_title"]))
    items.append(HRFlowable(width="100%", thickness=2, color=DARK_BLUE, spaceAfter=6))

    for exp in EXPERIENCIA:
        items.append(Paragraph(exp["titulo"], styles["job_title"]))
        if exp.get("empresa"):
            items.append(Paragraph(exp["empresa"], styles["company"]))
        if exp.get("fecha"):
            items.append(Paragraph(exp["fecha"], styles["date"]))
        for punto in exp["puntos"]:
            items.append(Paragraph(f"• {punto}", styles["bullet"]))
        items.append(Spacer(1, 8))

    items.append(Paragraph("EDUCACIÓN", styles["main_title"]))
    items.append(HRFlowable(width="100%", thickness=2, color=DARK_BLUE, spaceAfter=6))
    for edu in EDUCACION:
        items.append(Paragraph(edu["institucion"], styles["job_title"]))
        items.append(Paragraph(edu["descripcion"], styles["body"]))
        items.append(Spacer(1, 4))

    return items

def generate_pdf():
    OUTPUT = "CV_Erian_Arrieche_Optimizado.pdf"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, OUTPUT)

    page_w, page_h = A4
    margin = 10 * mm
    sidebar_w = 70 * mm
    gap = 4 * mm
    main_w = page_w - (2 * margin) - sidebar_w - gap

    styles = make_styles()
    sidebar_items = build_sidebar(styles)
    main_items = build_main(styles)

    from reportlab.platypus import KeepInFrame
    sidebar_frame = KeepInFrame(maxWidth=sidebar_w, maxHeight=page_h - 2 * margin, content=sidebar_items, mode="shrink")
    main_frame = KeepInFrame(maxWidth=main_w, maxHeight=page_h - 2 * margin, content=main_items, mode="shrink")

    two_col = Table([[sidebar_frame, main_frame]], colWidths=[sidebar_w, main_w])
    two_col.setStyle(TableStyle([
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0),   12),
        ("RIGHTPADDING",(0, 0), (0, 0),   gap),
        ("LEFTPADDING", (1, 0), (1, 0),   8),
        ("RIGHTPADDING",(1, 0), (1, 0),   12),
        ("BACKGROUND",  (0, 0), (0, 0),   DARK_BLUE),
        ("BACKGROUND",  (1, 0), (1, 0),   BG_GRAY),
        ("TOPPADDING",  (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING",(0,0), (-1,-1),  16),
    ]))

    doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)
    doc.build([two_col])
    return output_path

if __name__ == "__main__":
    path = generate_pdf()
    print(f"PDF generado en: {path}")
