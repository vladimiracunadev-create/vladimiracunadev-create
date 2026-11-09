# Hướng dẫn đóng góp

**Ngôn ngữ:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Cảm ơn bạn đã cân nhắc đóng góp cho hệ sinh thái này. Vì được thiết kế xoay quanh **khả năng quan sát**, **khả năng tái lập**, **chất lượng local-first** và **tính idempotent**, chúng tôi giữ kỳ vọng cao về tính toàn vẹn của mã để danh mục này tiếp tục phản ánh kỹ thuật hiện đại.

## Những đóng góp chúng tôi hoan nghênh

- 🐛 **Sửa lỗi:** Giải quyết các vấn đề đã xác định, tốt nhất kèm một bài kiểm thử tự động (`pytest`, v.v.) chứng minh bản sửa.
- 🚀 **Tính năng mới:** Cải tiến kiến trúc và các tích hợp mới, ví dụ với n8n, Ollama hoặc LangGraph.
- 📖 **Tài liệu:** Giải thích rõ ràng hơn, bản dịch hoặc sơ đồ kiến trúc tường minh (Mermaid hoặc draw.io).
- 🏗️ **Hạ tầng:** Cải thiện quy trình DevOps (Kubernetes, CI/CD, Makefile và cấu hình PWA).

## Quy trình làm việc (Git Flow)

Dự án này dùng quy trình nhánh tính năng (feature-branch) được chuẩn hóa:

1. **Fork** kho mã về tài khoản của bạn.
2. **Tạo một nhánh** cho tính năng hoặc bản sửa của bạn từ nhánh `main` mới nhất:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Phát triển** thay đổi của bạn.
   - Làm theo cách tiếp cận đã có của kho mã. Nếu kho dùng `uv` cho quy trình Python hiệu năng cao, đừng thay thế nếu bạn không giải thích được lý do.
   - Chạy các lớp bảo vệ (guardrail) hiện có của dự án.
4. **Commit** các thay đổi. Chúng tôi dùng **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, v.v.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Push** nhánh của bạn:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Mở một Pull Request (PR)** vào nhánh `main` của kho mã này.

## Tiêu chuẩn mã

- **Phát triển hướng kiểm thử (tùy chọn nhưng nên làm):** Kèm theo lệnh chạy kiểm thử. Nếu kho có GitHub Actions cho `mypy` hoặc `bandit`, hãy bảo đảm thay đổi của bạn vượt qua ở máy cục bộ (`make test`, `make lint` hoặc các script có trong hệ sinh thái).
- **Docker trước tiên:** Mọi phụ thuộc cần thiết phải được ghi tài liệu và sẵn có qua `docker-compose.yml` để kiến trúc khởi động dưới 60 giây hoặc tránh những rào cản cài đặt cục bộ không cần thiết.
- **Bắt buộc có tài liệu:** Với thay đổi lớn, hãy cập nhật README và, khi phù hợp, thêm sơ đồ giải thích.
