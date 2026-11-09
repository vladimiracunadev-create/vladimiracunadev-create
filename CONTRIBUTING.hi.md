# योगदान मार्गदर्शिका

**भाषाएँ:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

इस पारिस्थितिकी तंत्र में योगदान पर विचार करने के लिए धन्यवाद। चूँकि इसे **ऑब्ज़र्वेबिलिटी**, **पुनरुत्पादनीयता**, **local-first गुणवत्ता** और **idempotency** के इर्द-गिर्द डिज़ाइन किया गया है, इसलिए हम कोड की अखंडता से उच्च अपेक्षाएँ रखते हैं ताकि यह पोर्टफ़ोलियो आधुनिक इंजीनियरिंग का प्रतिबिंब बना रहे।

## जिन योगदानों का हम स्वागत करते हैं

- 🐛 **बग सुधार:** पहचानी गई समस्याओं को हल करें, अधिमानतः ऐसे स्वचालित परीक्षण (`pytest` आदि) के साथ जो सुधार को प्रमाणित करे।
- 🚀 **नई सुविधाएँ:** आर्किटेक्चर में सुधार और नए इंटीग्रेशन, जैसे n8n, Ollama या LangGraph के साथ।
- 📖 **दस्तावेज़ीकरण:** अधिक स्पष्ट व्याख्याएँ, अनुवाद या स्पष्ट आर्किटेक्चर आरेख (Mermaid या draw.io)।
- 🏗️ **इंफ्रास्ट्रक्चर:** DevOps वर्कफ़्लो (Kubernetes, CI/CD, Makefile और PWA कॉन्फ़िगरेशन) में सुधार।

## कार्यप्रवाह (Git Flow)

यह प्रोजेक्ट एक मानकीकृत फ़ीचर-ब्रांच कार्यप्रवाह का उपयोग करता है:

1. रिपॉज़िटरी को अपने खाते में **Fork** करें।
2. नवीनतम `main` ब्रांच से अपनी सुविधा या सुधार के लिए **एक ब्रांच बनाएँ**:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. अपना बदलाव **विकसित करें**।
   - रिपॉज़िटरी के स्थापित तरीके का पालन करें। यदि वह उच्च-प्रदर्शन Python कार्यप्रवाह के लिए `uv` का उपयोग करती है, तो बदलाव का औचित्य बताए बिना उसे न बदलें।
   - प्रोजेक्ट के मौजूदा गार्डरेल चलाएँ।
4. अपने बदलाव **Commit** करें। हम **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` आदि) का उपयोग करते हैं:

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. अपनी ब्रांच **Push** करें:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. इस रिपॉज़िटरी की `main` ब्रांच के विरुद्ध **Pull Request (PR) खोलें**।

## कोड मानक

- **परीक्षण-आधारित विकास (वैकल्पिक लेकिन अनुशंसित):** अपने परीक्षण चलाने के कमांड शामिल करें। यदि रिपॉज़िटरी में `mypy` या `bandit` के लिए GitHub Actions हैं, तो सुनिश्चित करें कि आपके बदलाव स्थानीय रूप से पास हों (`make test`, `make lint` या पारिस्थितिकी तंत्र में उपलब्ध स्क्रिप्ट)।
- **Docker-first:** हर आवश्यक निर्भरता का दस्तावेज़ीकरण हो और वह `docker-compose.yml` के ज़रिए उपलब्ध हो, ताकि आर्किटेक्चर 60 सेकंड से कम में शुरू हो सके या अनावश्यक स्थानीय सेटअप की बाधा से बचा जा सके।
- **दस्तावेज़ीकरण अनिवार्य है:** बड़े बदलाव के लिए README अपडेट करें और, जहाँ उपयुक्त हो, एक व्याख्यात्मक आरेख जोड़ें।
