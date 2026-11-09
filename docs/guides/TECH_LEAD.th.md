# 🛠️ คู่มือการประเมินทางเทคนิค

[← เริ่มต้นที่ไหน](../START_HERE.th.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · **ไทย** · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## ในหนึ่งบรรทัด

ไม่ต้องอ่านโค้ดก็ประเมินได้ว่าฉันคิดอย่างไร: แค่ดูว่าอะไรรันได้ อะไรถูกทดสอบ และอะไรระบุว่ายังค้างอยู่

## สี่เส้นทาง เส้นทางละ 10 นาที

| เส้นทาง | เพื่อดู… | วิธีการ |
|---|---|---|
| **A. การสังเกตการณ์ระบบและการประสานงาน** | เวิร์กโฟลว์ เมตริก แดชบอร์ด และ guardrail ครอบคลุม 20 กรณีและเอนจินฐานข้อมูลกว่า 18 ตัว | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. โครงสร้างพื้นฐานที่ทำซ้ำได้** | ห้องปฏิบัติการคอนเทนเนอร์ที่ขึ้นได้ในไม่กี่นาที | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. เอเจนต์ที่มีสถานะแบบกำหนดชนิด** | แบ็กเอนด์ LangGraph 25 ตัว DEMO/LIVE ห่วงโซ่การครอบครองหลักฐาน | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. ผลิตภัณฑ์นิติวิทยาศาสตร์ด้วย Rust** | ตัวติดตั้งและไบนารีพร้อมเช็กซัม ไม่ต้องโคลน | [รีลีสของ RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## สัญญาณคุณภาพที่คุณตรวจสอบได้

| สัญญาณ | ดูที่ไหน |
|---|---|
| การทดสอบ | GabySQL มี 850 การทดสอบ และ fuzz 503.8 ล้านคิวรีโดยไม่มี panic Empresa Operativa Chile มี 230 การทดสอบ Automa มี pytest 150 รายการ |
| ห่วงโซ่อุปทาน | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX SBOM และ Scorecard ตามแต่ละคลัง |
| เทเลเมทรี | เป็นศูนย์ในผลิตภัณฑ์นิติวิทยาศาสตร์และใน Empresa Operativa Chile ตรวจสอบทุกบิลด์ |
| การเผยแพร่ | รีลีสพร้อมเช็กซัมและหลักฐานการบิลด์ การเซ็นรับรองเชิงพาณิชย์ระบุว่ายังค้างอยู่ |
| ความตรงไปตรงมา | แต่ละคลังระบุสถานะและสิ่งที่ **ไม่ได้** ทำ |

ตัวเลขทั้งหมดพร้อมแหล่งที่มาอยู่ใน[สถานะที่ใช้ได้](../../README.th.md#สถานะที่ใช้ได้)

## วิธีที่ฉันออกแบบ

- **จากโมเดลสู่ภายนอก:** โดเมนมาก่อน อินเทอร์เฟซเป็นเพียงภาพฉาย
- **การสังเกตการณ์ระบบตั้งแต่วันแรก:** `/health`, `/ready`, `/metrics` และการตรวจสอบย้อนกลับ
- **ความยืดหยุ่นจริง:** idempotency, circuit breaker และการลดระดับอย่างควบคุมได้
- **หลายภาษาโดยการออกแบบ:** เลือกภาษาและเอนจินตามกรณีใช้งาน
- **DX มาก่อน:** `doctor` และ `smoke` ในทุกคลัง หากรันไม่ง่ายก็ใช้เป็นฐานของทีมไม่ได้

## ต้องการศึกษาเพิ่มเติม

- [เทคโนโลยีสแตก](../../README.th.md#-เทคโนโลยีสแตก)ที่ตรวจพบในคลังต่าง ๆ
- [ดูระบบนิเวศทั้งหมด](../ECOSYSTEM.th.md): แต่ละผลิตภัณฑ์พร้อมเวอร์ชัน การทดสอบ และรีลีส
- fork ของบุคคลที่สามแยกไว้ต่างหากและไม่นับเป็นผลงานของตนเอง: [Fork ของโปรเจกต์บุคคลที่สาม](../ECOSYSTEM.th.md#forks)

## ขั้นตอนถัดไป

หากต้องการให้ตรวจสอบสถาปัตยกรรมหรือสนทนาทางเทคนิค เขียนถึง [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com)
