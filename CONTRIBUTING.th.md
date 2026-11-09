# คู่มือการมีส่วนร่วม

**ภาษา:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

ขอบคุณที่พิจารณาร่วมสนับสนุนระบบนิเวศนี้ เนื่องจากออกแบบโดยยึด **การสังเกตการณ์ระบบ (observability)** **การทำซ้ำได้** **คุณภาพแบบ local-first** และ **idempotency** เราจึงตั้งมาตรฐานความสมบูรณ์ของโค้ดไว้สูง เพื่อให้พอร์ตโฟลิโอนี้ยังสะท้อนงานวิศวกรรมสมัยใหม่

## การมีส่วนร่วมที่เรายินดีต้อนรับ

- 🐛 **แก้ไขข้อบกพร่อง:** แก้ปัญหาที่ระบุได้ โดยควรมีการทดสอบอัตโนมัติ (`pytest` เป็นต้น) ที่พิสูจน์การแก้ไข
- 🚀 **ฟีเจอร์ใหม่:** การปรับปรุงสถาปัตยกรรมและการเชื่อมต่อใหม่ เช่น กับ n8n, Ollama หรือ LangGraph
- 📖 **เอกสาร:** คำอธิบายที่ชัดเจนขึ้น คำแปล หรือแผนภาพสถาปัตยกรรมที่ชัดแจ้ง (Mermaid หรือ draw.io)
- 🏗️ **โครงสร้างพื้นฐาน:** การปรับปรุงเวิร์กโฟลว์ DevOps (Kubernetes, CI/CD, Makefile และการตั้งค่า PWA)

## ขั้นตอนการทำงาน (Git Flow)

โปรเจกต์นี้ใช้เวิร์กโฟลว์แบบ feature-branch ที่เป็นมาตรฐาน:

1. **Fork** รีโพซิทอรีไปยังบัญชีของคุณ
2. **สร้างบรานช์** สำหรับฟีเจอร์หรือการแก้ไขของคุณจากบรานช์ `main` ล่าสุด:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **พัฒนา** การเปลี่ยนแปลงของคุณ
   - ทำตามแนวทางที่รีโพซิทอรีใช้อยู่ หากใช้ `uv` สำหรับเวิร์กโฟลว์ Python ประสิทธิภาพสูง อย่าเปลี่ยนเว้นแต่คุณจะอธิบายเหตุผลได้
   - รันกลไกป้องกัน (guardrail) ที่มีอยู่ของโปรเจกต์
4. **Commit** การเปลี่ยนแปลงของคุณ เราใช้ **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` เป็นต้น):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Push** บรานช์ของคุณ:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **เปิด Pull Request (PR)** ไปยังบรานช์ `main` ของรีโพซิทอรีนี้

## มาตรฐานโค้ด

- **การพัฒนาโดยใช้การทดสอบเป็นแนวทาง (ไม่บังคับแต่แนะนำ):** ใส่คำสั่งสำหรับรันการทดสอบของคุณ หากรีโพซิทอรีมี GitHub Actions สำหรับ `mypy` หรือ `bandit` โปรดตรวจให้แน่ใจว่าการเปลี่ยนแปลงผ่านในเครื่อง (`make test`, `make lint` หรือสคริปต์ที่มีในระบบนิเวศ)
- **Docker เป็นอันดับแรก:** ทุกส่วนที่ต้องพึ่งพาต้องมีเอกสารและพร้อมใช้ผ่าน `docker-compose.yml` เพื่อให้สถาปัตยกรรมเริ่มทำงานได้ในเวลาไม่ถึง 60 วินาที หรือหลีกเลี่ยงอุปสรรคการตั้งค่าในเครื่องที่ไม่จำเป็น
- **ต้องมีเอกสาร:** หากเป็นการเปลี่ยนแปลงใหญ่ ให้อัปเดต README และเพิ่มแผนภาพอธิบายเมื่อเหมาะสม
