# 🛠️ 기술 평가 가이드

[← 시작하기](../START_HERE.ko.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · **한국어** · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## 한 줄로

제가 어떻게 생각하는지 판단하는 데 코드를 읽을 필요는 없습니다. 무엇이 실행되고, 무엇이 테스트되며, 무엇이 보류로 밝혀져 있는지만 보면 충분합니다.

## 10분짜리 네 가지 경로

| 경로 | 볼 수 있는 것 | 방법 |
|---|---|---|
| **A. 관측 가능성과 오케스트레이션** | 20개 사례와 18개 이상의 DB 엔진에 걸친 워크플로, 지표, 대시보드, 가드레일 | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. 재현 가능한 인프라** | 몇 분 만에 올라오는 컨테이너 랩 | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. 타입 있는 상태의 에이전트** | LangGraph 백엔드 25개, DEMO/LIVE, 증거 보관 사슬 | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust로 만든 포렌식 제품** | 체크섬이 있는 설치 파일과 바이너리(복제 불필요) | [RootCause 릴리스](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## 직접 검증할 수 있는 품질 신호

| 신호 | 확인할 곳 |
|---|---|
| 테스트 | GabySQL 테스트 850개와 패닉 없는 5억 380만 쿼리 퍼징, Empresa Operativa Chile 테스트 230개, Automa pytest 150개 |
| 공급망 | 저장소에 따라 CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX SBOM, Scorecard |
| 텔레메트리 | 포렌식 제품과 Empresa Operativa Chile는 0이며, 빌드마다 검증 |
| 배포 | 체크섬과 빌드 증거가 있는 릴리스, 상용 서명은 보류로 명시 |
| 정직성 | 각 저장소가 상태와 **하지 않는 일**을 명시 |

출처가 있는 모든 수치는 [검증된 상태](../../README.ko.md#검증된-상태)에 있습니다.

## 설계 방식

- **모델에서 바깥으로:** 도메인이 먼저, 인터페이스는 그 투영.
- **첫날부터의 관측 가능성:** `/health`, `/ready`, `/metrics`, 추적 가능성.
- **실질적인 복원력:** 멱등성, 서킷 브레이커, 통제된 성능 저하.
- **설계에 따른 다언어:** 사용 사례별로 언어와 엔진을 선택.
- **DX 우선:** 저장소마다 `doctor`와 `smoke`. 쉽게 실행되지 않으면 팀의 기반으로 쓸 수 없습니다.

## 더 깊이 보려면

- 저장소에서 감지한 [기술 스택](../../README.ko.md#-기술-스택).
- [전체 생태계 보기](../ECOSYSTEM.ko.md): 각 제품의 버전, 테스트, 릴리스.
- 제3자 포크는 따로 관리하며 자체 작업으로 세지 않습니다: [제3자 프로젝트의 포크](../ECOSYSTEM.ko.md#forks).

## 다음 단계

아키텍처 리뷰나 기술 대화를 원하시면 [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com)로 연락해 주세요.
