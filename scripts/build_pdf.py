"""Build the current student-book PDF from Markdown and tested source files."""

from __future__ import annotations

import html
import math
import os
import re
from datetime import date
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Flowable,
    Frame,
    HRFlowable,
    Image as RLImage,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output" / "pdf" / "web-programming-from-platform-to-production-foundations-edition-revised-v10.pdf"
CHAPTERS = sorted((ROOT / "book").glob("part-*/*.md"))
SOLUTION_FILES = sorted(path for path in (ROOT / "labs" / "solutions").glob("week-*/*") if path.is_file())
COVER_ART = ROOT / "assets" / "images" / "cover-web-programming.png"
WEB_REQUEST_ART = ROOT / "assets" / "images" / "web-request-journey-illustration-labeled.png"
AUTHOR_PHOTO = ROOT / "assets" / "images" / "author-mahyar-teymournezhad.jpg"
MEDIA_FIGURES = {
    "development-workstation-evidence-loop": (
        ROOT / "assets" / "images" / "development-workstation-evidence-loop-v1.png",
        "Figure 0.2. The course workstation keeps editing, command execution, the Node.js runtime, local serving, browser inspection, automated testing, and Git history as distinct but cooperating responsibilities.",
    ),
    "repository-first-workflow": (
        ROOT / "assets" / "images" / "repository-first-workflow-v1.png",
        "Figure 0.5. A repository-first workflow begins with a private remote repository, creates one local project folder by cloning, and deliberately returns committed work with push.",
    ),
    "web-request-journey": (
        WEB_REQUEST_ART,
        "Figure 1.2. A browser request crosses local and interconnected networks to reach a web service; the response returns through the network and is rendered by the browser.",
    ),
    "client-server-software-roles": (
        ROOT / "assets" / "images" / "client-server-software-roles-v1.png",
        "Figure 1.3. Client and server are roles within an exchange: an application server answers the browser, then acts as a client when it requests data from a database server.",
    ),
    "html-css-javascript-jobs": (
        ROOT / "assets" / "images" / "html-css-javascript-jobs-labeled.png",
        "Figure 1.4. HTML supplies document meaning and structure; CSS controls presentation; JavaScript can respond to events and update state.",
    ),
    "website-webapp-api": (
        ROOT / "assets" / "images" / "website-webapp-api-comparison-labeled.png",
        "Figure 1.5. A content-oriented website, an interactive web application, and an API emphasize different interfaces while sharing Web infrastructure.",
    ),
    "browser-request-across-networks": (
        ROOT / "assets" / "images" / "browser-request-across-networks-labeled.png",
        "Figure 1.8. A request crosses a local network, independently operated transit networks, and a data-center network; the response returns across interconnected routes.",
    ),
    "protocol-cooperation-across-network": (
        ROOT / "assets" / "images" / "protocol-cooperation-across-network.png",
        "Figure 1.10. An HTTPS exchange combines application, security, transport, network, and link responsibilities while routers forward packets hop by hop.",
    ),
    "dns-name-resolution-ipv4": (
        ROOT / "assets" / "images" / "dns-name-resolution-ipv4.png",
        "Figure 1.11. DNS resolution follows a hierarchy to obtain a typed answer; an IPv4 address contains four eight-bit octets written in dotted-decimal notation.",
    ),
    "local-and-public-server-deployment": (
        ROOT / "assets" / "images" / "local-and-public-server-deployment-v1.png",
        "Figure 1.14. Local development keeps the browser and development server on one computer, whereas public deployment combines a separate DNS lookup with an HTTPS path through Internet routers, a gateway, an application server, and protected data storage.",
    ),
    "week-01-browser-output": (
        ROOT / "assets" / "images" / "week-01-browser-output.png",
        "Figure 1.17. The browser's default rendering of the complete Week 1 HTML example makes the document hierarchy visible before CSS is added.",
    ),
    "semantic-accessibility": (
        ROOT / "assets" / "images" / "semantic-accessibility-illustration.png",
        "Figure 2.3. One semantic document can support visual browsing, keyboard operation, assistive technology, and different viewport sizes.",
    ),
    "week-02-form-output": (
        ROOT / "assets" / "images" / "week-02-form-output.png",
        "Figure 2.5. The browser output of the complete semantic form example shows visible labels, native controls, grouped choices, help text, and a submit button.",
    ),
    "accessibility-combined-evidence": (
        ROOT / "assets" / "images" / "accessibility-combined-evidence-v1.png",
        "Figure 2.7. Accessibility judgments combine automated, keyboard, zoom and reflow, accessibility-tree, assistive-technology, and user-task evidence; no single test proves accessibility.",
    ),
    "responsive-layout": (
        ROOT / "assets" / "images" / "responsive-layout-illustration.png",
        "Figure 3.8. Responsive design preserves content and reading order while the layout adapts to the available viewport.",
    ),
    "week-03-output-desktop": (
        ROOT / "assets" / "images" / "week-03-responsive-output-desktop.png",
        "Figure 3.9. At a wide viewport, the completed CSS example presents the filter and event cards with space for enhanced component layout.",
    ),
    "week-03-output-narrow": (
        ROOT / "assets" / "images" / "week-03-responsive-output-narrow.png",
        "Figure 3.10. At a narrow viewport, the same HTML and CSS reflow the filter and event cards into one readable column.",
    ),
}
MEDIA_MAX_HEIGHT_MM = {
    "development-workstation-evidence-loop": 100,
    "repository-first-workflow": 92,
    "client-server-software-roles": 82,
    "website-webapp-api": 85,
    "local-and-public-server-deployment": 92,
    "accessibility-combined-evidence": 96,
    "week-03-output-desktop": 90,
    "week-03-output-narrow": 105,
}
AUTHOR = "Dr. Mahyar Teymournezhad"

PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 19 * mm
TOP_MARGIN = 22 * mm
BOTTOM_MARGIN = 19 * mm
CONTENT_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

INK = HexColor("#172033")
MUTED = HexColor("#5D6678")
NAVY = HexColor("#12355B")
BLUE = HexColor("#146C94")
TEAL = HexColor("#168C8C")
PALE_BLUE = HexColor("#EAF4F8")
PALE_TEAL = HexColor("#E7F5F2")
PALE_GOLD = HexColor("#FFF4D6")
RULE = HexColor("#CAD4DF")
CODE_BG = HexColor("#F3F5F7")
WHITE = colors.white


def find_font_directory() -> Path:
    candidates: list[Path] = []
    if os.getenv("COURSE_BOOK_FONT_DIR"):
        candidates.append(Path(os.environ["COURSE_BOOK_FONT_DIR"]))
    candidates.extend(
        [
            ROOT / "assets" / "fonts",
            Path(r"C:\texlive\2026\texmf-dist\fonts\truetype\public\dejavu"),
            Path(r"C:\Windows\Fonts"),
            Path("/usr/share/fonts/truetype/dejavu"),
            Path("/Library/Fonts"),
        ]
    )
    required = ["DejaVuSans.ttf", "DejaVuSerif.ttf", "DejaVuSansMono.ttf"]
    for candidate in candidates:
        if all((candidate / name).exists() for name in required):
            return candidate
    raise FileNotFoundError(
        "DejaVu fonts were not found. Install them or set COURSE_BOOK_FONT_DIR."
    )


def register_fonts() -> None:
    font_dir = find_font_directory()
    font_files = {
        "BookSans": "DejaVuSans.ttf",
        "BookSans-Bold": "DejaVuSans-Bold.ttf",
        "BookSans-Italic": "DejaVuSans-Oblique.ttf",
        "BookSerif": "DejaVuSerif.ttf",
        "BookSerif-Bold": "DejaVuSerif-Bold.ttf",
        "BookSerif-Italic": "DejaVuSerif-Italic.ttf",
        "BookMono": "DejaVuSansMono.ttf",
        "BookMono-Bold": "DejaVuSansMono-Bold.ttf",
    }
    for name, filename in font_files.items():
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily(
        "BookSans",
        normal="BookSans",
        bold="BookSans-Bold",
        italic="BookSans-Italic",
        boldItalic="BookSans-Bold",
    )
    pdfmetrics.registerFontFamily(
        "BookSerif",
        normal="BookSerif",
        bold="BookSerif-Bold",
        italic="BookSerif-Italic",
        boldItalic="BookSerif-Bold",
    )


