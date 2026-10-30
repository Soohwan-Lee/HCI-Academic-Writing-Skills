"""Build original, self-contained SVG explanations for the bilingual README."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[2]
COPY = {
    'en': [
        ('Section', 'Give the argument a purpose.', 'What must the reader understand here?'),
        ('Subsection', 'Order the questions.', 'What needs to be explained first?'),
        ('Paragraph', 'Develop one meaningful step.', 'What claim, evidence or interpretation advances?'),
        ('Sentence', 'Connect each inference.', 'What carries forward, and what is new?'),
    ],
    'ko': [
        ('섹션', '논증에서 맡을 역할을 정합니다.', '독자가 여기서 무엇을 이해해야 할까요?'),
        ('하위섹션', '질문의 순서를 설계합니다.', '무엇을 먼저 설명해야 할까요?'),
        ('문단', '논증을 한 단계 발전시킵니다.', '어떤 주장·근거·해석을 더할까요?'),
        ('문장', '추론과 추론을 연결합니다.', '무엇을 이어받고, 무엇을 새로 더할까요?'),
    ],
}
for lang, entries in COPY.items():
    for mobile in (False, True):
        width, height = (440, 754) if mobile else (1000, 444)
        title = 'From argument to prose' if lang == 'en' else '논증의 구조에서 문장의 흐름까지'
        subtitle = 'FOUR LEVELS OF WRITING' if lang == 'en' else '글을 설계하는 네 가지 수준'
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
               f'<title id="title">{escape(title)}</title>',
               '<desc id="desc">'+escape(' → '.join(x[0]+': '+x[2] for x in entries))+'</desc>',
               '<defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.65" fill="#ddd8cc"/></pattern></defs>',
               f'<rect width="{width}" height="{height}" rx="20" fill="#f7f5ef"/>',
               f'<rect width="{width}" height="{height}" rx="20" fill="url(#dots)"/>',
               '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,Apple SD Gothic Neo,Malgun Gothic,sans-serif">',
               f'<text x="28" y="35" font-size="11" font-weight="700" letter-spacing="2" fill="#65736d">{subtitle}</text>',
               f'<text x="28" y="70" font-size="{24 if mobile else 28}" font-weight="700" fill="#173f3c">{title}</text>']
        for i,(label,lead,question) in enumerate(entries):
            x = 20 if mobile else 24+(i%2)*488
            y = 94+i*157 if mobile else 96+(i//2)*164
            w = 400 if mobile else 464
            out += [f'<g transform="translate({x},{y})">',
                    f'<rect width="{w}" height="144" rx="12" fill="{("#173f3c" if i==3 else "#ffffff")}" stroke="{("#173f3c" if i==3 else "#dddcd4")}"/>',
                    '<rect x="18" y="18" width="32" height="26" rx="6" fill="#b75b3e"/>',
                    f'<text x="34" y="36" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">0{i+1}</text>',
                    f'<text x="62" y="39" font-size="22" font-weight="700" fill="{("#ffffff" if i==3 else "#173f3c")}">{escape(label)}</text>',
                    f'<text x="20" y="81" font-size="17" font-weight="600" fill="{("#ffffff" if i==3 else "#263c38")}">{escape(lead)}</text>',
                    f'<text x="20" y="112" font-size="{14 if mobile else 15}" fill="{("#cdded7" if i==3 else "#5a6963")}">{escape(question)}</text>',
                    '</g>']
        out+=['</g></svg>']
        suffix = '-mobile' if mobile else ''
        (ROOT / f'assets/writing-levels-{lang}{suffix}.svg').write_text('\n'.join(out)+'\n')
