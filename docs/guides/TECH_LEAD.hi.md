# 🛠️ तकनीकी मूल्यांकन गाइड

[← कहाँ से शुरू करें](../START_HERE.hi.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · **हिन्दी** · [Ελληνικά](TECH_LEAD.el.md)

## एक पंक्ति में

मैं कैसे सोचता हूँ, यह परखने के लिए कोड पढ़ना ज़रूरी नहीं: बस देखें कि क्या चलाया जा सकता है, क्या परखा जाता है और क्या लंबित घोषित है।

## 10-10 मिनट के चार मार्ग

| मार्ग | क्या देखें… | कैसे |
|---|---|---|
| **A. ऑब्ज़र्वेबिलिटी और ऑर्केस्ट्रेशन** | 20 मामलों और 18+ डेटाबेस इंजनों पर वर्कफ़्लो, मीट्रिक, डैशबोर्ड और गार्डरेल | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. पुनरुत्पादन-योग्य इंफ्रास्ट्रक्चर** | मिनटों में चालू होने वाली कंटेनर प्रयोगशालाएँ | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. टाइप्ड स्टेट वाले एजेंट** | 25 LangGraph बैकएंड, DEMO/LIVE, साक्ष्य-अभिरक्षा श्रृंखला | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust में फ़ॉरेंसिक उत्पाद** | चेकसम वाले इंस्टॉलर और बाइनरी, बिना क्लोन किए | [RootCause रिलीज़](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## गुणवत्ता के संकेत जिन्हें आप सत्यापित कर सकते हैं

| संकेत | कहाँ देखें |
|---|---|
| टेस्ट | GabySQL के 850 टेस्ट और 50.38 करोड़ क्वेरी का fuzz बिना panic के; Empresa Operativa Chile के 230 टेस्ट; Automa के 150 pytest |
| सप्लाई चेन | रिपॉज़िटरी के अनुसार CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX SBOM और Scorecard |
| टेलीमेट्री | फ़ॉरेंसिक उत्पादों और Empresa Operativa Chile में शून्य, हर बिल्ड में सत्यापित |
| वितरण | चेकसम और बिल्ड प्रमाण वाली रिलीज़; व्यावसायिक हस्ताक्षर लंबित घोषित |
| ईमानदारी | हर रिपॉज़िटरी अपनी स्थिति और जो वह **नहीं** करती, बताती है |

स्रोत सहित सभी आँकड़े [सत्यापन योग्य स्थिति](../../README.hi.md#सत्यापन-योग्य-स्थिति) में हैं।

## मैं कैसे डिज़ाइन करता हूँ

- **मॉडल से बाहर की ओर:** पहले डोमेन, इंटरफ़ेस उसका प्रक्षेपण।
- **पहले दिन से ऑब्ज़र्वेबिलिटी:** `/health`, `/ready`, `/metrics` और ट्रेसबिलिटी।
- **वास्तविक लचीलापन:** idempotency, circuit breaker और नियंत्रित क्षरण।
- **डिज़ाइन से बहुभाषी:** उपयोग-मामले के अनुसार भाषा और इंजन का चयन।
- **पहले DX:** हर रिपॉज़िटरी में `doctor` और `smoke`; जो आसानी से न चले, वह टीम का आधार नहीं बन सकता।

## और गहराई में जाने के लिए

- रिपॉज़िटरी में पाया गया [टेक्नोलॉजी स्टैक](../../README.hi.md#-टेक्नोलॉजी-स्टैक)।
- [पूरा पारिस्थितिकी तंत्र देखें](../ECOSYSTEM.hi.md): हर उत्पाद अपने संस्करण, टेस्ट और रिलीज़ के साथ।
- तृतीय-पक्ष fork अलग रखे जाते हैं और अपने कार्य में नहीं गिने जाते: [तृतीय-पक्ष प्रोजेक्ट्स के fork](../ECOSYSTEM.hi.md#forks)।

## अगला कदम

आर्किटेक्चर समीक्षा या तकनीकी बातचीत के लिए [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com) पर लिखें।