def normalize_text(value: str) -> str:
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2192": "->",
        "\u2190": "<-",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles = {
        "body": ParagraphStyle(
            "BookBody",
            parent=base["BodyText"],
            fontName="BookSerif",
            fontSize=9.4,
            leading=14,
            textColor=INK,
            spaceAfter=7,
            splitLongWords=False,
            allowWidows=0,
            allowOrphans=0,
        ),
        "small": ParagraphStyle(
            "BookSmall",
            fontName="BookSans",
            fontSize=7.6,
            leading=10.5,
            textColor=MUTED,
        ),
        "caption": ParagraphStyle(
            "BookCaption",
            fontName="BookSans-Italic",
            fontSize=7.1,
            leading=10,
            textColor=MUTED,
            leftIndent=4 * mm,
            rightIndent=4 * mm,
            spaceAfter=5,
        ),
        "table-caption": ParagraphStyle(
            "BookTableCaption",
            fontName="BookSans-Bold",
            fontSize=8.2,
            leading=11,
            textColor=NAVY,
            spaceBefore=5,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "h1": ParagraphStyle(
            "Heading1",
            fontName="BookSans-Bold",
            fontSize=20,
            leading=24,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=10,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            fontName="BookSans-Bold",
            fontSize=14,
            leading=18,
            textColor=BLUE,
            spaceBefore=13,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "Heading3",
            fontName="BookSans-Bold",
            fontSize=11.2,
            leading=14,
            textColor=TEAL,
            spaceBefore=9,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "Heading4",
            fontName="BookSans-Bold",
            fontSize=9.5,
            leading=12,
            textColor=INK,
            spaceBefore=7,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "quote": ParagraphStyle(
            "BookQuote",
            fontName="BookSerif-Italic",
            fontSize=9.5,
            leading=14,
            textColor=NAVY,
            leftIndent=10,
            rightIndent=8,
            borderColor=TEAL,
            borderWidth=0,
            borderPadding=(7, 9, 7, 10),
            backColor=PALE_TEAL,
            spaceBefore=5,
            spaceAfter=9,
        ),
        "code": ParagraphStyle(
            "BookCode",
            fontName="BookMono",
            fontSize=7.1,
            leading=10,
            textColor=INK,
            leftIndent=7,
            rightIndent=7,
            borderColor=RULE,
            borderWidth=0.5,
            borderPadding=7,
            backColor=CODE_BG,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "list": ParagraphStyle(
            "BookList",
            parent=base["BodyText"],
            fontName="BookSerif",
            fontSize=9.2,
            leading=13.5,
            textColor=INK,
            leftIndent=3,
            spaceAfter=2,
        ),
        "toc-title": ParagraphStyle(
            "TOCTitle",
            fontName="BookSans-Bold",
            fontSize=22,
            leading=26,
            textColor=NAVY,
            spaceAfter=15,
        ),
        "front-title": ParagraphStyle(
            "FrontTitle",
            fontName="BookSans-Bold",
            fontSize=17,
            leading=21,
            textColor=NAVY,
            spaceAfter=8,
        ),
        "front-heading": ParagraphStyle(
            "FrontHeading",
            fontName="BookSans-Bold",
            fontSize=12,
            leading=15,
            textColor=BLUE,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
    }
    return styles


def inline_markup(text: str) -> str:
    text = normalize_text(text.strip())
    tokens: list[str] = []

    def hold(value: str) -> str:
        tokens.append(value)
        return f"@@TOKEN{len(tokens) - 1}@@"

    text = re.sub(
        r"`([^`]+)`",
        lambda match: hold(
            f'<font name="BookMono" color="#12355B">{html.escape(normalize_text(match.group(1)))}</font>'
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda match: hold(
            f'<a href="{html.escape(match.group(2), quote=True)}" color="#146C94"><u>{html.escape(match.group(1))}</u></a>'
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: hold(html.escape(match.group(1))),
        text,
    )
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for index in reversed(range(len(tokens))):
        token = tokens[index]
        text = text.replace(f"@@TOKEN{index}@@", token)
    return text


class WebSequenceDiagram(Flowable):
    def __init__(self, width: float):
        super().__init__()
        self.width = width
        self.height = 97 * mm

    @staticmethod
    def _arrow(canvas, x1, y1, x2, y2, color=TEAL):
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        if length == 0:
            return
        ux, uy = dx / length, dy / length
        px, py = -uy, ux
        head_length = 2.5 * mm
        head_half_width = 1.2 * mm
        base_x, base_y = x2 - ux * head_length, y2 - uy * head_length
        canvas.setStrokeColor(color)
        canvas.setLineWidth(0.9)
        canvas.setLineCap(1)
        canvas.setLineJoin(1)
        canvas.line(x1, y1, x2, y2)
        canvas.line(base_x + px * head_half_width, base_y + py * head_half_width, x2, y2)
        canvas.line(base_x - px * head_half_width, base_y - py * head_half_width, x2, y2)

    def draw(self) -> None:
        canvas = self.canv
        labels = ["User", "Browser", "DNS resolver", "Web server"]
        # Keep every participant box inside the available text width.  The final
        # centre is derived from the actual frame instead of an A4-specific guess.
        x_values = [18 * mm, 59 * mm, 108 * mm, self.width - 18 * mm]
        top = self.height - 13 * mm

        canvas.setFont("BookSans-Bold", 7.8)
        for x, label in zip(x_values, labels):
            canvas.setFillColor(PALE_BLUE)
            canvas.setStrokeColor(BLUE)
            canvas.roundRect(x - 15 * mm, top - 4 * mm, 30 * mm, 9 * mm, 2 * mm, fill=1)
            canvas.setFillColor(INK)
            canvas.drawCentredString(x, top - 0.5 * mm, label)
            canvas.setStrokeColor(RULE)
            canvas.setDash(2, 2)
            canvas.line(x, top - 5 * mm, x, 7 * mm)
            canvas.setDash()

        events = [
            (0, 1, "Navigate to HTTPS URL"),
            (1, 2, "Resolve host name"),
            (2, 1, "Return address information"),
            (1, 3, "Connect and establish TLS"),
            (1, 3, "Send HTTP request"),
            (3, 1, "Return HTTP response"),
            (1, 1, "Parse HTML; discover resources"),
            (1, 3, "Request additional resources"),
            (3, 1, "Return additional responses"),
            (1, 1, "Layout and paint"),
        ]
        y = top - 11 * mm
        canvas.setFont("BookSans", 6.7)
        for source, target, label in events:
            start = x_values[source]
            end = x_values[target]
            canvas.setStrokeColor(TEAL if source != target else BLUE)
            if source == target:
                canvas.line(start, y, start + 12 * mm, y)
                canvas.line(start + 12 * mm, y, start + 12 * mm, y - 4 * mm)
                self._arrow(canvas, start + 12 * mm, y - 4 * mm, start, y - 4 * mm, color=BLUE)
                text_x = start + 15 * mm
                text_y = y - 2.8 * mm
            else:
                self._arrow(canvas, start, y, end, y, color=TEAL)
                text_x = (start + end) / 2
                text_y = y + 1.5 * mm
            canvas.setFillColor(INK)
            canvas.drawCentredString(text_x, text_y, label)
            y -= 7 * mm
        canvas.setFillColor(MUTED)
        canvas.setFont("BookSans-Italic", 6.8)
        canvas.drawString(
            4 * mm,
            2.5 * mm,
            "Figure 1.7. A page navigation coordinates naming, connection security, HTTP exchanges, parsing, and rendering.",
        )


class ConceptFigure(Flowable):
    """A deterministic vector illustration for one foundational concept."""

    captions = {
        "terminal-directory-rescue": "Figure 0.3. npm searches for package.json in the terminal's current project directory.",
        "javascript-runtime-map": "Figure 0.4. JavaScript runs in browsers and Node.js, while each environment supplies different host APIs.",
        "two-terminal-model": "Figure 0.6. The server and command terminals are ordinary terminals with different current jobs.",
        "server-browser-evidence": "Figure 0.7. Terminal output and a browser page together prove that localhost is responding.",
        "network-panel": "Figure 0.8. Network records requests; select the document row to inspect HTTP evidence.",
        "enoent-diagnosis": "Figure 0.9. The ENOENT path shows where npm looked for package.json.",
        "web-layers": "Figure 1.1. The Web is one application built on Internet infrastructure.",
        "url-anatomy": "Figure 1.6. A URL is a structured identifier whose components have distinct roles.",
        "protocol-stack": "Figure 1.9. Two common HTTPS stacks. Read each column from the web content down to the network link.",
        "dns-resolution": "Figure 1.11. A recursive resolver follows the DNS hierarchy and caches the answer.",
        "http-exchange": "Figure 1.12. HTTP separates client request intent from server response outcome.",
        "browser-pipeline": "Figure 1.13. Browsers transform bytes and resources into pixels and interaction.",
        "debugging-loop": "Figure 1.15. Evidence-driven debugging is a repeatable scientific loop.",
        "html-tree": "Figure 1.16. Nested HTML elements become a document tree.",
        "git-workflow": "Figure 1.18. Git moves selected changes from the working tree into durable history.",
        "html-anatomy": "Figure 2.1. An HTML element combines tags, attributes, content, and a parsed DOM representation.",
        "semantic-landmarks": "Figure 2.2. Semantic landmarks divide a page into named, navigable regions.",
        "form-data-flow": "Figure 2.4. Labels identify controls; names carry values across the request boundary.",
        "accessibility-tree": "Figure 2.6. HTML and browser state contribute to a platform accessibility representation.",
        "css-rule-anatomy": "Figure 3.1. A CSS rule connects a selector to a declaration block containing property-and-value proposals.",
        "selector-matching": "Figure 3.2. Selectors express different relationships and produce different sets of matched elements.",
        "css-cascade": "Figure 3.3. The cascade resolves relevant declarations through an ordered decision process.",
        "box-model": "Figure 3.4. Padding, border, and margin surround an element's content box.",
        "logical-axes": "Figure 3.5. Logical inline and block axes follow writing mode and direction instead of assuming physical sides.",
        "layout-systems": "Figure 3.6. Flexbox coordinates one primary axis; Grid coordinates rows and columns.",
        "responsive-reflow": "Figure 3.7. Responsive constraints reflow the same content without changing its meaning.",
        "container-query": "Figure 3.11. One component can adapt to the inline size of its own container at a single viewport width.",
        "css-devtools-evidence": "Figure 3.12. CSS debugging traces evidence from resource loading through matching, cascade, computed values, and layout.",
    }

    def __init__(self, kind: str, width: float):
        super().__init__()
        self.kind = kind
        self.width = width
        heights_mm = {
            "protocol-stack": 74,
            "terminal-directory-rescue": 82,
            "two-terminal-model": 82,
            "server-browser-evidence": 76,
            "network-panel": 86,
            "enoent-diagnosis": 78,
            "javascript-runtime-map": 76,
            "css-rule-anatomy": 70,
            "selector-matching": 72,
            "logical-axes": 72,
            "container-query": 74,
            "css-devtools-evidence": 70,
        }
        self.height = heights_mm.get(kind, 62) * mm

    def _box(self, canvas, x, y, w, h, label, fill=PALE_BLUE, stroke=BLUE, size=7.4):
        canvas.setFillColor(fill)
        canvas.setStrokeColor(stroke)
        canvas.setLineWidth(0.8)
        canvas.roundRect(x, y, w, h, 2.2 * mm, fill=1, stroke=1)
        canvas.setFillColor(INK)
        canvas.setFont("BookSans-Bold", size)
        canvas.drawCentredString(x + w / 2, y + h / 2 - 2.3, label)

    def _arrow(self, canvas, x1, y1, x2, y2, color=TEAL):
        """Draw a directionally correct arrow, including on diagonal paths."""
        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)
        if length == 0:
            return
        ux, uy = dx / length, dy / length
        px, py = -uy, ux
        head_length = 2.7 * mm
        head_half_width = 1.35 * mm
        base_x = x2 - ux * head_length
        base_y = y2 - uy * head_length
        canvas.setStrokeColor(color)
        canvas.setLineWidth(1.1)
        canvas.setLineCap(1)
        canvas.setLineJoin(1)
        canvas.line(x1, y1, x2, y2)
        canvas.line(base_x + px * head_half_width, base_y + py * head_half_width, x2, y2)
        canvas.line(base_x - px * head_half_width, base_y - py * head_half_width, x2, y2)

    def _horizontal_layout(self, widths_mm, left_mm=6, right_mm=6):
        """Return x positions whose boxes fit exactly within the figure interior."""
        widths = [value * mm for value in widths_mm]
        available = self.width - (left_mm + right_mm) * mm - sum(widths)
        gap = available / max(1, len(widths) - 1)
        if gap < 1.5 * mm:
            raise ValueError(f"Figure {self.kind!r} has insufficient horizontal space")
        positions = []
        cursor = left_mm * mm
        for width in widths:
            positions.append(cursor)
            cursor += width + gap
        return positions, widths

    def _terminal_window(self, c, x, y, w, h, title, lines, accent=TEAL):
        c.setFillColor(HexColor("#101827")); c.setStrokeColor(accent); c.setLineWidth(0.9)
        c.roundRect(x, y, w, h, 2 * mm, fill=1, stroke=1)
        c.setFillColor(accent); c.roundRect(x, y + h - 8 * mm, w, 8 * mm, 2 * mm, fill=1, stroke=0)
        c.rect(x, y + h - 8 * mm, w, 4 * mm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("BookSans-Bold", 6.5)
        c.drawString(x + 3 * mm, y + h - 5.2 * mm, title)
        c.setFont("BookMono", 5.35)
        line_y = y + h - 12 * mm
        for line in lines:
            c.setFillColor(HexColor("#B9F4E8") if line.startswith(">") else WHITE)
            c.drawString(x + 3 * mm, line_y, line)
            line_y -= 4.2 * mm

    def draw(self) -> None:
        canvas = self.canv
        canvas.setFillColor(HexColor("#F8FBFC"))
        canvas.setStrokeColor(RULE)
        canvas.roundRect(0, 8 * mm, self.width, self.height - 8 * mm, 3 * mm, fill=1, stroke=1)
        getattr(self, f"_draw_{self.kind.replace('-', '_')}")(canvas)
        canvas.setFillColor(MUTED)
        canvas.setFont("BookSans-Italic", 6.8)
        canvas.drawString(4 * mm, 2.5 * mm, self.captions[self.kind])

    def _draw_terminal_directory_rescue(self, c):
        panel_w = (self.width - 18 * mm) / 2
        self._terminal_window(
            c, 5 * mm, 20 * mm, panel_w, 47 * mm, "WRONG DIRECTORY - npm FAILS",
            [
                r"C:\Users\Mahyar>npm run serve:week01:starter",
                "npm error code ENOENT",
                r"npm error path C:\Users\Mahyar\package.json",
                "Meaning: npm looked here; package.json is absent.",
            ],
            accent=HexColor("#B85C4A"),
        )
        right_x = 13 * mm + panel_w
        self._terminal_window(
            c, right_x, 20 * mm, panel_w, 47 * mm, "CORRECT ROOT - VERIFY BEFORE RUNNING",
            [
                "> cd /d C:\\Users\\Mahyar\\Documents\\GitHub\\",
                r"  web-programming-course-book",
                r"> dir package.json",
                "  package.json",
                r"> npm run serve:week01:starter",
            ],
            accent=HexColor("#23866B"),
        )
        self._arrow(c, 5 * mm + panel_w, 43 * mm, right_x - 1 * mm, 43 * mm)
        c.setFillColor(PALE_GOLD); c.setStrokeColor(HexColor("#B06A2F"))
        c.roundRect(22 * mm, 11 * mm, self.width - 44 * mm, 6 * mm, 1 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6.2)
        c.drawCentredString(self.width / 2, 13 * mm, "Rule: see package.json before running an npm project command")

    def _draw_javascript_runtime_map(self, c):
        language_x = 47 * mm
        language_w = self.width - 94 * mm
        self._box(
            c, language_x, 59 * mm, language_w, 10 * mm,
            "JAVASCRIPT (ECMASCRIPT) LANGUAGE", fill=PALE_GOLD,
            stroke=HexColor("#B06A2F"), size=7.1,
        )
        browser_x = 7 * mm
        node_x = self.width - 77 * mm
        panel_w = 70 * mm
        c.setFillColor(PALE_BLUE); c.setStrokeColor(BLUE); c.setLineWidth(0.8)
        c.roundRect(browser_x, 25 * mm, panel_w, 25 * mm, 2.2 * mm, fill=1, stroke=1)
        c.setFillColor(PALE_TEAL); c.setStrokeColor(TEAL)
        c.roundRect(node_x, 25 * mm, panel_w, 25 * mm, 2.2 * mm, fill=1, stroke=1)
        self._arrow(c, language_x + 12 * mm, 59 * mm, browser_x + panel_w / 2, 51 * mm, color=BLUE)
        self._arrow(c, language_x + language_w - 12 * mm, 59 * mm, node_x + panel_w / 2, 51 * mm, color=TEAL)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 7.2)
        c.drawCentredString(browser_x + panel_w / 2, 44 * mm, "BROWSER RUNTIME")
        c.drawCentredString(node_x + panel_w / 2, 44 * mm, "NODE.JS RUNTIME")
        c.setFont("BookSans", 5.5)
        c.drawCentredString(browser_x + panel_w / 2, 36 * mm, "Host APIs: DOM, events, fetch, storage")
        c.drawCentredString(browser_x + panel_w / 2, 29 * mm, "Runs client-side code for a page")
        c.drawCentredString(node_x + panel_w / 2, 36 * mm, "Host APIs: files, process, HTTP server")
        c.drawCentredString(node_x + panel_w / 2, 29 * mm, "Runs tools and server-side code")
        c.setFillColor(PALE_TEAL); c.setStrokeColor(TEAL)
        c.roundRect(24 * mm, 12 * mm, self.width - 48 * mm, 7 * mm, 1.2 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6.1)
        c.drawCentredString(self.width / 2, 14.5 * mm, "Shared language: values, variables, functions, arrays, objects, promises, and modules")

    def _draw_two_terminal_model(self, c):
        panel_w = (self.width - 18 * mm) / 2
        self._terminal_window(
            c, 5 * mm, 22 * mm, panel_w, 49 * mm, "TERMINAL A - SERVER (LEAVE RUNNING)",
            [
                "> npm run serve:week01:starter",
                "Serving ...\\labs\\starters\\week-01",
                "Open http://localhost:8000/",
                "Press Ctrl+C to stop.",
                "[No prompt: the server owns this terminal]",
            ],
            accent=TEAL,
        )
        right_x = 13 * mm + panel_w
        self._terminal_window(
            c, right_x, 22 * mm, panel_w, 49 * mm, "TERMINAL B - COMMANDS (AVAILABLE)",
            [
                r"> cd /d C:\...\web-programming-course-book",
                "> git status",
                "On branch main",
                "> npm test",
                "Foundation verification passed.",
            ],
            accent=BLUE,
        )
        c.setFillColor(INK); c.setFont("BookSans", 6.2)
        c.drawCentredString(self.width / 2, 14 * mm, "They may be two Command Prompt windows or two VS Code terminal tabs; no special server-terminal app is installed.")

    def _draw_server_browser_evidence(self, c):
        terminal_w = 76 * mm
        self._terminal_window(
            c, 5 * mm, 19 * mm, terminal_w, 48 * mm, "SERVER TERMINAL - EXPECTED OUTPUT",
            [
                "> npm run serve:week01:starter",
                "Serving C:\\...\\labs\\starters\\week-01",
                "Open http://localhost:8000/",
                "Press Ctrl+C to stop.",
            ],
            accent=TEAL,
        )
        bx = 88 * mm; bw = self.width - bx - 5 * mm
        c.setFillColor(WHITE); c.setStrokeColor(BLUE); c.roundRect(bx, 19 * mm, bw, 48 * mm, 2 * mm, fill=1, stroke=1)
        c.setFillColor(HexColor("#DFE8EF")); c.roundRect(bx, 57 * mm, bw, 10 * mm, 2 * mm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.roundRect(bx + 5 * mm, 59.5 * mm, bw - 10 * mm, 5 * mm, 1 * mm, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("BookMono", 5.5); c.drawString(bx + 8 * mm, 61 * mm, "http://localhost:8000/")
        c.setFont("BookSans-Bold", 12); c.setFillColor(NAVY); c.drawString(bx + 8 * mm, 46 * mm, "Campus Hub")
        c.setFont("BookSans", 7); c.setFillColor(INK)
        c.drawString(bx + 8 * mm, 38 * mm, "Robotics workshop")
        c.drawString(bx + 8 * mm, 32 * mm, "Accessible web event form")
        c.setFillColor(PALE_TEAL); c.setStrokeColor(TEAL); c.roundRect(bx + 8 * mm, 22 * mm, 36 * mm, 6 * mm, 1 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6); c.drawCentredString(bx + 26 * mm, 24 * mm, "PAGE RESPONDED")
        self._arrow(c, 82 * mm, 43 * mm, bx - 1 * mm, 43 * mm)

    def _draw_network_panel(self, c):
        x = 5 * mm; y = 18 * mm; w = self.width - 10 * mm; h = 59 * mm
        c.setFillColor(WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.9); c.roundRect(x, y, w, h, 2 * mm, fill=1, stroke=1)
        c.setFillColor(HexColor("#E8EDF2")); c.rect(x, y + h - 10 * mm, w, 10 * mm, fill=1, stroke=0)
        tabs = [("Elements", 9), ("Console", 34), ("Sources", 57), ("Network", 80)]
        c.setFont("BookSans-Bold", 6.2)
        for label, offset in tabs:
            c.setFillColor(BLUE if label == "Network" else MUTED)
            c.drawString(x + offset * mm, y + h - 6.3 * mm, label)
        c.setStrokeColor(BLUE); c.setLineWidth(1.4); c.line(x + 79 * mm, y + h - 8 * mm, x + 104 * mm, y + h - 8 * mm)
        c.setFillColor(PALE_GOLD); c.setStrokeColor(HexColor("#B06A2F")); c.roundRect(x + 111 * mm, y + h - 8 * mm, 42 * mm, 5.5 * mm, 1 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 5.7); c.drawCentredString(x + 132 * mm, y + h - 6.2 * mm, "2  Reload the page")
        c.setFillColor(PALE_BLUE); c.rect(x, y + 31 * mm, 69 * mm, 16 * mm, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont("BookSans-Bold", 5.8)
        for label, px in [("Name", 4), ("Status", 32), ("Type", 48)]: c.drawString(x + px * mm, y + 43 * mm, label)
        c.setFillColor(INK); c.setFont("BookMono", 5.8)
        c.drawString(x + 4 * mm, y + 36 * mm, "localhost")
        c.drawString(x + 34 * mm, y + 36 * mm, "200")
        c.drawString(x + 49 * mm, y + 36 * mm, "document")
        c.setFillColor(PALE_GOLD); c.setStrokeColor(HexColor("#B06A2F")); c.roundRect(x + 3 * mm, y + 27 * mm, 55 * mm, 5.5 * mm, 1 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 5.7); c.drawCentredString(x + 30.5 * mm, y + 29 * mm, "3  Select the document row")
        dx = x + 73 * mm
        c.setFillColor(PALE_TEAL); c.rect(dx, y + 31 * mm, w - 73 * mm, 16 * mm, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont("BookSans-Bold", 6); c.drawString(dx + 3 * mm, y + 43 * mm, "Headers   Preview   Response   Timing")
        c.setFillColor(INK); c.setFont("BookMono", 5.45)
        details = ["Request URL: http://localhost:8000/", "Request Method: GET", "Status Code: 200 OK", "Content-Type: text/html; charset=utf-8"]
        detail_y = y + 36 * mm
        for line in details:
            c.drawString(dx + 3 * mm, detail_y, line); detail_y -= 6 * mm
        c.setFillColor(PALE_GOLD); c.setStrokeColor(HexColor("#B06A2F")); c.roundRect(x + 3 * mm, y + 49 * mm, 52 * mm, 5.5 * mm, 1 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans-Bold", 5.7); c.drawCentredString(x + 29 * mm, y + 51 * mm, "1  Select Network")

    def _draw_enoent_diagnosis(self, c):
        c.setFillColor(HexColor("#FFF0EC")); c.setStrokeColor(HexColor("#B85C4A")); c.roundRect(5 * mm, 40 * mm, 55 * mm, 25 * mm, 2 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookMono", 5.4)
        c.drawString(8 * mm, 57 * mm, "npm error code ENOENT")
        c.drawString(8 * mm, 50 * mm, r"path C:\Users\Mahyar\package.json")
        c.setFont("BookSans-Bold", 6.2); c.drawString(8 * mm, 44 * mm, "npm looked in C:\\Users\\Mahyar")
        steps = [("1 Show location", "cd"), ("2 Find project", "dir"), ("3 Enter root", "cd /d ..."), ("4 Prove file", "dir package.json"), ("5 Run script", "npm run ...")]
        positions, widths = self._horizontal_layout([27, 27, 28, 31, 29], left_mm=5, right_mm=5)
        for index, ((label, command), px, pw) in enumerate(zip(steps, positions, widths)):
            self._box(c, px, 19 * mm, pw, 15 * mm, label, fill=PALE_TEAL, stroke=TEAL, size=5.5)
            c.setFillColor(MUTED); c.setFont("BookMono", 4.9); c.drawCentredString(px + pw / 2, 22 * mm, command)
            if index < len(steps) - 1: self._arrow(c, px + pw, 26.5 * mm, positions[index + 1], 26.5 * mm)
        self._arrow(c, 60 * mm, 50 * mm, 83 * mm, 35 * mm, color=HexColor("#B85C4A"))
        c.setFillColor(INK); c.setFont("BookSans", 6.1)
        c.drawString(87 * mm, 54 * mm, "ENOENT means a required file or folder was not found.")
        c.drawString(87 * mm, 47 * mm, "It does not mean Node.js must be reinstalled.")

    def _draw_web_layers(self, c):
        self._box(c, 8 * mm, 22 * mm, 44 * mm, 22 * mm, "Internet", fill=HexColor("#DCEAF5"), stroke=NAVY, size=9)
        self._box(c, 63 * mm, 29 * mm, 38 * mm, 15 * mm, "World Wide Web", fill=PALE_TEAL, stroke=TEAL)
        self._box(c, 114 * mm, 35 * mm, 23 * mm, 10 * mm, "HTML")
        self._box(c, 141 * mm, 35 * mm, 23 * mm, 10 * mm, "CSS")
        self._box(c, 127.5 * mm, 20 * mm, 23 * mm, 10 * mm, "JavaScript")
        self._arrow(c, 52 * mm, 33 * mm, 63 * mm, 36 * mm)
        self._arrow(c, 101 * mm, 36 * mm, 114 * mm, 40 * mm)
        self._arrow(c, 101 * mm, 36 * mm, 127.5 * mm, 25 * mm)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.5)
        c.drawCentredString(30 * mm, 17 * mm, "Networks, routers, IP, transport")
        c.drawCentredString(82 * mm, 22 * mm, "URLs + HTTP + browsers")

    def _draw_url_anatomy(self, c):
        segments = [
            ("https://", "scheme", 22, NAVY), ("hub.example.edu", "host", 39, BLUE),
            (":8443", "port", 17, TEAL), ("/events", "path", 23, HexColor("#6B5CA5")),
            ("?limit=5", "query", 26, HexColor("#B06A2F")), ("#today", "fragment", 21, HexColor("#8C4663")),
        ]
        positions, widths = self._horizontal_layout([item[2] for item in segments], left_mm=6, right_mm=6)
        for (value, label, _width_mm, color), x, w in zip(segments, positions, widths):
            c.setFillColor(color); c.roundRect(x, 29 * mm, w, 11 * mm, 1.5 * mm, fill=1, stroke=0)
            c.setFillColor(WHITE); c.setFont("BookMono-Bold", 6.4); c.drawCentredString(x + w / 2, 34 * mm, value)
            c.setFillColor(INK); c.setFont("BookSans-Bold", 6.5); c.drawCentredString(x + w / 2, 23 * mm, label)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.4)
        c.drawString(6 * mm, 15 * mm, "Origin = scheme + host + port")
        c.drawRightString(self.width - 6 * mm, 15 * mm, "The fragment remains on the client")

    def _draw_protocol_stack(self, c):
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6.6)
        c.drawCentredString(47 * mm, 61 * mm, "Example A - HTTPS using HTTP/2")
        c.drawCentredString(123 * mm, 61 * mm, "Example B - HTTPS using HTTP/3")
        stacks = [
            (14 * mm, 66 * mm, ["HTML, CSS, JS, images", "HTTP/2", "TLS", "TCP", "IP", "Wi-Fi or Ethernet"]),
            (90 * mm, 66 * mm, ["HTML, CSS, JS, images", "HTTP/3", "QUIC (includes TLS)", "UDP", "IP", "Wi-Fi or Ethernet"]),
        ]
        fills = [NAVY, BLUE, TEAL, HexColor("#6B5CA5"), HexColor("#B06A2F"), HexColor("#167A55")]
        for x, width, labels in stacks:
            y = 54 * mm
            for label, fill in zip(labels, fills):
                c.setFillColor(fill); c.roundRect(x, y, width, 5.2 * mm, 1 * mm, fill=1, stroke=0)
                c.setFillColor(WHITE); c.setFont("BookSans-Bold", 5.6)
                c.drawCentredString(x + width / 2, y + 1.75 * mm, label)
                y -= 5.7 * mm
        c.setFillColor(PALE_GOLD); c.setStrokeColor(HexColor("#B06A2F")); c.setLineWidth(0.7)
        c.roundRect(25 * mm, 12 * mm, self.width - 50 * mm, 6 * mm, 1.2 * mm, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("BookSans", 5.8)
        c.drawCentredString(self.width / 2, 14 * mm, "DNS name lookup is a related, usually separate exchange performed before or when an address is needed.")

    def _draw_dns_resolution(self, c):
        labels = ["Browser", "Recursive resolver", "Root", "TLD", "Authoritative"]
        y = 31 * mm
        positions, widths = self._horizontal_layout([25, 36, 20, 20, 31], left_mm=5, right_mm=5)
        for label, x, width in zip(labels, positions, widths):
            self._box(c, x, y, width, 11 * mm, label, size=6.25)
        for index in range(len(labels) - 1):
            self._arrow(c, positions[index] + widths[index], y + 7 * mm, positions[index + 1], y + 7 * mm)
        self._arrow(c, positions[1], y + 2 * mm, positions[0] + widths[0], y + 2 * mm, color=BLUE)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.3)
        c.drawString(5 * mm, 19 * mm, "1. Ask for an address record")
        c.drawString(63 * mm, 19 * mm, "2. Follow referrals when no cached answer exists")
        c.drawString(5 * mm, 13 * mm, "3. Return the answer and cache it for its TTL")

    def _draw_http_exchange(self, c):
        self._box(c, 10 * mm, 27 * mm, 35 * mm, 18 * mm, "Browser client", fill=PALE_TEAL, stroke=TEAL)
        server_x = self.width - 45 * mm
        self._box(c, server_x, 27 * mm, 35 * mm, 18 * mm, "Web server", fill=PALE_BLUE, stroke=BLUE)
        self._arrow(c, 46 * mm, 40 * mm, server_x - 1 * mm, 40 * mm)
        self._arrow(c, server_x - 1 * mm, 29 * mm, 46 * mm, 29 * mm, color=BLUE)
        c.setFillColor(INK); c.setFont("BookMono", 6.3)
        c.drawCentredString(88 * mm, 44 * mm, "GET /events  Accept: text/html")
        c.drawCentredString(88 * mm, 23 * mm, "200 OK  Content-Type: text/html")
        c.setFont("BookSans", 6.4); c.setFillColor(MUTED)
        c.drawCentredString(88 * mm, 15 * mm, "Method and target express intent; status and fields describe the outcome.")

    def _draw_browser_pipeline(self, c):
        steps = ["Response bytes", "HTML -> DOM", "CSS -> styles", "Layout", "Paint", "Composite"]
        positions, widths = self._horizontal_layout([23, 23, 23, 23, 23, 23], left_mm=5, right_mm=5)
        for i, (label, x, w) in enumerate(zip(steps, positions, widths)):
            self._box(c, x, 29 * mm, w, 13 * mm, label, fill=PALE_TEAL if i < 3 else PALE_BLUE, stroke=TEAL if i < 3 else BLUE, size=5.9)
            if i < len(steps) - 1:
                self._arrow(c, x + w, 35.5 * mm, positions[i + 1], 35.5 * mm)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.3)
        c.drawCentredString(self.width / 2, 18 * mm, "Scripts and user actions can change the DOM and trigger later rendering work again.")

    def _draw_debugging_loop(self, c):
        labels = ["1  Observe", "2  Hypothesize", "3  Test", "4  Change one factor", "5  Record"]
        positions = [(10, 33), (54, 43), (105, 43), (124, 25), (73, 13)]
        widths = [28, 32, 25, 38, 27]
        for label, (x, y), w in zip(labels, positions, widths): self._box(c, x * mm, y * mm, w * mm, 10 * mm, label, size=6.3)
        points = [(38,38,54,48),(86,48,105,48),(130,48,143,35),(124,30,100,18),(73,18,24,33)]
        for x1,y1,x2,y2 in points: self._arrow(c,x1*mm,y1*mm,x2*mm,y2*mm)

    def _draw_html_tree(self, c):
        nodes = [("html", 76, 43, 25), ("head", 42, 30, 25), ("body", 110, 30, 25), ("title", 23, 17, 25), ("meta", 58, 17, 25), ("header", 92, 17, 25), ("main", 126, 17, 25)]
        centers = {}
        for label, x, y, w in nodes:
            self._box(c, x*mm, y*mm, w*mm, 9*mm, label, size=6.4); centers[label]=((x+w/2)*mm,y*mm)
        for parent, child in [("html","head"),("html","body"),("head","title"),("head","meta"),("body","header"),("body","main")]:
            px,py=centers[parent]; cx,cy=centers[child]; c.setStrokeColor(RULE); c.line(px,py,cx,cy+9*mm)

    def _draw_git_workflow(self, c):
        labels = [("Working tree", PALE_BLUE, BLUE), ("Staging area", PALE_TEAL, TEAL), ("Local repository", PALE_BLUE, BLUE), ("Remote repository", PALE_GOLD, HexColor("#B06A2F"))]
        positions, widths = self._horizontal_layout([32, 32, 38, 35], left_mm=6, right_mm=6)
        for (label, fill, stroke), x, width in zip(labels, positions, widths):
            self._box(c, x, 29 * mm, width, 14 * mm, label, fill=fill, stroke=stroke, size=6.3)
        for i in range(3):
            self._arrow(c, positions[i] + widths[i], 36 * mm, positions[i + 1], 36 * mm)
        c.setFillColor(MUTED); c.setFont("BookSans",6.2)
        for i, command in enumerate(["git add", "git commit", "git push"]):
            midpoint = (positions[i] + widths[i] + positions[i + 1]) / 2
            c.drawCentredString(midpoint, 20 * mm, command)

    def _draw_html_anatomy(self, c):
        segments = [
            ("<a", "tag name", 13, NAVY),
            ('class="event-link"', "attribute", 39, BLUE),
            ('href="/events"', "attribute", 36, TEAL),
            (">", "boundary", 7, HexColor("#6B5CA5")),
            ("Robotics event", "text content", 37, HexColor("#B06A2F")),
            ("</a>", "closing tag", 18, NAVY),
        ]
        positions, widths = self._horizontal_layout(
            [item[2] for item in segments], left_mm=5, right_mm=5
        )
        for (value, label, _width_mm, color), x, width in zip(segments, positions, widths):
            c.setFillColor(color)
            c.roundRect(x, 38 * mm, width, 10 * mm, 1.2 * mm, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("BookMono-Bold", 5.5 if width < 20 * mm else 5.9)
            c.drawCentredString(x + width / 2, 41.7 * mm, value)
            c.setFillColor(INK)
            c.setFont("BookSans-Bold", 5.5)
            c.drawCentredString(x + width / 2, 32 * mm, label)
        self._arrow(c, self.width / 2, 29 * mm, self.width / 2, 23 * mm)
        self._box(
            c,
            38 * mm,
            12 * mm,
            self.width - 76 * mm,
            10 * mm,
            "DOM anchor node: class + href + text",
            fill=PALE_TEAL,
            stroke=TEAL,
            size=6.4,
        )

    def _draw_semantic_landmarks(self, c):
        x, y, w, h = 23 * mm, 13 * mm, self.width - 46 * mm, 37 * mm
        c.setFillColor(WHITE); c.setStrokeColor(NAVY); c.setLineWidth(1)
        c.roundRect(x, y, w, h, 2.5 * mm, fill=1, stroke=1)
        self._box(c, x + 4 * mm, y + 27 * mm, w - 8 * mm, 6 * mm, "header", fill=PALE_BLUE, size=6.2)
        self._box(c, x + 4 * mm, y + 19 * mm, 28 * mm, 6 * mm, "nav", fill=PALE_TEAL, stroke=TEAL, size=6.2)
        self._box(c, x + 35 * mm, y + 9 * mm, w - 39 * mm, 16 * mm, "main", fill=PALE_BLUE, size=6.4)
        self._box(c, x + 39 * mm, y + 12 * mm, 42 * mm, 7 * mm, "section", fill=WHITE, stroke=TEAL, size=6.0)
        self._box(c, x + 84 * mm, y + 12 * mm, w - 88 * mm, 7 * mm, "article", fill=WHITE, stroke=TEAL, size=6.0)
        self._box(c, x + 4 * mm, y + 2 * mm, w - 8 * mm, 5 * mm, "footer", fill=PALE_GOLD, stroke=HexColor("#B06A2F"), size=5.9)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.2)
        c.drawCentredString(self.width / 2, 52 * mm, "One document, several regions with distinct purposes")

    def _draw_form_data_flow(self, c):
        labels = [("Visible label", PALE_TEAL, TEAL), ("Named control", PALE_BLUE, BLUE), ("name=value", PALE_GOLD, HexColor("#B06A2F")), ("Server validation", PALE_BLUE, NAVY)]
        positions, widths = self._horizontal_layout([31, 33, 31, 39], left_mm=7, right_mm=7)
        for (label, fill, stroke), x, width in zip(labels, positions, widths):
            self._box(c, x, 29 * mm, width, 13 * mm, label, fill=fill, stroke=stroke, size=6.3)
        for index in range(3):
            self._arrow(c, positions[index] + widths[index], 35.5 * mm, positions[index + 1], 35.5 * mm)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        notes = ["for -> id", "form rules", "HTTP request"]
        for index, note in enumerate(notes):
            midpoint = (positions[index] + widths[index] + positions[index + 1]) / 2
            c.drawCentredString(midpoint, 22 * mm, note)
        c.drawCentredString(self.width / 2, 15 * mm, "Client constraints improve feedback; the server still treats every value as untrusted.")

    def _draw_accessibility_tree(self, c):
        labels = [("HTML source", PALE_BLUE, BLUE), ("DOM + state", PALE_TEAL, TEAL), ("Accessibility tree", PALE_GOLD, HexColor("#B06A2F")), ("Assistive technology", PALE_BLUE, NAVY)]
        positions, widths = self._horizontal_layout([29, 31, 39, 42], left_mm=5, right_mm=5)
        for (label, fill, stroke), x, width in zip(labels, positions, widths):
            self._box(c, x, 29 * mm, width, 14 * mm, label, fill=fill, stroke=stroke, size=6.1)
        for index in range(3):
            self._arrow(c, positions[index] + widths[index], 36 * mm, positions[index + 1], 36 * mm)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        c.drawCentredString(self.width / 2, 20 * mm, "Roles, names, states, values, and relationships are exposed through platform APIs.")
        c.drawCentredString(self.width / 2, 15 * mm, "CSS and JavaScript can alter what is present, visible, operable, or exposed.")

    def _draw_css_rule_anatomy(self, c):
        c.setFillColor(INK); c.setFont("BookMono", 9)
        c.drawCentredString(self.width / 2, 49 * mm, ".event-card { padding: 1rem; }")
        labels = ["Selector", "Declaration block", "Property", "Value"]
        examples = [".event-card", "{ ... }", "padding", "1rem"]
        fills = [PALE_BLUE, PALE_TEAL, PALE_GOLD, WHITE]
        strokes = [BLUE, TEAL, HexColor("#B06A2F"), NAVY]
        positions, widths = self._horizontal_layout([31, 39, 29, 25], left_mm=8, right_mm=8)
        for index, (label, example, fill, stroke, x, width) in enumerate(zip(labels, examples, fills, strokes, positions, widths)):
            self._box(c, x, 27 * mm, width, 13 * mm, label, fill=fill, stroke=stroke, size=6.1)
            c.setFillColor(INK); c.setFont("BookMono", 6.4)
            c.drawCentredString(x + width / 2, 21.5 * mm, example)
            if index < len(labels) - 1:
                self._arrow(c, x + width, 33.5 * mm, positions[index + 1], 33.5 * mm, color=stroke)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        c.drawCentredString(self.width / 2, 13.5 * mm, "The selector finds candidates; each property-value declaration proposes presentation.")

    def _draw_selector_matching(self, c):
        left_x = 8 * mm
        self._box(c, left_x, 38 * mm, 56 * mm, 12 * mm, 'article class="event-card"', fill=PALE_BLUE, stroke=BLUE, size=5.7)
        self._box(c, left_x + 9 * mm, 22 * mm, 38 * mm, 10 * mm, "h3", fill=WHITE, stroke=NAVY, size=6.1)
        self._arrow(c, left_x + 28 * mm, 38 * mm, left_x + 28 * mm, 32 * mm, color=BLUE)
        rows = [
            (".event-card", "matches article", PALE_TEAL, TEAL),
            (".event-card h3", "matches h3", PALE_TEAL, TEAL),
            (".event-card .featured", "no match", PALE_GOLD, HexColor("#B06A2F")),
        ]
        right_x = 79 * mm
        for index, (selector, result, fill, stroke) in enumerate(rows):
            y = (42 - index * 13) * mm
            self._box(c, right_x, y, 50 * mm, 9 * mm, selector, fill=fill, stroke=stroke, size=5.6)
            self._box(c, right_x + 55 * mm, y, 31 * mm, 9 * mm, result, fill=WHITE, stroke=stroke, size=5.5)
            self._arrow(c, right_x + 50 * mm, y + 4.5 * mm, right_x + 55 * mm, y + 4.5 * mm, color=stroke)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.0)
        c.drawCentredString(self.width / 2, 13 * mm, "A space means descendant relationship; no space can combine conditions on one element.")

    def _draw_css_cascade(self, c):
        labels = ["Relevant", "Origin +", "Layer", "Specificity", "Scope", "Order", "Winner"]
        colors_list = [NAVY, BLUE, TEAL, HexColor("#6B5CA5"), HexColor("#8A6F40"), HexColor("#B06A2F"), HexColor("#167A55")]
        positions, widths = self._horizontal_layout([20, 22, 19, 25, 19, 19, 21], left_mm=4, right_mm=4)
        for index, (label, color, x, width) in enumerate(zip(labels, colors_list, positions, widths)):
            self._box(c, x, 30 * mm, width, 12 * mm, label, fill=WHITE if index < 5 else PALE_TEAL, stroke=color, size=6.0)
            if index < len(labels) - 1:
                self._arrow(c, x + width, 36 * mm, positions[index + 1], 36 * mm, color=color)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        c.drawCentredString(self.width / 2, 20 * mm, "Origin includes importance; scope proximity applies only after specificity ties.")
        c.drawCentredString(self.width / 2, 15 * mm, "Order of appearance decides only after every earlier dimension no longer distinguishes candidates.")

    def _draw_box_model(self, c):
        cx, cy = self.width / 2, 34 * mm
        layers = [
            (128 * mm, 34 * mm, PALE_GOLD, HexColor("#B06A2F"), "margin"),
            (104 * mm, 28 * mm, PALE_BLUE, BLUE, "border"),
            (80 * mm, 22 * mm, PALE_TEAL, TEAL, "padding"),
            (50 * mm, 14 * mm, WHITE, NAVY, "content"),
        ]
        for width, height, fill, stroke, label in layers:
            c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(0.8)
            c.rect(cx - width / 2, cy - height / 2, width, height, fill=1, stroke=1)
            c.setFillColor(INK); c.setFont("BookSans-Bold", 5.9)
            c.drawString(cx - width / 2 + 2 * mm, cy + height / 2 - 3 * mm, label)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        c.drawCentredString(self.width / 2, 13 * mm, "border-box includes content, padding, and border; margin remains outside.")

    def _draw_logical_axes(self, c):
        panels = [
            (8 * mm, "Horizontal LTR", "inline start", "inline end", False),
            (92 * mm, "Horizontal RTL", "inline start", "inline end", True),
        ]
        for x, title, start_label, end_label, reverse in panels:
            w = 69 * mm
            c.setFillColor(WHITE); c.setStrokeColor(RULE); c.roundRect(x, 18 * mm, w, 34 * mm, 2 * mm, fill=1, stroke=1)
            c.setFillColor(INK); c.setFont("BookSans-Bold", 6.5); c.drawCentredString(x + w / 2, 46 * mm, title)
            mid_y = 34 * mm
            if reverse:
                self._arrow(c, x + w - 9 * mm, mid_y, x + 9 * mm, mid_y, color=TEAL)
                c.setFont("BookSans", 5.5); c.drawString(x + w - 26 * mm, 37.5 * mm, start_label); c.drawString(x + 5 * mm, 27 * mm, end_label)
            else:
                self._arrow(c, x + 9 * mm, mid_y, x + w - 9 * mm, mid_y, color=TEAL)
                c.setFont("BookSans", 5.5); c.drawString(x + 5 * mm, 37.5 * mm, start_label); c.drawRightString(x + w - 5 * mm, 27 * mm, end_label)
            self._arrow(c, x + w / 2, 42 * mm, x + w / 2, 22 * mm, color=BLUE)
            c.setFillColor(MUTED); c.setFont("BookSans", 5.5); c.drawCentredString(x + w / 2 + 13 * mm, 23 * mm, "block flow")
        c.setFillColor(MUTED); c.setFont("BookSans", 6.0)
        c.drawCentredString(self.width / 2, 12.5 * mm, "padding-inline and margin-inline adapt when the document direction changes.")

    def _draw_layout_systems(self, c):
        c.setFillColor(INK); c.setFont("BookSans-Bold", 7)
        c.drawString(12 * mm, 46 * mm, "Flexbox")
        c.drawString(96 * mm, 46 * mm, "Grid")
        for index, width in enumerate([22, 29, 18]):
            self._box(c, (12 + sum([22, 29, 18][:index]) + index * 3) * mm, 28 * mm, width * mm, 11 * mm, f"Item {index + 1}", fill=PALE_TEAL, stroke=TEAL, size=5.8)
        for row in range(2):
            for col in range(3):
                self._box(c, (96 + col * 21) * mm, (33 - row * 12) * mm, 18 * mm, 9 * mm, f"{row + 1},{col + 1}", fill=PALE_BLUE, stroke=BLUE, size=5.7)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.1)
        c.drawString(12 * mm, 19 * mm, "one primary axis")
        c.drawString(96 * mm, 17 * mm, "coordinated rows and columns")

    def _draw_responsive_reflow(self, c):
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6.5)
        c.drawString(9 * mm, 47 * mm, "Narrow container")
        c.drawString(76 * mm, 47 * mm, "Wide container")
        c.setStrokeColor(RULE); c.setFillColor(WHITE)
        c.roundRect(9 * mm, 14 * mm, 48 * mm, 30 * mm, 2 * mm, fill=1, stroke=1)
        for row in range(3):
            self._box(c, 14 * mm, (34 - row * 8) * mm, 38 * mm, 6 * mm, f"Card {row + 1}", fill=PALE_TEAL, stroke=TEAL, size=5.5)
        c.roundRect(76 * mm, 14 * mm, self.width - 85 * mm, 30 * mm, 2 * mm, fill=1, stroke=1)
        wide_width = (self.width - 97 * mm) / 3
        for col in range(3):
            self._box(c, 81 * mm + col * (wide_width + 3 * mm), 22 * mm, wide_width, 14 * mm, f"Card {col + 1}", fill=PALE_BLUE, stroke=BLUE, size=5.5)
        self._arrow(c, 60 * mm, 29 * mm, 72 * mm, 29 * mm)

    def _draw_container_query(self, c):
        c.setFillColor(INK); c.setFont("BookSans-Bold", 6.7)
        c.drawString(8 * mm, 52 * mm, "One viewport: 1200px")
        c.setFillColor(WHITE); c.setStrokeColor(RULE); c.roundRect(8 * mm, 16 * mm, self.width - 16 * mm, 32 * mm, 2 * mm, fill=1, stroke=1)
        main_x, main_w = 14 * mm, 91 * mm
        side_x, side_w = 112 * mm, self.width - 126 * mm
        self._box(c, main_x, 35 * mm, main_w, 9 * mm, "Main container: 25rem", fill=PALE_BLUE, stroke=BLUE, size=6.0)
        self._box(c, side_x, 35 * mm, side_w, 9 * mm, "Sidebar: 15rem", fill=PALE_GOLD, stroke=HexColor("#B06A2F"), size=5.8)
        self._box(c, main_x + 5 * mm, 21 * mm, 50 * mm, 10 * mm, "Event card content", fill=PALE_TEAL, stroke=TEAL, size=5.8)
        self._box(c, main_x + 60 * mm, 21 * mm, 25 * mm, 10 * mm, "Action", fill=WHITE, stroke=TEAL, size=5.8)
        self._box(c, side_x + 5 * mm, 25 * mm, side_w - 10 * mm, 7 * mm, "Content", fill=PALE_TEAL, stroke=TEAL, size=5.5)
        self._box(c, side_x + 5 * mm, 18 * mm, side_w - 10 * mm, 5 * mm, "Action below", fill=WHITE, stroke=HexColor("#B06A2F"), size=5.0)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.0)
        c.drawCentredString(self.width / 2, 11.5 * mm, "The same component crosses its 20rem threshold only in the wider container.")

    def _draw_css_devtools_evidence(self, c):
        labels = ["Network", "Matched rule", "Cascade winner", "Computed box", "Layout overlay"]
        notes = ["CSS loaded", "selector applies", "not crossed out", "used values", "tracks + overflow"]
        colors_list = [NAVY, BLUE, TEAL, HexColor("#6B5CA5"), HexColor("#B06A2F")]
        positions, widths = self._horizontal_layout([25, 30, 31, 29, 31], left_mm=5, right_mm=5)
        for index, (label, note, stroke, x, width) in enumerate(zip(labels, notes, colors_list, positions, widths)):
            self._box(c, x, 31 * mm, width, 12 * mm, label, fill=WHITE if index < 4 else PALE_GOLD, stroke=stroke, size=5.7)
            c.setFillColor(MUTED); c.setFont("BookSans", 5.1); c.drawCentredString(x + width / 2, 25 * mm, note)
            if index < len(labels) - 1:
                self._arrow(c, x + width, 37 * mm, positions[index + 1], 37 * mm, color=stroke)
        c.setFillColor(MUTED); c.setFont("BookSans", 6.0)
        c.drawCentredString(self.width / 2, 14.5 * mm, "Stop at the first failed link in the evidence chain; do not compensate downstream.")


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: Path, **kwargs):
        super().__init__(str(filename), **kwargs)
        self._heading_counter = 0

    def beforeDocument(self) -> None:
        self._heading_counter = 0

    def afterFlowable(self, flowable: Flowable) -> None:
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in {"Heading1", "Heading2", "Heading3"}:
            return
        level = {"Heading1": 0, "Heading2": 1, "Heading3": 2}[style_name]
        text = flowable.getPlainText()
        self._heading_counter += 1
        key = f"heading-{self._heading_counter}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
        self.notify("TOCEntry", (level, text, self.page, key))


def draw_cover(canvas, doc) -> None:
    canvas.saveState()
    canvas.setTitle("Web Programming: From the Platform to Production - Revised Foundations Edition")
    canvas.setAuthor(AUTHOR)
    canvas.setSubject("University web programming course book")
    if not COVER_ART.exists():
        raise FileNotFoundError(f"Cover artwork not found: {COVER_ART}")
    artwork = ImageReader(str(COVER_ART))
    image_width, image_height = artwork.getSize()
    scale = max(PAGE_WIDTH / image_width, PAGE_HEIGHT / image_height)
    draw_width = image_width * scale
    draw_height = image_height * scale
    canvas.drawImage(
        artwork,
        (PAGE_WIDTH - draw_width) / 2,
        (PAGE_HEIGHT - draw_height) / 2,
        width=draw_width,
        height=draw_height,
        preserveAspectRatio=True,
        mask="auto",
    )
    canvas.setFillColor(HexColor("#061326"), alpha=0.30)
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    canvas.setFillColor(HexColor("#061326"), alpha=0.62)
    canvas.roundRect(17 * mm, PAGE_HEIGHT - 118 * mm, 113 * mm, 74 * mm, 4 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("BookSans-Bold", 27)
    canvas.drawString(24 * mm, PAGE_HEIGHT - 70 * mm, "WEB PROGRAMMING")
    canvas.setFillColor(HexColor("#8DE7F2"))
    canvas.setFont("BookSerif", 15)
    canvas.drawString(24 * mm, PAGE_HEIGHT - 84 * mm, "From the Platform to Production")
    canvas.setFillColor(PALE_GOLD)
    canvas.roundRect(24 * mm, PAGE_HEIGHT - 104 * mm, 57 * mm, 10 * mm, 2 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.setFont("BookSans-Bold", 8.5)
    canvas.drawCentredString(52.5 * mm, PAGE_HEIGHT - 100.5 * mm, "FOUNDATIONS EDITION")
    canvas.setFillColor(WHITE)
    canvas.setFont("BookSans-Bold", 12)
    canvas.drawString(24 * mm, 39 * mm, AUTHOR)
    canvas.setFont("BookSans", 8)
    canvas.drawString(24 * mm, 31 * mm, "Computer Engineering Program")
    canvas.drawString(24 * mm, 24 * mm, f"Technical review: {date.today().strftime('%d %B %Y')}")
    canvas.restoreState()


def draw_front_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(WHITE)
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    canvas.restoreState()


def draw_body_page(canvas, doc) -> None:
    canvas.saveState()
    page_number = canvas.getPageNumber()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 14 * mm, PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 14 * mm)
    canvas.setFont("BookSans", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(LEFT_MARGIN, PAGE_HEIGHT - 10.5 * mm, "WEB PROGRAMMING - FROM THE PLATFORM TO PRODUCTION")
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 10.5 * mm, "FOUNDATIONS EDITION")
    canvas.line(LEFT_MARGIN, 13 * mm, PAGE_WIDTH - RIGHT_MARGIN, 13 * mm)
    canvas.drawString(LEFT_MARGIN, 8.5 * mm, "Computer Engineering Program")
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 8.5 * mm, str(page_number))
    canvas.restoreState()


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(inline_markup(text), style)


def table_from_lines(lines: list[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows: list[list[Paragraph]] = []
    for index, line in enumerate(lines):
        if index == 1 and re.fullmatch(r"\s*\|?\s*:?-+.*", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append([Paragraph(inline_markup(cell), styles["small"]) for cell in cells])

    columns = len(rows[0])
    max_lengths = [
        max(len(row[column].getPlainText()) for row in rows)
        for column in range(columns)
    ]
    total = sum(max_lengths) or columns
    minimum = CONTENT_WIDTH / (columns * 1.7)
    widths = [max(minimum, CONTENT_WIDTH * length / total) for length in max_lengths]
    scale = CONTENT_WIDTH / sum(widths)
    widths = [width * scale for width in widths]

    result = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
    result.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "BookSans-Bold"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE_BLUE]),
                ("GRID", (0, 0), (-1, -1), 0.4, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return result


def consume_list(lines: list[str], start: int, styles: dict[str, ParagraphStyle]):
    ordered = bool(re.match(r"^\d+\.\s+", lines[start]))
    items: list[ListItem] = []
    index = start
    pattern = r"^\d+\.\s+(.*)" if ordered else r"^-\s+(.*)"
    while index < len(lines):
        match = re.match(pattern, lines[index])
        if not match:
            break
        text = match.group(1)
        index += 1
        while index < len(lines) and lines[index].startswith("   "):
            text += " " + lines[index].strip()
            index += 1
        items.append(ListItem(paragraph(text, styles["list"]), leftIndent=12))
    flowable = ListFlowable(
        items,
        bulletType="1" if ordered else "bullet",
        start="1" if ordered else "-",
        leftIndent=15,
        bulletFontName="BookSans",
        bulletFontSize=7.5,
        spaceAfter=6,
    )
    return flowable, index


def markdown_to_flowables(markdown: str, styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    lines = normalize_text(markdown).splitlines()
    story: list[Flowable] = []
    index = 0
    first_heading = True

    while index < len(lines):
        line = lines[index].rstrip()
        if not line.strip():
            index += 1
            continue

        figure = re.fullmatch(r"<!--\s*figure:([a-z0-9-]+)\s*-->", line.strip())
        if figure:
            kind = figure.group(1)
            if kind not in ConceptFigure.captions:
                raise ValueError(f"Unknown figure kind: {kind}")
            story.extend([ConceptFigure(kind, CONTENT_WIDTH), Spacer(1, 7)])
            index += 1
            continue

        media = re.fullmatch(r"<!--\s*(?:illustration|media):([a-z0-9-]+)\s*-->", line.strip())
        if media:
            key = media.group(1)
            if key not in MEDIA_FIGURES:
                raise ValueError(f"Unknown media figure: {key}")
            media_path, media_caption = MEDIA_FIGURES[key]
            if not media_path.exists():
                raise FileNotFoundError(f"Figure artwork not found: {media_path}")
            image_reader = ImageReader(str(media_path))
            image_width, image_height = image_reader.getSize()
            max_height = MEDIA_MAX_HEIGHT_MM.get(key, 145) * mm
            scale = min(CONTENT_WIDTH / image_width, max_height / image_height)
            rendered_width = image_width * scale
            rendered_height = image_height * scale
            image_flowable = RLImage(str(media_path), width=rendered_width, height=rendered_height)
            image_flowable.hAlign = "CENTER"
            story.extend([
                KeepTogether([
                    image_flowable,
                    Spacer(1, 2 * mm),
                    paragraph(media_caption, styles["caption"]),
                ]),
                Spacer(1, 5),
            ])
            index += 1
            continue

        table_caption = re.fullmatch(r"\*\*(Table\s+.+)\*\*", line.strip())
        if table_caption:
            story.append(paragraph(table_caption.group(1), styles["table-caption"]))
            index += 1
            continue

        if line.startswith("```"):
            language = line[3:].strip()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            index += 1
            if language == "mermaid":
                story.append(WebSequenceDiagram(CONTENT_WIDTH))
                story.append(Spacer(1, 5))
            else:
                story.append(Preformatted("\n".join(code_lines), styles["code"], maxLineLength=92))
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)", line)
        if heading:
            level = len(heading.group(1))
            text = heading.group(2)
            if level == 1 and not first_heading:
                story.extend([CondPageBreak(65 * mm), Spacer(1, 4 * mm)])
            story.append(paragraph(text, styles[f"h{level}"]))
            first_heading = False
            index += 1
            continue

        if line.startswith("> "):
            quote_lines = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(lines[index].lstrip("> "))
                index += 1
            story.append(paragraph(" ".join(quote_lines), styles["quote"]))
            continue

        if line.startswith("|") and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[index + 1]):
            table_lines = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            story.extend([table_from_lines(table_lines, styles), Spacer(1, 7)])
            continue

        if re.match(r"^(?:-\s+|\d+\.\s+)", line):
            list_flowable, index = consume_list(lines, index, styles)
            story.append(list_flowable)
            continue

        if re.fullmatch(r"-{3,}", line.strip()):
            story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=8, spaceAfter=9))
            index += 1
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines):
            next_line = lines[index].rstrip()
            if not next_line.strip():
                index += 1
                break
            if (
                next_line.startswith(("#", ">", "```", "|"))
                or re.match(r"^(?:-\s+|\d+\.\s+)", next_line)
                or re.fullmatch(r"-{3,}", next_line.strip())
            ):
                break
            paragraph_lines.append(next_line.strip())
            index += 1
        story.append(paragraph(" ".join(paragraph_lines), styles["body"]))

    return story


