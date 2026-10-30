<p align="left"><img src="assets/logo.svg" width="64" alt="근거의 흐름이 원고 페이지로 이어지는 로고"></p>

# HCI Academic Writing Skills

**연구 근거를 설득력 있는 HCI 논문의 논증으로 연결합니다.**

기존 ACM LaTeX 프로젝트의 `.tex` 파일을 직접 수정하는 AI 에이전트용 라이팅
스킬입니다. 논문의 기여를 정리하고, 관련 연구를 종합하며, 문단과 문장의 흐름을
다듬되 주장에 필요한 근거와 범위를 유지하도록 돕습니다.

[English](README.md) · [설치](docs/COMPATIBILITY.md) · [스킬](skills/hci-academic-writing/SKILL.md) · [107편 분석](research/CORPUS.md) · [작업 기록](docs/REVIEW-LOG.md)

![논문 페이지와 사람의 상호작용, 연결된 근거를 표현한 장식 일러스트](assets/editorial-cover.png)

## 기여에 맞게 작성하기

CHI, CSCW, UIST, DIS, IUI 안에도 서로 다른 연구가 존재합니다. 학회명만으로
글의 구조를 정하지 않고, 기여를 먼저 판단한 뒤 방법·독자·논문 형식에 맞춥니다.

| 기여 유형 | 주요 라이팅 과제 |
|---|---|
| 정량적 발견 | 구성개념, 비교, 분석 단위, 불확실성과 추론 범위 |
| 정성적 이해 | 맥락 속 경험, 해석, 성찰성과 분석적 기여 |
| 시스템·인터랙션 기법 | 새로운 기능, 작동 원리, 평가 질문과 실패 조건 |
| 디자인·Research through Design | 제작, 물성과의 만남, 성찰과 디자인 지식 |
| 개념·이론 | 전제, 구분, 설명력과 적용 한계 |
| 방법·도구 | 절차, 근거, 타당성과 사용 조건 |
| 데이터셋·리소스 | 출처, 구축, 특성, 재사용과 관리 |
| 리뷰·문헌 종합 | 선정 과정, 코딩 단위, 종합과 리뷰 유형별 요건 |

복합 기여에는 여러 경로를 함께 적용합니다. Pictorial은 시각적 논증과 읽기 경로를
유지합니다. 공통 모듈은 abstract, introduction, 연구 공백을 중심으로 한 related
work, 문단의 역할, 문장 간 연결, discussion, 압축, 리뷰어 응답을 다룹니다.
8,000단어 배분표는 **편집용 출발점**이며 측정으로 입증된 표준이 아닙니다.

## 논문 프로젝트에 설치하기

저장소를 복제하고 저장소 루트에서 실행합니다. 설치에는 Python 3.9 이상이 필요합니다.
`/path/to/paper`는 기존 논문 프로젝트 경로로 바꾸세요.

```sh
git clone https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills.git
cd HCI-Academic-Writing-Skills

# 미리보기: 파일을 생성하지 않습니다.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper

# 전체 스킬 폴더를 복사합니다.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper --apply
```

Claude Code는 `--host claude-code`, Antigravity는 사용 환경에 맞게
`--host antigravity-app`, `antigravity-ide`, `antigravity-cli`를 선택합니다.
설치기는 내용이 다른 기존 파일을 덮어쓰지 않습니다. 업데이트할 때는 이전 설치본을
검토하고 옮긴 뒤 설치하세요. 전역 설정은 변경하지 않습니다.
[개인용 설치·호스트별 경로·호환성 근거](docs/COMPATIBILITY.md)를 참고하세요.

논문 폴더에서 새 에이전트 세션을 열고 `hci-academic-writing` 사용을 명시적으로
요청하세요. 해당 `SKILL.md`를 읽는지 확인하는 것이 좋습니다. 핵심 스킬은 독립적으로
사용할 수 있고, 연결된 공개 논문 분석은 필요할 때 추가로 읽습니다. Codex와
Antigravity는 문서상 경로·형식 및 설치를 확인했으며, 실제 편집은 Claude Code에서
검증했습니다. 자동 탐색 여부는 아직 검증하지 않았습니다.

## 실제 작업으로 시작하기

수정 범위와 필요한 연구 근거를 함께 제공하세요. 예를 들면:

> hci-academic-writing을 사용해줘. 루트는 chi26.tex야.
> sections/related-work.tex를 저자별 나열에서 미해결 문제 중심의 논증으로
> 다듬어줘. 기존 주장과 인용의 연결은 유지하고, 문단 간 흐름과 문장 연결을
> 개선해줘. 실질적으로 근거가 부족한 부분만 표시해줘.

