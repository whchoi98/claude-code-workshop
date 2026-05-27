# Slide 88: Multilingual docs

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### i18n docs

```bash
# 패턴 1: 두 디렉토리 분리
docs/
├── en/
│   ├── README.md
│   └── api.md
└── ko/
    ├── README.md
    └── api.md

# 패턴 2: 한 파일에 섹션 분리 (작은 프로젝트)
# README.md

## English
This project provides a payment gateway integration.

## 한국어
이 프로젝트는 결제 게이트웨이 통합을 제공합니다.

# docs-writer 호출
> @docs-writer src/payment.js 변경 사항을
  docs/en/payment.md와 docs/ko/payment.md에 모두 반영해 줘

# 결과: 두 언어 버전이 동시에 갱신됨
```

## Speaker Notes

다국어 문서 관리 패턴을 살펴봅니다.
한국어와 영어를 동시에 관리해야 할 때 두 가지 패턴이 있습니다.
첫 번째 패턴은 두 디렉토리 분리입니다.
docs/en과 docs/ko로 디렉토리를 나누고 같은 파일명을 양쪽에 둡니다.
대규모 프로젝트에 적합합니다.
두 번째 패턴은 한 파일 안에 섹션 분리입니다.
README 같은 단일 파일에 English와 한국어 섹션을 함께 둡니다.
작은 프로젝트에 적합합니다.
docs-writer를 호출할 때 두 언어 모두에 변경을 반영해 달라고 명시합니다.
예시처럼 한국어와 영어 파일 경로를 모두 지정합니다.
결과적으로 두 언어 버전이 동시에 갱신되며 용어 일관성이 유지됩니다.