def author_portrait_flowables(styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    candidates = [
        AUTHOR_PHOTO,
        AUTHOR_PHOTO.with_suffix(".png"),
        AUTHOR_PHOTO.with_suffix(".jpeg"),
    ]
    portrait = next((path for path in candidates if path.exists()), None)
    if portrait is None:
        return []
    image_reader = ImageReader(str(portrait))
    image_width, image_height = image_reader.getSize()
    scale = min((48 * mm) / image_width, (62 * mm) / image_height)
    image_flowable = RLImage(
        str(portrait), width=image_width * scale, height=image_height * scale
    )
    image_flowable.hAlign = "CENTER"
    return [image_flowable, Spacer(1, 4 * mm)]


def front_matter(styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC1",
            fontName="BookSans-Bold",
            fontSize=10,
            leading=14,
            leftIndent=0,
            firstLineIndent=0,
            textColor=NAVY,
            spaceBefore=5,
        ),
        ParagraphStyle(
            "TOC2",
            fontName="BookSans",
            fontSize=8.3,
            leading=11,
            leftIndent=10,
            firstLineIndent=0,
            textColor=INK,
        ),
        ParagraphStyle(
            "TOC3",
            fontName="BookSans",
            fontSize=7.5,
            leading=10,
            leftIndent=20,
            firstLineIndent=0,
            textColor=MUTED,
        ),
    ]
    return [
        NextPageTemplate("front"),
        PageBreak(),
        Spacer(1, 18 * mm),
        paragraph("About this edition", styles["front-title"]),
        paragraph(
            "This foundations edition contains the first three completed sessions of a comprehensive university course "
            "book: how the Web works, semantic HTML and accessibility, and professional responsive CSS. It uses the "
            "final chapter format, laboratory model, worked-answer policy, and visual system that subsequent parts follow.",
            styles["body"],
        ),
        paragraph(
            "The student edition includes full answers to formative exercises and quizzes. Secure summative variants "
            "remain in a separate access-controlled instructor supplement.",
            styles["body"],
        ),
        Spacer(1, 4 * mm),
        paragraph("How to use the book", styles["front-heading"]),
        paragraph(
            "Predict before running examples, complete each laboratory checkpoint, commit your work, and attempt every "
            "exercise before reading its solution. Treat browser tools, tests, and version history as engineering evidence.",
            styles["body"],
        ),
        Spacer(1, 4 * mm),
        paragraph("Publication information", styles["front-heading"]),
        paragraph(
            f"Revised foundations edition, 28 August 2026. Author: {AUTHOR}. Copyright (c) 2026 {AUTHOR}. Distributed under the "
            "Apache License, Version 2.0; see the repository LICENSE file. The current technical baseline targets "
            "Node.js 24 LTS.",
            styles["body"],
        ),
        PageBreak(),
        paragraph("Preface", styles["front-title"]),
        paragraph(
            "The Web is often introduced as a collection of commands: write this tag, copy that style rule, install a "
            "framework, and run a server. Those commands can produce a page, but they do not yet give a student a dependable "
            "mental model. When something fails, copied steps offer little help. This book therefore begins with smaller, "
            "more human questions. What is the browser trying to do? Which program is speaking? What information crosses the "
            "network? Which part can we observe? Only then do we name the protocol, language feature, or tool that solves the problem.",
            styles["body"],
        ),
        paragraph(
            "No previous knowledge of web development is assumed. A technical term is introduced in plain language, connected "
            "to a familiar situation, and then refined until it is precise enough for engineering work. Abbreviations are expanded "
            "when they first become important. Diagrams show relationships; examples make those relationships concrete; laboratories "
            "turn explanation into evidence. Advanced material is not separated from fundamentals by a sudden jump. It grows from the "
            "same ideas at a larger scale.",
            styles["body"],
        ),
        paragraph(
            "The continuing Campus Hub project gives the course a single thread. Students first publish a small document, then make "
            "it semantic, responsive, interactive, data-driven, secure, tested, and deployable. Each addition has a reason. The aim is "
            "not merely to finish an application, but to understand what the application asks the browser, network, server, and database to do.",
            styles["body"],
        ),
        paragraph("For students", styles["front-heading"]),
        paragraph(
            "Predict before running an example. Keep a record of what you observed and what you inferred. Attempt the exercises before "
            "reading their answers, and compare reasoning rather than memorizing a final line of code. If a paragraph feels dense, return "
            "to its concrete example and explain it aloud in your own words.",
            styles["body"],
        ),
        paragraph("For instructors", styles["front-heading"]),
        paragraph(
            "Each session is organized as a teachable sequence: motivating problem, concept model, prediction, demonstration, guided "
            "laboratory, independent transfer, debugging clinic, retrieval quiz, and reflection. The explanations are detailed enough "
            "for preparation and self-study, while checkpoints provide natural places for questions, live demonstrations, and formative assessment.",
            styles["body"],
        ),
        PageBreak(),
        paragraph("About the author", styles["front-title"]),
        *author_portrait_flowables(styles),
        paragraph(AUTHOR, styles["front-heading"]),
        paragraph(
            "Dr. Mahyar Teymournezhad is the author and curriculum designer of *Web Programming: From the Platform to Production*. "
            "He developed the book as the central reference for a university computer engineering course, with one consistent path "
            "from a student's first encounter with the Web to production-oriented full-stack engineering.",
            styles["body"],
        ),
        paragraph(
            "The authoring approach places durable concepts before fashionable tools. It treats accessibility, security, testing, "
            "version control, and professional explanation as everyday engineering responsibilities rather than optional final topics. "
            "Every laboratory is designed to leave observable evidence, and every worked answer explains why a solution is appropriate, "
            "what assumptions it makes, and where a different choice may be justified.",
            styles["body"],
        ),
        NextPageTemplate("body"),
        PageBreak(),
        paragraph("Contents", styles["toc-title"]),
        toc,
        PageBreak(),
    ]


