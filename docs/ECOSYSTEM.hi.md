# 🗂️ पारिस्थितिकी तंत्र: उत्पाद, प्रयोगशालाएँ, अनुप्रयुक्त AI और वैज्ञानिक कम्प्यूटिंग

[← प्रोफ़ाइल पर वापस जाएँ](../README.hi.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · **हिन्दी** · [Ελληνικά](ECOSYSTEM.el.md)

इस प्रोफ़ाइल का व्यावहारिक कार्य एक अलग दस्तावेज़ में है: डाउनलोड और इंस्टॉल होने वाला सॉफ़्टवेयर, इंजीनियरिंग प्रयोगशालाएँ, अनुप्रयुक्त AI और वैज्ञानिक कम्प्यूटिंग, साथ ही खाते में मौजूद तृतीय-पक्ष प्रोजेक्ट्स के हर fork का विवरण।

## 📦उत्पाद रियल डिस्ट्रीब्यूशन के साथ

सॉफ्टवेयर जो डाउनलोड, इंस्टाल किया गया है और इस्तेमाल किया गया है - न केवल क्लोन किया गया।

| उत्पाद | क्या है | स्टैक | डिलिवरी |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | साइबर सुरक्षा फोरेंसिक: हर सर्वसम्मतिपूर्ण संसाधन विरूपण एक खतरे का पहला संकेत हो सकता है। पहले निदान, बाद में हस्तक्षेप | रुस्ट🦀 ·EETW/WPR | **v0.19.0** · **16 रिलीज़** · **5 संस्करण**A-GUI·पोर्टेबल·सी एल आई·पावरशेल·वीएस कोड· [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | मोबाइल भाई-बहन: एक फोरेंसिक सेंसर जो प्रत्येक ऐप को अपने खिलाफ तुलना करता है, झंडे के तारेवेयर, और अलग-अलग अनुमतियों को केवल अनुरोधित लोगों से अलग करता है। | फ्लुटर·कोट्टलिन·स्विफ्ट | **v0.8.0** ·Android APK·5 भाषाओं· **शून्य टेलीमेट्री** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | MacOS संस्करण:`launchd`दृढ़ता, गेटकीपर, एसआईपी, फ़ाइलवॉल्ट, एक्सप्रोटेक्ट, टीसीसी अनुमतियां, हस्ताक्षरित प्रक्रियाएं और नेटवर्क पड़ोसी - प्रत्येक सतह को एक ज्ञात-अच्छा राज्य के खिलाफ जांच की जाती है | रुस्ट🦀 ·MacOS 13+ | **v0.1.0** ·प्रथम प्रकाशित रिलीज़·अपाचे-2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | The server sibling: correlates what no single log sees together — exposed surface, access-attempt bursts, a session granted to that same address, critical file integrity, and sensor silence — and turns it into one actionable sentence | Rust 🦀 · Windows · Linux · macOS | **v0.2.0** · **18 rules** with evidence and runbook · never executes actions on its own · local console without web dependencies · **no published release yet** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | ब्राउज़र फोरेंसिक सेंसर: कुकीज़, ईमेल सत्र, एक्सटेंशन, डाउनलोड, अनुमतियां और पृष्ठ जो वास्तविक विंडो की नकल करते हैं | जावास्क्रिप्ट·MV3 एक्सटेंशन | **v0.2.0** ·अभी तक कोई प्रकाशित रिलीज़ नहीं·पैनल पर`127.0.0.1` ·शून्य निर्भरता·CI में सत्यापित शून्य टेलीमेट्री· [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Watch-only defense for Bitcoin custody: inventories the origin of each key, cross-checks it with published warnings, and explains root cause with evidence | JavaScript · Windows app · local panel | **v0.3.0** · **2 releases** · zero dependencies · never asks for seeds · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | मल्टी-चेन घड़ी केवल सांत्वना: आविष्कारों के अनुबंध, प्रॉक्सी, oracles, पुल, शासन, और निर्भरता, और जड़-काउज़ runbooks उत्पन्न | जावास्क्रिप्ट·Windows app·स्थानीय पैनल | **v0.3.0**भंडार में·प्रकाशित रिलीज़:`v0.1.0` ·शून्य निर्भरता·कभी निजी कुंजी के लिए पूछता है·CI में सत्यापित· [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | Local Android app for inspecting QR codes before acting: explains 26 signals, separates facts from hypotheses, and exports redacted evidence | Flutter · Dart | **v0.1.4** · **5 releases** · **107 tests** · published Android APK · verifiable SHA-256 · technical APK package signature; commercial/store signatures in progress · zero telemetry · [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | प्रत्येक मासिक बंद करने के लिए निगमन से पहले एक SpA गाइड: साक्ष्य के साथ निगमन, VAT कैरी-फॉरवर्ड, F29 ड्राफ्ट, अचल बंद और ऑडिट लॉग. हर नियम अपने आधिकारिक स्रोत को इंगित करता है | जावास्क्रिप्ट·रुस्ट·पीडब्लूए | **v1.5.0** ·Android·Windows·ब्राउज़र· **158 परीक्षण** · **0 उत्पादन निर्भरता** ·शून्य टेलीमेट्री· [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR और बारकोड रीडर**अभिनय से पहले व्याख्या**16 स्थानीय यूआरएल जोखिम संकेत और स्पष्ट पुष्टि | फ्लुटर·डार्ट | **v1.1.0** ·Android·आईओएस·मैक ओएस·पीडब्लूए·एन्क्रिप्टेड इतिहास**AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | एम्बेडेड डेटाबेस: एकल`.db`फ़ाइल, WAL, लागत आधारित अनुकूलनकर्ता, HTTP / JSON API | रुस्ट🦀 | Windows·मैक ओएस·लिनक्स· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | स्थानीय ऑर्केस्ट्रेटर: JSON प्रवाह जो वास्तविक खिड़कियां खोलते हैं, DOM के साथ बातचीत करते हैं, और सबूत छोड़ देते हैं | पायथन·प्लेराइट·Pywebview | **v0.3.0** · **27 प्रवाह** ·प्रकाशित और सत्यापन योग्य इंस्टॉलर· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | स्थानीय-पहली फैक्ट्री जो पूर्ववर्ती, ठीक-ट्यूनिंग, आरएजी और मूल्यांकन के लिए लेखापरीक्षित डेटासेट में पीडीएफ, वर्ड, वेब, गिट, जेएसओएन और सीएसवी को बदल देती है। | पायथन | **v0.2.0** ·Windows + Internet Android·प्रथम प्रकाशित रिलीज़· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | 15 AWS इन्वेंट्री एकीकरण, 20 ट्यूटोरियल, CLI/SSO, और केवल डिफॉल्ट के साथ स्थानीय-पहली ऐप; प्रगति में कार्यान्वयन, सार्वभौमिक पहुंच नहीं | जावास्क्रिप्ट·Windows | **v0.1.1** ·प्रथम प्रकाशित रिलीज़· [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | व्यावसायिक संचालन के निर्देशित वैचारिक डेमो: सूची, स्टॉक, सीआरएम, ऑर्डर, नकली भुगतान और पता लगाने की क्षमता | जावास्क्रिप्ट·वेब·Windows·Android | **v0.3.0** · **2 रिलीज़** ·कोई वास्तविक धन या चिली कर प्राधिकरण एकीकरण· [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | एंड्रॉयड सबसे पहले स्थानीय पढ़ने वाले पाठक, जिसमें कोई क्रॉप ज़ूम, पुनर्खुली इतिहास, व्हाट्सएप शेयरिंग और डिफ़ॉल्ट पठनीय चयन नहीं है। | एचटीएमएल·वेब·Android·Windows | **v0.3.3** ·APK·कोई लेखा, संवेदनशील अनुमतियां, या टेलीमेट्री· [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | एक वीडियो, प्लेलिस्ट, या**पूरे यूट्यूब चैनल**पाठ्यपुस्तक के साथ पाठ करने के लिए। यह मौजूदा उपशीर्षक पर निर्भर नहीं है: व्हिस्पर ऑडियो को पहचानता है**अपनी मशीन पर**, कोई API, खाता, या कुंजी के साथ विन्यस्त करने के लिए | पायथन·PySide6·फास्टएपीआई·तेज़-whisper | **v0.2.0** ·Windows डेस्कटॉप + स्थानीय पैनल पर`127.0.0.1`+ CLI,**उसी कतार को साझा करना** ·एमडी·PDF·TXT·एसआरटी·VTT·जेएसओएन·एमपी 3·ओजीजी· **89 परीक्षण** ·बंडल Fmpeg·शून्य टेलीमेट्री· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | स्थानीय रचनात्मक एआई लॉन्चर: ऑर्केस्ट्रेट Qwen3-TTS, whisper.cpp, FaceFusion, AceForge, and ComfyUI | 2·रुस्ट·प्रतिक्रिया | v0.5.1· **5/5 उपकरण, जो वास्तविक निवेश के साथ हैं** ·MacOS Apple सिलिकॉन·प्रयोगात्मक Windows· **अभी तक कोई प्रकाशित रिलीज़ नहीं** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | खरोंच से कार्यालय सूट: दस्तावेज़ नियम DOM पर निर्भर नहीं करते - एचटीएमएल केवल एक प्रक्षेपण है | जंग/WASM·गो·19 अधिनियम | चरणों द्वारा विकासवादी मोनोरेपो· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | बच्चों के लिए शैक्षिक ऐप: क्रोमेटिक ट्यूनर, ऑडियो-क्लॉक-अकरीट मेट्रोनोम, वास्तविक वायलिन के साथ गीत | 2·प्रतिक्रिया·टीएस | **v1.3.0** ·Windows·Android·लिनक्स·मैक ओएस·पीडब्लूए· [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | प्लक-स्ट्रिंग सिबलिंग: 6 दुनिया में 24 सबक, 6 स्ट्रिंग ट्यूनर, बहाव मुक्त मेट्रोनोम और 11 वास्तविक गिटार नोट | 2·प्रतिक्रिया·टीएस | **v1.0.0** ·Windows·Android·लिनक्स·मैक ओएस·आईओएस·पीडब्लूए·कोई खाता, विज्ञापन, या ऑनलाइन निर्भरता नहीं· [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | 10 वर्ष की आयु से क्यूका: 8 स्तरों में 24 वर्ग, 72 गतिविधियाँ, छह-पल्स लैब (3+3 और 2+2+2) और सुलभ मंजिल आरेख। यह बताता है कि यह**पूरक, प्रतिस्थापित नहीं**शिक्षकों और संस्कृति वाहक | फ्लुटर·डार्ट | **v0.2.0** ·Android 7+·Windows 10/11·APK·EXE·एमएसआई·पोर्टेबल· **29 परीक्षण + 2 सत्यापनकर्ता** ·कोई कैमरा, माइक्रोफोन, खाता, विज्ञापन, या इंटरनेट· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪इंजीनियरिंग प्रयोगशाला

| रेपो | यह क्या दर्शाता है |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 वास्तविक समस्याएं**(लोड के तहत विलंबता, N+1, पुनः प्रयास तूफान, लीक, मोनोलिथ्स, कैश स्टैम्पेड, बैकप्रेशर, शून्य-डाउनटाइम माइग्रेशन, भूल गए DLQ) उच्च-विश्वविद्यालय इंजेक्शन विफलताओं के साथ, हल में**7 स्टैक**PHP 8·पायथन·Node.js·जावा 21·8 .NET· **1.23** · **रुस्ट 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.10.0** · **20 मामले**स्रोत → n8n → receiver over**18+ DB इंजन** —**19 परिचालन**व्यक्तिगत रूप से डॉकर के साथ लेखा परीक्षा**8-परत**लेखा परीक्षा, idempotency रेलिंग, सर्किट ब्रेकर, और DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12 नैदानिक और आधुनिकीकरण microapps**PHP के लिए·केवल MCP सर्वर·3 चरणों में सख्त· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13 प्रयोगशालाएं**4-सेवा प्लेटफॉर्म + स्वचालित पर`.exe`लॉन्चर के साथ इंस्टॉलर· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 मामले**पर`wslc`मूल WSL कंटेनर इंजन**बिना किसी डेस्कटॉप के** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | "Deckers डेस्कटॉप": Windows नियंत्रण WSL2 बैकएंड के साथ यूनिक्राफ्ट पर,`kraft`QEMU/KVM· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 लैब्स**QEMU, KVM, libvirt, क्लाउड-इनिट और के साथ वास्तविक वर्चुअलाइजेशन`vm-manager`लिनक्स और WSL2 पर· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | लिनक्स अलगाव: घोषित नीतियों और के तहत तीसरे पक्ष के कोड, फ़ाइलों और व्यापार मॉडल चलाता है**वास्तव में लागू नियंत्रण के हस्ताक्षरित सबूत का उत्सर्जन करता है** · **36 मामले**दो परिवारों में -15 तकनीकी और 21 पूंजी बाजार -·प्रयोगात्मक और शैक्षिक घोषित, *नहीं एक सुरक्षा उत्पाद*· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 भुगतान परिवारों**एक स्थानीय स्व-विस्तार डेमो में: राज्यों, लेजर, पारस्परिकता, सुरक्षा और कार्यान्वयन गाइड· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Native Decentraland social 3D अनुभव: एक MVP और SDK7, ECS, and टाइपस्क्रिप्ट के साथ एक बहु-खेल वास्तुकला·स्पेनिश दस्तावेज़ीकरण·कोई भुगतान या टेलीमेट्री |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | प्रगतिशील मामले जहां प्रत्येक व्यक्ति एक एडब्ल्यूएस सेवा जोड़ता है**और**एक नई GitHub कार्य क्षमता·SAA-C03·DVA-C02·SOA-C02 कवरेज |

🤖 अनुप्रयुक्त AI

| रेपो | यह क्या दर्शाता है |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 परिचालन परिवर्धन**टाइप स्टेट, सशर्त मार्ग, एनडीजेएसएन स्ट्रीमिंग, डीईएमओ / लाइव मोड, 8 सुरक्षा परतें, शाह-256 श्रृंखला हिरासत की |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13 परिचालन एजेंट**क्लाउड कोड और संगत रनटाइम्स के लिए: प्रत्येक को एक पूर्ण मिशन प्राप्त होता है -अनुभवी विकास, विरासत आधुनिकीकरण, पाठ्यक्रम डिजाइन, पोर्टफोलियो प्रकाशन, सुरक्षा उपचार, घटना विश्लेषण- एक घोषित अनुबंध, मानव द्वार और सत्यापन योग्य सबूत के तहत· **39 नियतिवादी evals** ·34 परीक्षण·शून्य-डिप्स (केवल स्टिलिब)·लिनक्स·मैक ओएस·Windows· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | एक सैंडबॉक्स में MCP उपकरण के साथ स्थानीय-पहली AI· `127.0.0.1`बांधना·बहुपरत ट्रस्ट प्रोफाइल·अपनी सीमा के बारे में ईमानदार |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 एजेंटिक प्लगइन्स**क्लाउड कोड, OpenAI/Codex, Copilot, Gemini, और MCP में एक स्रोत से इंस्टॉल करने योग्य:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`, और`rootcause-response` · **69 बिना किसी बहाव के दृष्टिकोण पैदा**प्रत्येक रनटाइम को उसी अनुबंध से अपना प्रारूप प्राप्त होता है-·शून्य-डीप·लिनक्स·मैक ओएस·Windows· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **15 मनोवैज्ञानिक कौशल**क्लाउड कोड के लिए· **सुरक्षा**: 12-परत`security-audit`(OSV)·केवी·ईपीएस·एस.टी.·कंटेनर·रहस्य) और 14-चरण`bitcoin-custody-audit` · **रेपो गेट**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **सहगामी**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **डकर**: `docker-cleanup`, `docker-compose-doctor` · **doc**: `md-to-doc` ·शून्य-डीप·क्रॉस-प्लेटफॉर्म |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 मनोवैज्ञानिक कौशल**कोडेक्स के लिए: सुरक्षा और आपूर्ति श्रृंखला, प्रीफ्लाइट, कार्यात्मक प्रवाह, लचीलापन और राज्य, रिलीज सबूत, पायथन / या एमएल / मैकडाउन गेट्स, संस्करण, निर्भरता, डोकर और दस्तावेज़·पायथन-first· `pnpm` ·लिनक्स·मैक ओएस·Windows· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

## 🔬वैज्ञानिक कम्प्यूटिंग

| रेपो | यह क्या दर्शाता है |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | Reproducible genomics मंच: टाइप`ScientificResult<T>`अनुबंध, FASTA/GFF3/VCF, मॉड्यूल के साथ**स्पष्ट परिपक्वता और सबूत*** यह नैदानिक निदान नहीं करता है*· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 तृतीय-पक्ष प्रोजेक्ट्स के fork (52)

ये दूसरों के प्रोजेक्ट्स के fork हैं जो इस खाते में रखे गए हैं। **ये मेरा अपना कार्य नहीं हैं**: श्रेय उनके मूल लेखकों का है, ये इस प्रोफ़ाइल की किसी भी संख्या में नहीं गिने जाते, और हर विवरण केवल वही सारांशित करता है जो मूल प्रोजेक्ट स्वयं घोषित करता है; इसका अर्थ मेरी ओर से सपोर्ट, ऑडिट या प्रोडक्शन अनुभव नहीं है। विवरण मूल प्रोजेक्ट के अनुसार · 2026-11-09।

### 🤖 कोडिंग एजेंट और एजेंट फ़्रेमवर्क (18)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | AI-संचालित सॉफ़्टवेयर विकास के लिए एजेंट प्लेटफ़ॉर्म |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | SDK, IDE एक्सटेंशन या CLI के रूप में स्वायत्त कोडिंग एजेंट |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | ओपन-सोर्स कोडिंग एजेंट |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | टर्मिनल के लिए ओपन-सोर्स AI कोडिंग एजेंट |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | विस्तार-योग्य एजेंट जो किसी भी LLM से कोड इंस्टॉल, चलाता, संपादित और टेस्ट करता है |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | एजेंट टूलकिट: एकीकृत LLM API, एजेंट लूप, TUI और कोडिंग CLI |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | वह एजेंट जो आपके साथ बढ़ता है (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | "बैटरी शामिल" एजेंट हार्नेस (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | भूमिका निभाने वाले स्वायत्त एजेंटों को ऑर्केस्ट्रेट करने वाला फ़्रेमवर्क |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Python और .NET में एजेंट और मल्टी-एजेंट वर्कफ़्लो बनाने व तैनात करने के लिए Microsoft का फ़्रेमवर्क |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | DeepSeek का एजेंट हार्नेस जहाँ सब कुछ प्लगइन है |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | एजेंटों के बेड़े की योजना, संचालन और निगरानी, कार्य से मर्ज हुए PR तक |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | कोडिंग एजेंटों के बेड़े के साथ काम करने की जगह (डेस्कटॉप, मोबाइल और रिमोट) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | अलग-थलग git worktree और समीक्षक एजेंटों के साथ कोडिंग एजेंटों का समन्वय करने वाला कानबन बोर्ड |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | AI सहकर्मी, हर एक का अपना कंप्यूटर; हर क्रिया पहले तय और बाद में दर्ज होती है |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | ब्राउज़र चलाने वाले AI एजेंटों के लिए Python लाइब्रेरी |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | AI एजेंटों के लिए computer use CLI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | "एजेंट टूल्स के लिए OpenRouter" |

### 🧩 एजेंटों के लिए स्किल, प्लगइन और वर्कफ़्लो (11)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Anthropic द्वारा प्रबंधित उच्च-गुणवत्ता वाले Claude Code प्लगइन्स की आधिकारिक निर्देशिका |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | agentic स्किल्स के बड़े कैटलॉग को खोजने, चुनने और सत्यापित करने के लिए स्थानीय कंट्रोल प्लेन (CLI, स्थानीय MCP, प्लगइन) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Claude Code के लिए मल्टी-एजेंट कोड समीक्षा |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | कोडिंग एजेंटों के लिए विशेषज्ञ Blender स्किल्स, MCP-आधारित पाइपलाइन के साथ |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | कोडिंग एजेंटों के लिए संपादकीय डायग्राम डिज़ाइन (HTML + SVG) |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | AI एजेंटों के साथ सॉफ़्टवेयर डिज़ाइन और समीक्षा के लिए Google की खुली स्किल्स |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Claude Code को समन्वित एजेंटों के गेम स्टूडियो में बदलता है |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | कंपनी की तरह संरचित एजेंट संगठन: विभाग और इंस्टॉल करने योग्य स्किल्स |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | सॉफ़्टवेयर के पूरे जीवनचक्र के लिए एजेंट और स्किल्स वाला खुला QA/QE प्लेटफ़ॉर्म |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | वर्चुअल कार्यकारी टीम: 8 विशेषज्ञ Claude एजेंटों द्वारा समर्थित एक कार्यकारी व्यक्तित्व |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | ऐसा MCP सर्वर जिससे Claude, Cursor या Windsurf n8n वर्कफ़्लो बना सकें |

### 🛡️ सुरक्षा और सॉफ़्टवेयर विश्लेषण (8)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Claude Code को आक्रामक और रक्षात्मक सुरक्षा एजेंट में बदलता है |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | शुरुआती से उन्नत स्तर तक 70 साइबर सुरक्षा प्रोजेक्ट |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | एजेंट स्किल्स के लिए NVIDIA का सुरक्षा स्कैनर (प्रॉम्प्ट इंजेक्शन, डेटा रिसाव, सप्लाई चेन) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | MITRE ATT&CK, NIST CSF और अन्य ढाँचों से मैप की गईं एजेंटों के लिए सैकड़ों साइबर सुरक्षा स्किल्स |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | स्वतंत्र रूप से सत्यापित निष्कर्षों के साथ बहु-चरणीय सुरक्षा ऑडिट के लिए Cloudflare की स्किल |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | SEO, सुरक्षा, पहुँच-योग्यता और प्रदर्शन के लिए वेबसाइट क्रॉलर और विश्लेषक |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | एजेंटों के साथ रिवर्स इंजीनियरिंग, ऐप व्यवहार से नेटिव बाइनरी तक |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | किसी भी सॉफ़्टवेयर के काम करने का तरीका समझना और अपना बनाना |

### 🧠 AI मॉडल और इन्फ्रास्ट्रक्चर (5)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | फ़ाउंडेशन मॉडल के शोध और विकास के लिए खुला फ़्रेमवर्क |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | बड़े पैमाने पर एजेंटिक रीइन्फोर्समेंट लर्निंग प्रशिक्षण |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | OLMo पारिस्थितिकी तंत्र के लिए PyTorch बिल्डिंग ब्लॉक |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | DeepSeek मॉडलों के लिए उच्च-प्रदर्शन, बड़े पैमाने का इन्फ़रेंस फ़्रेमवर्क |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | बिना पुनः प्रशिक्षण के भाषा मॉडल में बदलाव (सेंसरशिप, चापलूसी आदि) |

### 🏢 व्यवसाय प्रबंधन और प्लेटफ़ॉर्म (6)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | मुक्त और ओपन-सोर्स ERP |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | ओपन-सोर्स बिज़नेस ऐप्स |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | ओपन-सोर्स मार्केटिंग ऑटोमेशन |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | AI एजेंटों के लिए बना ओपन-सोर्स CRM (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | एंड-टू-एंड डेवलपर प्लेटफ़ॉर्म: सोर्स कंट्रोल, CI/CD, एनवायरनमेंट और आर्टिफ़ैक्ट रजिस्ट्री |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | ओपन-सोर्स GPS ट्रैकिंग प्लेटफ़ॉर्म, 200+ डिवाइस प्रोटोकॉल |

### 🎓 शिक्षा और संदर्भ (4)

| Fork | मूल प्रोजेक्ट | भाषा | यह क्या है |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | कंप्यूटर साइंस के लिए निःशुल्क स्व-अध्ययन पथ (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | गणित के लिए निःशुल्क स्व-अध्ययन पथ (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | गणितीय एनिमेशन के लिए समुदाय का Python फ़्रेमवर्क |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | असेंबली में Atari 2600 खेलों का नमूना स्रोत कोड |
