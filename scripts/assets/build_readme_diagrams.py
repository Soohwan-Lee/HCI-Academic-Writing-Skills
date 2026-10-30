"""Build original, self-contained SVG explanations for the bilingual README."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SPEC = {
    "en": {
        "kicker": "HOW THE SKILL PLANS A MANUSCRIPT",
        "title_desktop": "Separate the contribution, then connect four levels of prose",
        "title_mobile": "From contribution to connected prose",
        "anchor_tag": "ANCHOR",
        "anchor_title": "Contribution first",
        "anchor_lines": (
            "Separate what the paper adds",
            "from four independent choices:",
        ),
        "anchor_mobile_lead": "Kept distinct from method · topic · venue · format",
        "axes": ("Method", "Topic", "Venue", "Format"),
        "anchor_note_lines": (
            "Same method or venue can",
            "need a different structure.",
        ),
        "anchor_mobile_note": "Same method or venue can need a different structure.",
        "desc_prefix": (
            "Separate contribution from method, topic, venue and format; then plan "
        ),
        "levels": [
            (
                "Section",
                "Give the argument a purpose.",
                "What must the reader understand here?",
            ),
            (
                "Subsection",
                "Order the questions.",
                "What needs to be explained first?",
            ),
            (
                "Paragraph",
                "Develop one meaningful step.",
                "What claim, evidence or interpretation advances?",
            ),
            (
                "Sentence",
                "Connect each inference.",
                "What carries forward, and what is new?",
            ),
        ],
    },
    "ko": {
        "kicker": "논문을 설계하는 방식",
        "title_desktop": "기여를 먼저 구분하고, 네 수준을 연결해 설계합니다",
        "title_mobile": "기여 구분부터 문장 연결까지",
        "anchor_tag": "출발점",
        "anchor_title": "기여를 먼저 구분",
        "anchor_lines": (
            "논문이 더하는 새로운 지식을",
            "네 가지 요소와 분리해 파악합니다.",
        ),
        "anchor_mobile_lead": "연구 방법 · 주제 · 제출 학회 · 원고 형식과 분리해 파악",
        "axes": ("연구 방법", "주제", "제출 학회", "원고 형식"),
        "anchor_note_lines": (
            "같은 방법·학회라도 기여가 다르면",
            "논증의 구조가 달라집니다.",
        ),
        "anchor_mobile_note": "같은 방법·학회라도 기여가 다르면 구조가 달라집니다.",
        "desc_prefix": "기여를 연구 방법·주제·학회·원고 형식과 구분한 뒤 연결해 설계: ",
        "levels": [
            (
                "섹션",
                "논증에서 맡을 역할을 정합니다.",
                "독자가 여기서 무엇을 이해해야 할까요?",
            ),
            (
                "하위섹션",
                "질문의 순서를 설계합니다.",
                "무엇을 먼저 설명해야 할까요?",
            ),
            (
                "문단",
                "논증을 한 단계 발전시킵니다.",
                "어떤 주장·근거·해석을 더할까요?",
            ),
            (
                "문장",
                "추론과 추론을 연결합니다.",
                "무엇을 이어받고, 무엇을 새로 더할까요?",
            ),
        ],
    },
}

FONT_STACK = (
    "-apple-system,BlinkMacSystemFont,Segoe UI,Arial,"
    "Apple SD Gothic Neo,Malgun Gothic,sans-serif"
)


def build_desktop(cfg: dict) -> str:
    width, height = 1000, 408
    title = cfg["title_desktop"]
    desc = cfg["desc_prefix"] + " → ".join(
        f"{label}: {question}" for label, _, question in cfg["levels"]
    )
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(desc)}</desc>',
        "<defs>"
        '<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">'
        '<circle cx="1" cy="1" r="0.65" fill="#dfd9cd"/>'
        "</pattern>"
        "</defs>",
        f'<rect x="0.75" y="0.75" width="{width - 1.5}" height="{height - 1.5}" '
        'rx="20" fill="#f7f5ef" stroke="#dedad0" stroke-width="1.5"/>',
        f'<rect x="1.5" y="1.5" width="{width - 3}" height="{height - 3}" '
        'rx="19" fill="url(#dots)"/>',
        f'<g font-family="{FONT_STACK}">',
        f'<text x="28" y="34" font-size="11" font-weight="700" letter-spacing="1.8" '
        f'fill="#65736d">{escape(cfg["kicker"])}</text>',
        f'<text x="28" y="66" font-size="25" font-weight="700" '
        f'fill="#173f3c">{escape(title)}</text>',
    ]

    # Left anchor card: Contribution separated from method/topic/venue/format.
    ax, ay, aw, ah = 28, 92, 252, 292
    out += [
        f'<g transform="translate({ax},{ay})">',
        f'<rect width="{aw}" height="{ah}" rx="14" fill="#173f3c"/>',
        '<rect x="20" y="20" width="64" height="22" rx="5" fill="#255450"/>',
        f'<text x="52" y="35" text-anchor="middle" font-size="10.5" '
        f'font-weight="700" letter-spacing="1.2" fill="#cfe0da">'
        f'{escape(cfg["anchor_tag"])}</text>',
        f'<text x="20" y="72" font-size="21" font-weight="700" fill="#ffffff">'
        f'{escape(cfg["anchor_title"])}</text>',
        f'<text x="20" y="100" font-size="13.5" fill="#cde0da">'
        f'{escape(cfg["anchor_lines"][0])}</text>',
        f'<text x="20" y="119" font-size="13.5" fill="#cde0da">'
        f'{escape(cfg["anchor_lines"][1])}</text>',
    ]
    for idx, axis in enumerate(cfg["axes"]):
        px = 20 + (idx % 2) * 108
        py = 138 + (idx // 2) * 38
        out += [
            f'<rect x="{px}" y="{py}" width="100" height="30" rx="7" '
            'fill="#204d49" stroke="#366a65"/>',
            f'<text x="{px + 50}" y="{py + 20}" text-anchor="middle" '
            f'font-size="12.5" font-weight="600" fill="#e6f0ec">'
            f"{escape(axis)}</text>",
        ]
    out += [
        '<line x1="20" y1="228" x2="232" y2="228" stroke="#2c5b56"/>',
        '<circle cx="26" cy="249" r="3.5" fill="#d27759"/>',
        f'<text x="36" y="253" font-size="12.5" fill="#ebd6cc">'
        f'{escape(cfg["anchor_note_lines"][0])}</text>',
        f'<text x="36" y="272" font-size="12.5" fill="#ebd6cc">'
        f'{escape(cfg["anchor_note_lines"][1])}</text>',
        "</g>",
    ]

    # Connector from anchor card into level 01, plus stepped telescoping elbows.
    row_h, gap = 64, 12
    base_x, right_edge = 316, 972
    step = 22
    first_mid_y = ay + row_h // 2
    out += [
        f'<line x1="{ax + aw}" y1="{first_mid_y}" x2="{base_x - 2}" '
        f'y2="{first_mid_y}" stroke="#b75b3e" stroke-width="2"/>',
        f'<circle cx="{ax + aw}" cy="{first_mid_y}" r="3.5" fill="#b75b3e"/>',
        f'<polygon points="{base_x},{first_mid_y} {base_x - 7},{first_mid_y - 4.5} '
        f'{base_x - 7},{first_mid_y + 4.5}" fill="#b75b3e"/>',
    ]

    for i, (label, lead, question) in enumerate(cfg["levels"]):
        rx = base_x + i * step
        ry = ay + i * (row_h + gap)
        rw = right_edge - rx
        if i > 0:
            prev_x = base_x + (i - 1) * step
            prev_bottom = ay + (i - 1) * (row_h + gap) + row_h
            elbow_x = prev_x + 11
            mid_y = ry + row_h // 2
            out += [
                f'<path d="M{elbow_x} {prev_bottom} V{mid_y} H{rx - 3}" '
                'fill="none" stroke="#b75b3e" stroke-width="1.8" '
                'stroke-linejoin="round"/>',
                f'<polygon points="{rx},{mid_y} {rx - 6.5},{mid_y - 4} '
                f'{rx - 6.5},{mid_y + 4}" fill="#b75b3e"/>',
            ]
        out += [
            f'<g transform="translate({rx},{ry})">',
            f'<rect width="{rw}" height="{row_h}" rx="10" fill="#ffffff" '
            'stroke="#dcd9cf"/>',
            '<rect x="16" y="19" width="32" height="26" rx="6" fill="#b75b3e"/>',
            f'<text x="32" y="36" text-anchor="middle" font-size="12" '
            f'font-weight="700" fill="#ffffff">0{i + 1}</text>',
            f'<text x="60" y="39" font-size="19" font-weight="700" '
            f'fill="#173f3c">{escape(label)}</text>',
            '<line x1="184" y1="14" x2="184" y2="50" stroke="#e5e2d8"/>',
            f'<text x="202" y="27" font-size="15.5" font-weight="600" '
            f'fill="#223835">{escape(lead)}</text>',
            f'<text x="202" y="48" font-size="13.5" fill="#5a6963">'
            f"{escape(question)}</text>",
            "</g>",
        ]

    out.append("</g></svg>")
    return "\n".join(out) + "\n"


def build_mobile(cfg: dict) -> str:
    width, height = 440, 704
    title = cfg["title_mobile"]
    desc = cfg["desc_prefix"] + " → ".join(
        f"{label}: {question}" for label, _, question in cfg["levels"]
    )
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(desc)}</desc>',
        "<defs>"
        '<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">'
        '<circle cx="1" cy="1" r="0.65" fill="#dfd9cd"/>'
        "</pattern>"
        "</defs>",
        f'<rect x="0.75" y="0.75" width="{width - 1.5}" height="{height - 1.5}" '
        'rx="20" fill="#f7f5ef" stroke="#dedad0" stroke-width="1.5"/>',
        f'<rect x="1.5" y="1.5" width="{width - 3}" height="{height - 3}" '
        'rx="19" fill="url(#dots)"/>',
        f'<g font-family="{FONT_STACK}">',
        f'<text x="22" y="33" font-size="10.5" font-weight="700" '
        f'letter-spacing="1.6" fill="#65736d">{escape(cfg["kicker"])}</text>',
        f'<text x="22" y="61" font-size="22" font-weight="700" '
        f'fill="#173f3c">{escape(title)}</text>',
    ]

    # Top anchor card on mobile.
    ax, ay, aw, ah = 20, 80, 400, 108
    out += [
        f'<g transform="translate({ax},{ay})">',
        f'<rect width="{aw}" height="{ah}" rx="12" fill="#173f3c"/>',
        f'<text x="18" y="31" font-size="18" font-weight="700" fill="#ffffff">'
        f'{escape(cfg["anchor_title"])}</text>',
        '<rect x="320" y="14" width="62" height="21" rx="5" fill="#255450"/>',
        f'<text x="351" y="28" text-anchor="middle" font-size="10" '
        f'font-weight="700" letter-spacing="1.1" fill="#cfe0da">'
        f'{escape(cfg["anchor_tag"])}</text>',
        f'<text x="18" y="56" font-size="13" fill="#cde0da">'
        f'{escape(cfg["anchor_mobile_lead"])}</text>',
        '<line x1="18" y1="71" x2="382" y2="71" stroke="#2c5b56"/>',
        '<circle cx="23" cy="89" r="3" fill="#d27759"/>',
        f'<text x="32" y="93" font-size="12.5" fill="#ebd6cc">'
        f'{escape(cfg["anchor_mobile_note"])}</text>',
        "</g>",
    ]

    # Connector into level 01 and stepped cards below.
    first_y = 206
    out += [
        f'<line x1="42" y1="{ay + ah}" x2="42" y2="{first_y - 2}" '
        'stroke="#b75b3e" stroke-width="2"/>',
        f'<polygon points="42,{first_y} 37.5,{first_y - 7} 46.5,{first_y - 7}" '
        'fill="#b75b3e"/>',
    ]

    card_h, gap, step = 110, 12, 18
    right_edge = 420
    for i, (label, lead, question) in enumerate(cfg["levels"]):
        rx = 20 + i * step
        ry = first_y + i * (card_h + gap)
        rw = right_edge - rx
        if i > 0:
            prev_x = 20 + (i - 1) * step
            prev_bottom = first_y + (i - 1) * (card_h + gap) + card_h
            elbow_x = prev_x + 9
            mid_y = ry + card_h // 2
            out += [
                f'<path d="M{elbow_x} {prev_bottom} V{mid_y} H{rx - 3}" '
                'fill="none" stroke="#b75b3e" stroke-width="1.8" '
                'stroke-linejoin="round"/>',
                f'<polygon points="{rx},{mid_y} {rx - 6},{mid_y - 3.8} '
                f'{rx - 6},{mid_y + 3.8}" fill="#b75b3e"/>',
            ]
        out += [
            f'<g transform="translate({rx},{ry})">',
            f'<rect width="{rw}" height="{card_h}" rx="9" fill="#ffffff" '
            'stroke="#dcd9cf"/>',
            '<rect x="16" y="15" width="30" height="24" rx="6" fill="#b75b3e"/>',
            f'<text x="31" y="31" text-anchor="middle" font-size="11.5" '
            f'font-weight="700" fill="#ffffff">0{i + 1}</text>',
            f'<text x="56" y="34" font-size="18.5" font-weight="700" '
            f'fill="#173f3c">{escape(label)}</text>',
            f'<text x="16" y="66" font-size="15" font-weight="600" '
            f'fill="#223835">{escape(lead)}</text>',
            f'<text x="16" y="90" font-size="13" fill="#5a6963">'
            f"{escape(question)}</text>",
            "</g>",
        ]

    out.append("</g></svg>")
    return "\n".join(out) + "\n"


def main() -> None:
    for lang, cfg in SPEC.items():
        (ROOT / f"assets/writing-levels-{lang}.svg").write_text(build_desktop(cfg))
        (ROOT / f"assets/writing-levels-{lang}-mobile.svg").write_text(
            build_mobile(cfg)
        )


if __name__ == "__main__":
    main()