def appendix_solution(styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    story: list[Flowable] = [
        PageBreak(),
        paragraph("Appendix A - Tested laboratory reference solutions", styles["h1"]),
        paragraph(
            "These files are generated into the PDF from the same tested sources used by the repository checks. "
            "Compare it with your committed attempt only after completing the laboratory.",
            styles["body"],
        ),
    ]
    previous_week = None
    for solution_file in SOLUTION_FILES:
        week = solution_file.parent.name.replace("week-", "Week ")
        if previous_week is not None and week != previous_week:
            story.append(PageBreak())
        story.append(paragraph(f"{week} - {solution_file.name}", styles["h2"]))
        story.append(Preformatted(normalize_text(solution_file.read_text(encoding="utf-8")).rstrip(), styles["code"], maxLineLength=92))
        previous_week = week
    story.extend([
        PageBreak(),
        paragraph("Appendix B - Quick commands", styles["h1"]),
        paragraph("Run the complete repository verification:", styles["body"]),
        Preformatted("npm test", styles["code"]),
        paragraph("Serve the Week 1 starter at http://localhost:8000/:", styles["body"]),
        Preformatted("npm run serve:week01:starter", styles["code"]),
        paragraph("Build and verify this PDF edition:", styles["body"]),
        Preformatted("npm run pdf\nnpm run pdf:verify", styles["code"]),
    ])
    return story


def build() -> Path:
    if not CHAPTERS:
        raise FileNotFoundError("No chapter Markdown files were found.")
    register_fonts()
    styles = make_styles()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    body_frame = Frame(
        LEFT_MARGIN,
        BOTTOM_MARGIN,
        CONTENT_WIDTH,
        PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN,
        id="body-frame",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    full_frame = Frame(0, 0, PAGE_WIDTH, PAGE_HEIGHT, id="full-frame", showBoundary=0)
    doc = BookDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title="Web Programming: From the Platform to Production - Revised Foundations Edition",
        author=AUTHOR,
        subject="University web programming course book",
        creator="Reproducible ReportLab build pipeline",
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[full_frame], onPage=draw_cover),
            PageTemplate(id="front", frames=[body_frame], onPage=draw_front_page),
            PageTemplate(id="body", frames=[body_frame], onPage=draw_body_page),
        ]
    )

    story: list[Flowable] = [Spacer(1, 1)]
    story.extend(front_matter(styles))
    for chapter_index, chapter in enumerate(CHAPTERS):
        if chapter_index:
            story.append(PageBreak())
        story.extend(markdown_to_flowables(chapter.read_text(encoding="utf-8"), styles))
    story.extend(appendix_solution(styles))

    doc.multiBuild(story)
    return OUTPUT


if __name__ == "__main__":
    output = build()
    print(f"Created {output}")