> 이 집단 의사결정 논문의 시스템 기여와 집단 수준의 발견을 구분해서 개요를
> 만들어줘. 제공한 결과를 사용하고, 집단 결과를 개인 판단의 개선으로 바꾸지 마.

> 가정용 오브제를 다룬 디자인 연구야. 제작과 성찰이 어떤 디자인 지식으로
> 이어지는지 정리해줘. 모호함과 상반된 해석은 유지하고 효과 검증을 만들어내지 마.

> 결과 문단을 150단어로 압축해줘. 효과 추정치, 불확실성, 유의하지 않은 결과,
> 분석 단위를 유지하고 기존 .tex를 수정해줘. 단어 집계 기준과 주요 변경을 알려줘.

프로젝트 구조, 매크로, BibTeX 키, label과 무관한 수정은 보존하는 흐름입니다.
읽기 전용 LaTeX 검사기는 정적 의존성을 확인하며, 실제 컴파일에는 TeX 환경이
필요합니다. Overleaf 업로드와 제출은 별도 작업입니다. ACM 템플릿 자체를
포함하거나 대체하지 않습니다.

## 확인할 수 있는 근거

**전문 기반 분석 107편:** CHI 34편, CSCW 21편, UIST 15편, DIS 18편,
IUI 17편으로 요청한 5개 학회 105편이며, COMPASS와 Findings of EMNLP 각 1편이
보충 사례입니다. 수상작, 주요 연구 흐름과 방법론적 대조 사례를 포함합니다.
수상 여부는 별도로 확인하며, 저자·랩의 명성을 라이팅 규칙의 근거로 삼지 않습니다.

협업, 인간–AI 상호작용, 반대 의견과 성찰뿐 아니라 접근성, 프라이버시, 돌봄,
교육, 공예, 신체적 인터랙션과 사회적 맥락의 연구를 함께 다룹니다. 목적 표집한
교육용 사례집이며 대표 표본은 아닙니다. 시스템 논문의 비중이 높고, 일부 경로는
추가 확충이 필요합니다.

- [논문 목록·출처](research/CORPUS.md) · [분포와 한계](research/COVERAGE-AUDIT.md)
- [논문 간 종합](research/SYNTHESIS.md) · [스킬용 근거 인덱스](skills/hci-academic-writing/references/corpus-index.md)
- [길이 측정](research/measurements/README.md): 본문·섹션 7편, 선택 문단 32개/14편
- [계획](docs/PLAN.md) · [표집 결정](docs/SAMPLING-PLAN.md) · [단계별 검토](docs/REVIEW-LOG.md)

분석은 AI 에이전트가 작성하고 통합 과정에서 검토했습니다. 독립적인 사람 코더의
검증은 수행하지 않았습니다. 길이를 수치로 측정한 범위는 위 부분집합이며,
보편적인 적정 문단 길이나 섹션 비율을 주장하지 않습니다.

## 검증 결과와 한계

설치·LaTeX 검사기 자동 테스트 18개가 통과했습니다. 기록된 로컬 원문 버전으로
길이 측정을 재현했습니다. 실제 Claude Code 편집 2건에서는 설치된 스킬을 읽고,
무관한 파일과 제공된 근거를 보존했으며 ACM LaTeX 컴파일도 통과했습니다.
[파일 편집 검증 기록](tests/behavior/README.md)에 환경과 범위를 명시했습니다.

생성 실험에서는 지침을 제공했어도 관찰 기간, 코딩 단위, 연구 공백에 관한
미확인 주장을 추가하는 오류가 남았습니다. [오류와 수정 기록](tests/behavior/SEMANTIC-REPORT.md)을
공개합니다. 이 도구는 작성을 돕지만 사실성·방법론적 타당성·게재 성과를 보장하지
않습니다. 대조 실험이나 독립적인 연구자 사용 평가는 아직 수행하지 않았습니다.

```sh
python3 -m unittest discover -s tests/install -v
python3 -m unittest discover -s tests/latex-audit -v
python3 scripts/build_corpus_index.py --check
```

## 기여와 재사용

오류 수정, 대조 사례, 실제 작성 중 발견한 실패 사례를 환영합니다.
[기여 안내](CONTRIBUTING.md)를 참고하세요. 프로젝트의 원본 코드와 문서는
[MIT 라이선스](LICENSE)로 제공하며, 연결된 논문의 권리는 원 권리자에게 있습니다.
원문 PDF, 비공개 Zotero 기록과 모델 대화 전문은 배포하지 않습니다.
[시각 자료 출처](assets/README.md)에 생성형 커버와 원본 로고를 기록했습니다.
