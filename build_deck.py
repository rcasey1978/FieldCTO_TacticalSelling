#!/usr/bin/env python3
"""
Build the Field CTO X-Arch executive deck (.pptx) from the slide outline.

Generates a 16:9 dark-theme deck: title slide, 12 condensed core slides, an
appendix divider, and 8 condensed appendix slides. Full speaker notes are
embedded in each slide's notes pane. All figures are illustrative
(see 06-financial-model.md).

Run:  python3 build_deck.py
Out:  Field-CTO-XArch-Business-Case.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---- Theme ----------------------------------------------------------------
BG = RGBColor(0x10, 0x10, 0x14)        # near-black navy
PANEL = RGBColor(0x1A, 0x1A, 0x2E)     # panel
ACCENT = RGBColor(0x00, 0xBC, 0xEB)    # Cisco cyan
ACCENT2 = RGBColor(0x00, 0xA4, 0xFD)   # blue
TEXT = RGBColor(0xF2, 0xF4, 0xF8)      # near-white
MUTED = RGBColor(0x9A, 0xA3, 0xB2)     # muted grey
FONT = "Calibri"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def _solid(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_bg(slide):
    r = slide.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)  # rectangle
    _solid(r, BG)
    r.shadow.inherit = False
    # send to back
    sp = r._element
    sp.getparent().remove(sp)
    slide.shapes._spTree.insert(2, sp)
    return r


def add_text(slide, left, top, width, height, runs, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, space_after=6):
    """runs: list of paragraphs; each paragraph is list of (text, size, color, bold)."""
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        for (text, size, color, bold) in para:
            run = p.add_run()
            run.text = text
            run.font.size = Pt(size)
            run.font.color.rgb = color
            run.font.bold = bold
            run.font.name = FONT
    return tb


def add_accent_bar(slide, top=Inches(1.25)):
    bar = slide.shapes.add_shape(1, Inches(0.6), top, Inches(1.4), Pt(4))
    _solid(bar, ACCENT)


def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def bullets_para(items, size=16, color=TEXT):
    paras = []
    for it in items:
        paras.append([(u"\u2022  ", size, ACCENT, True), (it, size, color, False)])
    return paras


prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]


def new_slide():
    s = prs.slides.add_slide(BLANK)
    add_bg(s)
    return s


def content_slide(kicker, headline, bullets, notes, footer=None):
    s = new_slide()
    add_text(s, Inches(0.6), Inches(0.45), Inches(12.1), Inches(0.4),
             [[(kicker.upper(), 12, ACCENT, True)]])
    add_accent_bar(s, Inches(0.95))
    add_text(s, Inches(0.6), Inches(1.15), Inches(12.1), Inches(1.1),
             [[(headline, 28, TEXT, True)]])
    # panel behind bullets
    panel = s.shapes.add_shape(1, Inches(0.6), Inches(2.55),
                               Inches(12.1), Inches(4.3))
    _solid(panel, PANEL)
    panel.line.color.rgb = RGBColor(0x2C, 0x2C, 0x3A)
    panel.line.width = Pt(1)
    add_text(s, Inches(1.0), Inches(2.8), Inches(11.3), Inches(3.9),
             bullets_para(bullets, size=18), space_after=12)
    add_text(s, Inches(0.6), Inches(7.02), Inches(12.1), Inches(0.35),
             [[(footer or "Illustrative figures \u2014 replace with actuals before presenting.",
                10, MUTED, False)]])
    set_notes(s, notes)
    return s


# ---- Title slide ----------------------------------------------------------
s = new_slide()
band = s.shapes.add_shape(1, 0, Inches(2.6), SLIDE_W, Inches(2.3))
_solid(band, PANEL)
add_text(s, Inches(0.8), Inches(2.75), Inches(11.7), Inches(0.5),
         [[("EXECUTIVE FUNDING DECISION", 14, ACCENT, True)]])
add_text(s, Inches(0.8), Inches(3.25), Inches(11.7), Inches(1.2),
         [[("Field CTO X-Arch Selling", 40, TEXT, True)]])
add_text(s, Inches(0.8), Inches(4.25), Inches(11.7), Inches(0.6),
         [[("Funding the motion that monetizes Cisco + Splunk", 20, MUTED, False)]])
add_text(s, Inches(0.8), Inches(6.7), Inches(11.7), Inches(0.4),
         [[("Illustrative business case \u2014 figures are parameterized placeholders.",
            11, MUTED, False)]])
set_notes(s, "Opening: We now own the most complete portfolio in the market. "
            "This deck asks leadership to fund a small, senior team whose only "
            "job is to sell it as one integrated outcome. It's a bounded, "
            "high-leverage bet with a Q3 stop gate. Keep the room focused on the "
            "decision: fund the pilot.")

# ---- Core slides (12) -----------------------------------------------------
content_slide(
    "The problem",
    "We own the most complete portfolio \u2014 and still sell it in silos",
    ["Four Cisco conversations, not one integrated outcome",
     "Speeds-and-feeds, not the outcomes buyers fund",
     "Splunk \u2194 Cisco cross-sell is under-attached",
     "SIs and competitors own the 'architecture of the deal'",
     "Cost of inaction: nine figures of influenceable pipeline left on the table"],
    "The core tension: portfolio completeness without a motion to sell it as one. "
    "Land the line: 'the customer experiences four Cisco conversations, not one.' "
    "Then make inaction concrete: the GAP between a flat renewal and an X-Arch "
    "reframe, repeated across ~50 strategic accounts a year, is recurring, not "
    "one-time. Source: 01 \u00a71 (problem + cost-of-inaction box).")

content_slide(
    "Why now",
    "The post-Splunk window is open \u2014 and closing",
    ["One vendor, edge to SOC",
     "Live integrations: XDR+ES, ThousandEyes+AppD+Splunk, Cyber Vision+OT",
     "Vendor consolidation invites a C-suite frame",
     "AI build-outs pull networking, security, and data forward together"],
    "Urgency without hype. The integrations are real and fresh; consolidation and "
    "AI builds create cross-architecture entry points right now. First mover on the "
    "motion compounds. Source: 01 \u00a72.")

content_slide(
    "The differentiator",
    "One vendor, edge to SOC \u2014 but only if someone tells it end-to-end",
    ["The loop: sense \u2192 connect \u2192 secure \u2192 understand \u2192 act",
     "Every arrow between architectures is a cross-sell",
     "Most sellers own one box; the Field CTO owns the arrows",
     "Splunk \u2194 Cisco attach is the top under-executed play"],
    "The story competitors can't match end-to-end. Walk the loop once, slowly, and "
    "point at the arrows \u2014 that's where the incremental value lives. Source: 02 \u00a72.")

content_slide(
    "The solution",
    "A thin, senior Field CTO seller group that leads across architectures",
    ["Owns the CxO conversation (risk, resilience, cost)",
     "Architects across BUs; specialists detail and close",
     "Leads with vertical credibility (NIS2, DORA, HIPAA, NERC-CIP)",
     "Orchestrates \u2014 NOT another product-overlay SE team"],
    "Define the role crisply and pre-empt the 'another overlay team' objection: "
    "this is leverage that makes existing teams MORE productive. Thin, senior, "
    "orchestration-first. Source: 01 \u00a73; 03 \u00a71.")

content_slide(
    "Extending the model",
    "Black Ops: an elite tiger team for the accounts nobody can crack",
    ["The group runs the marathon; Black Ops is the breakthrough",
     "Parachutes into stalled / SI-locked / narrow-window whales",
     "Focused ~60\u2013120-day mission that IGNITES DURABLE GROWTH, then hands back",
     "Fully ethical; OT-safety and read-only guardrails still apply"],
    "A mode, not separate headcount. Two things to stress: the mission is focused "
    "but the point is durable, multi-year growth for Cisco (it always hands the "
    "account back \u2014 no hoarding), and 'Black Ops' is a special-forces posture "
    "metaphor \u2014 fully ethical, nothing hidden from the customer. Source: 09.")

content_slide(
    "Focus",
    "Three high-attach architectures, four high-pull verticals",
    ["Secure Networking \u00b7 Observability & Data \u00b7 Resilience & SecOps",
     "(+1) AI-Ready Infrastructure as a pull-through adjacency",
     "Transportation & Logistics \u00b7 Financial Services",
     "Healthcare \u00b7 Public Sector / Critical Infrastructure",
     "Chosen for cross-attach + regulatory pull; the list is swappable"],
    "We deliberately don't boil the ocean: three anchor pillars with the clearest "
    "boardroom narrative, plus AI-ready infra as adjacency. Four verticals chosen "
    "for high cross-attach, regulatory/resilience pull, and joint Cisco+Splunk "
    "strength \u2014 swappable without changing the operating design. Source: 02 \u00a74\u20135; "
    "04 master matrix.")

content_slide(
    "The motion",
    "A repeatable lifecycle and a library of plays \u2014 not heroics",
    ["Select \u2192 Frame \u2192 Architect \u2192 Value \u2192 Close \u2192 Expand",
     "Plays: Splunk-attach, SOC modernization, full-stack DX, passive OT, consolidation TCO",
     "Each play = discovery script + reference architecture + value case + proof"],
    "Show this is systematized, not dependent on a few heroes. The play library "
    "codifies the knowledge so the motion scales and survives key-person risk. "
    "Source: 05 \u00a71\u20132.")

content_slide(
    "Worked example \u00b7 aviation",
    "Airport operator: Black Ops broke open a stalled 'smart airport' program",
    ["OT-heavy hub + NIS2 + a Terminal 4 build",
     "SI about to lock the architecture \u2014 pod convened",
     "Reframed as board-level operational resilience",
     "One X-Arch architecture: passive OT + segmentation + SD-WAN + SOC + edge AI",
     "Won OT trust (read-only), then handed back to scale"],
    "The end-to-end proof. Walk the transformation: stalled + SI-locked \u2192 executive "
    "breakthrough \u2192 one co-authored architecture \u2192 multi-year program. Stress the OT "
    "safety boundary as the trust-winner with airport engineering. Source: 10.")

content_slide(
    "The return",
    "~$180M influenced pipeline, ~$60M bookings, payback < 12 months",
    ["Year-1 (illustrative): ~$180M influenced pipeline",
     "~$60M incremental bookings \u2192 ~$36M incremental gross margin",
     "Break-even ~$9M bookings \u2014 roughly FIVE deals cover the whole cost",
     "Profitable across scenarios: ~$25M / $60M / $90M \u2192 ~$9M / $31M / $46M net"],
    "The money slide. Anchor on break-even (~$9M bookings, about five deals, covers "
    "the entire $5.4M cost); everything above is upside. All three scenarios clear "
    "break-even \u2014 the question is pace, not payback. Illustrative and parameterized. "
    "Source: 01 \u00a76; 06 \u00a72\u20133, \u00a75.")

content_slide(
    "The ask",
    "Fund a 12-person, 4-quarter pilot (~$5.4M illustrative)",
    ["8 Field CTOs + 1 group lead + 2 X-Arch architects + 1 deal desk/ops",
     "~$5.4M/yr fully loaded (enablement, tooling, travel)",
     "Internal-first staffing; ~40\u201360 named accounts with paired controls",
     "Q3 go/expand/stop gate tied to explicit success criteria"],
    "State the ask plainly and immediately bound the downside: small, senior team; "
    "defined spend; a real stop gate at Q3. Ask for the decision. Source: 01 \u00a75; "
    "06 \u00a71.")

content_slide(
    "Bounded risk + proof",
    "A Q3 gate and control-account measurement make this low-risk",
    ["Q3 go/expand/stop gate stops spend before it turns negative",
     "Matched control accounts prove attach, deal-size, win-rate deltas",
     "Top risks (talent, comp friction, attribution) have concrete mitigations",
     "Influence ledger prevents over-claiming and BU disputes"],
    "Address the skeptic. We measure with control accounts, so influence is proven "
    "not asserted; and we can stop at Q3 if the deltas aren't there. Source: 07 "
    "\u00a71\u20133; 05 \u00a77.")

content_slide(
    "Recommendation",
    "Approve the pilot; first executive framings within 90 days",
    ["Approve the 12-person, 4-quarter pilot with a Q3 gate",
     "+30d: group lead named; charter, comp, metrics baselined",
     "+60d: cohort staffed (internal-first); accounts + controls selected",
     "+90d: first X-Arch opportunities framed; enablement underway"],
    "Close with a clear call to action and a concrete near-term timeline so "
    "approval feels actionable, not open-ended. Restate: bounded downside, "
    "differentiated upside. Ask for the yes. Source: 01 \u00a79; README one-screen summary.")

# ---- Appendix divider -----------------------------------------------------
s = new_slide()
add_text(s, Inches(0.8), Inches(3.0), Inches(11.7), Inches(1.0),
         [[("APPENDIX", 16, ACCENT, True)]])
add_text(s, Inches(0.8), Inches(3.5), Inches(11.7), Inches(1.0),
         [[("Detail held in reserve for Q&A", 30, TEXT, True)]])
set_notes(s, "Use these only if the room asks. Don't present them by default.")

APPX = [
    ("Appendix \u00b7 A1", "Role, competencies, and skills matrix",
     ["Four pillars: business fluency, X-arch depth, exec presence, orchestration",
      "Deep in \u22652 pillars; conversant in all",
      "Deep in one vertical; team covers all four"],
     "Detail for HR/org-design questions. Source: 03 \u00a71\u20133."),
    ("Appendix \u00b7 A2", "Org placement and RACI",
     ["GTM-primary; strong dotted line to CTO/engineering",
      "Revenue-accountable AND cross-BU neutral",
      "Field CTO owns the frame; AE owns the account"],
     "For 'where does it sit / who owns what' questions. Source: 03 \u00a75, \u00a78."),
    ("Appendix \u00b7 A3", "Per-vertical field engagement kits",
     ["Buyers, discovery questions, outcome hypotheses, objections",
      "One kit per vertical (x4)",
      "Strategy \u2192 field-ready playbook"],
     "For 'how do we actually sell this' questions. Source: 04 \u00a71\u20134."),
    ("Appendix \u00b7 A4", "OT safety boundary",
     ["Read-only / passive acquisition for safety signals",
      "Never write config to PLC/HMI/DCS/RTU/SIS",
      "A hard guardrail AND a trust-winning differentiator"],
     "For OT/operations stakeholders. Source: 04 OT safety boundary."),
    ("Appendix \u00b7 A5", "Assumptions register and 3-year P&L",
     ["Every input (A1\u2013A13) is visible and editable",
      "3-year scale path with improving ROI",
      "Structure holds; only inputs change"],
     "For finance deep-dives. Source: 06 \u00a70, \u00a74."),
    ("Appendix \u00b7 A6", "Compensation design",
     ["Influence credit is additive \u2014 BUs keep 100%",
      "50% bookings / 20% Splunk attach / 15% leading / 15% MBOs",
      "Deal desk arbitrates via the influence ledger"],
     "For comp/quota questions. Source: 05 \u00a76."),
    ("Appendix \u00b7 A7", "Competitive framing",
     ["Point vendors, SIEM/observability, SIs, hyperscalers",
      "The SI dynamic is the biggest structural risk",
      "Whoever frames the architecture wins the budget"],
     "For competitive/positioning questions. Source: 02 \u00a77."),
    ("Appendix \u00b7 A8", "Full risk register and early-warning indicators",
     ["12 risks: likelihood, impact, mitigation, owner",
      "Leading signals with explicit action triggers",
      "Bounded downside via the Q3 gate"],
     "For risk/governance questions. Source: 07 \u00a73."),
]
for kicker, headline, bullets, notes in APPX:
    content_slide(kicker, headline, bullets, notes,
                  footer="Appendix \u2014 reserve for Q&A. Illustrative figures.")

prs.save("Field-CTO-XArch-Business-Case.pptx")
print("Wrote Field-CTO-XArch-Business-Case.pptx with", len(prs.slides._sldIdLst), "slides")
