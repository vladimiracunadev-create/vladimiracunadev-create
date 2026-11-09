# 기여 가이드

**언어:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

이 생태계에 기여를 고려해 주셔서 감사합니다. **관측 가능성**, **재현성**, **로컬 우선 품질**, **멱등성**을 중심으로 설계되었기에, 이 포트폴리오가 현대 엔지니어링을 보여 주는 거울로 남도록 코드 무결성에 높은 기준을 유지합니다.

## 환영하는 기여

- 🐛 **버그 수정:** 확인된 문제를 해결하세요. 수정을 증명하는 자동화 테스트(`pytest` 등)가 있으면 좋습니다.
- 🚀 **새 기능:** 아키텍처 개선과 n8n, Ollama, LangGraph 등과의 새로운 통합.
- 📖 **문서:** 더 명확한 설명, 번역 또는 명시적인 아키텍처 다이어그램(Mermaid 또는 draw.io).
- 🏗️ **인프라:** DevOps 워크플로(Kubernetes, CI/CD, Makefile, PWA 설정) 개선.

## 워크플로 (Git Flow)

이 프로젝트는 표준화된 기능 브랜치 워크플로를 사용합니다.

1. 저장소를 내 계정으로 **포크**합니다.
2. 최신 `main` 브랜치에서 기능 또는 수정용 **브랜치를 만듭니다**.

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. 변경 사항을 **개발**합니다.
   - 저장소의 기존 방식을 따르세요. 고성능 Python 워크플로에 `uv`를 사용한다면, 변경 이유를 설명하지 않는 한 대체하지 마세요.
   - 프로젝트에 이미 있는 가드레일을 실행합니다.
4. 변경 사항을 **커밋**합니다. **Conventional Commits**(`feat:`, `fix:`, `docs:`, `chore:` 등)를 사용합니다.

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. 브랜치를 **푸시**합니다.

   ```bash
   git push origin feature/new-aws-magic
   ```

6. 이 저장소의 `main` 브랜치를 대상으로 **풀 리퀘스트(PR)를 엽니다**.

## 코드 표준

- **테스트 주도 개발(선택 사항이나 권장):** 테스트 실행 명령을 포함하세요. 저장소에 `mypy` 또는 `bandit`용 GitHub Actions가 있다면 변경 사항이 로컬에서 통과하는지 확인하세요(`make test`, `make lint` 또는 생태계에서 제공하는 스크립트).
- **Docker 우선:** 필요한 모든 의존성은 문서화하고 `docker-compose.yml`로 제공해야 하며, 아키텍처가 60초 안에 시작되거나 불필요한 로컬 설정 부담이 없도록 해야 합니다.
- **문서는 필수:** 큰 변경이라면 README를 업데이트하고, 해당하는 경우 설명 다이어그램을 추가하세요.
