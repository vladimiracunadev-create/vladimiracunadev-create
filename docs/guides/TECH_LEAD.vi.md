# 🛠️ Hướng dẫn đánh giá kỹ thuật

[← Bắt đầu từ đâu](../START_HERE.vi.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · **Tiếng Việt** · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Trong một dòng

Bạn không cần đọc mã để đánh giá cách tôi tư duy: chỉ cần xem điều gì chạy được, điều gì được kiểm thử và điều gì được nêu là còn tồn đọng.

## Bốn lộ trình 10 phút

| Lộ trình | Để xem… | Cách làm |
|---|---|---|
| **A. Khả năng quan sát và điều phối** | Workflow, số liệu, bảng điều khiển và guardrail trên 20 trường hợp và hơn 18 hệ quản trị CSDL | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Hạ tầng có thể tái lập** | Phòng thí nghiệm container chạy trong vài phút | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agent có trạng thái định kiểu** | 25 backend LangGraph, DEMO/LIVE, chuỗi bảo quản bằng chứng | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Sản phẩm pháp chứng bằng Rust** | Bộ cài và tệp nhị phân kèm checksum, không cần clone | [Bản phát hành RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Dấu hiệu chất lượng bạn có thể kiểm chứng

| Dấu hiệu | Xem ở đâu |
|---|---|
| Kiểm thử | GabySQL với 850 kiểm thử và lượt fuzz 503,8 triệu truy vấn không panic; Empresa Operativa Chile với 230 kiểm thử; Automa với 150 pytest |
| Chuỗi cung ứng | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX và Scorecard, tùy kho mã |
| Đo từ xa | Bằng không ở các sản phẩm pháp chứng và ở Empresa Operativa Chile, được xác minh ở mỗi bản build |
| Phân phối | Bản phát hành kèm checksum và bằng chứng build; chữ ký thương mại được nêu là còn chờ |
| Sự trung thực | Mỗi kho nêu trạng thái và điều nó **không** làm |

Mọi con số kèm nguồn nằm trong [Trạng thái có thể truy cập](../../README.vi.md#trạng-thái-có-thể-truy-cập).

## Cách tôi thiết kế

- **Từ mô hình ra ngoài:** miền nghiệp vụ trước, giao diện chỉ là một phép chiếu.
- **Khả năng quan sát từ ngày đầu:** `/health`, `/ready`, `/metrics` và khả năng truy vết.
- **Khả năng phục hồi thực sự:** idempotency, circuit breaker và suy giảm có kiểm soát.
- **Đa ngôn ngữ theo thiết kế:** ngôn ngữ và engine được chọn theo từng trường hợp.
- **DX trước hết:** `doctor` và `smoke` cho mỗi kho; nếu không chạy dễ dàng thì không dùng làm nền tảng cho đội ngũ được.

## Để tìm hiểu sâu hơn

- [Ngăn xếp công nghệ](../../README.vi.md#-ngăn-xếp-công-nghệ) được phát hiện trong các kho mã.
- [Xem toàn bộ hệ sinh thái](../ECOSYSTEM.vi.md): mỗi sản phẩm kèm phiên bản, kiểm thử và bản phát hành.
- Các fork của bên thứ ba được tách riêng và không tính là sản phẩm tự thực hiện: [Fork của dự án bên thứ ba](../ECOSYSTEM.vi.md#forks).

## Bước tiếp theo

Để rà soát kiến trúc hoặc trao đổi kỹ thuật, hãy viết tới [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
