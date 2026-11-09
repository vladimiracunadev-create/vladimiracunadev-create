# 🛠️ Οδηγός τεχνικής αξιολόγησης

[← Από πού να ξεκινήσετε](../START_HERE.el.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · **Ελληνικά**

## Σε μία γραμμή

Δεν χρειάζεται να διαβάσετε κώδικα για να κρίνετε πώς σκέφτομαι: αρκεί να δείτε τι εκτελείται, τι δοκιμάζεται και τι δηλώνεται ως εκκρεμές.

## Τέσσερις διαδρομές των 10 λεπτών

| Διαδρομή | Για να δείτε… | Πώς |
|---|---|---|
| **A. Παρατηρησιμότητα και ενορχήστρωση** | Ροές εργασίας, μετρικές, πίνακες ελέγχου και guardrails σε 20 περιπτώσεις και 18+ μηχανές βάσεων δεδομένων | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Αναπαραγώγιμη υποδομή** | Εργαστήρια containers σε λειτουργία μέσα σε λεπτά | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Πράκτορες με τυποποιημένη κατάσταση** | 25 backends LangGraph, DEMO/LIVE, αλυσίδα επιμέλειας | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Προϊόν ψηφιακής εγκληματολογίας σε Rust** | Εγκαταστάτες και δυαδικά με checksums, χωρίς κλωνοποίηση | [Εκδόσεις RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Ενδείξεις ποιότητας που μπορείτε να επαληθεύσετε

| Ένδειξη | Πού να κοιτάξετε |
|---|---|
| Τεστ | GabySQL με 850 τεστ και fuzz 503,8 εκατ. ερωτημάτων χωρίς panics· Empresa Operativa Chile με 230 τεστ· Automa με 150 pytest |
| Εφοδιαστική αλυσίδα | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX και Scorecard, ανάλογα με το αποθετήριο |
| Τηλεμετρία | Μηδενική στα προϊόντα εγκληματολογίας και στο Empresa Operativa Chile, επαληθευμένη σε κάθε build |
| Διανομή | Εκδόσεις με checksums και τεκμήρια build· οι εμπορικές υπογραφές δηλώνονται ως εκκρεμείς |
| Ειλικρίνεια | Κάθε αποθετήριο δηλώνει την κατάστασή του και τι **δεν** κάνει |

Όλοι οι αριθμοί με την πηγή τους βρίσκονται στη [Επαληθευμένη κατάσταση](../../README.el.md#επαληθευμένη-κατάσταση).

## Πώς σχεδιάζω

- **Από το μοντέλο προς τα έξω:** πρώτα το πεδίο, η διεπαφή ως προβολή.
- **Παρατηρησιμότητα από την πρώτη μέρα:** `/health`, `/ready`, `/metrics` και ιχνηλασιμότητα.
- **Πραγματική ανθεκτικότητα:** ιδεοδυναμία, circuit breaker και ελεγχόμενη υποβάθμιση.
- **Πολύγλωσσο εκ σχεδιασμού:** γλώσσα και μηχανή ανά περίπτωση χρήσης.
- **Πρώτα το DX:** `doctor` και `smoke` ανά αποθετήριο· αν δεν εκτελείται εύκολα, δεν κάνει για βάση ομάδας.

## Πού να εμβαθύνετε

- [Στοίβα τεχνολογιών](../../README.el.md#-στοίβα-τεχνολογιών) που εντοπίστηκε στα αποθετήρια.
- [Δείτε ολόκληρο το οικοσύστημα](../ECOSYSTEM.el.md): κάθε προϊόν με την έκδοση, τα τεστ και την κυκλοφορία του.
- Τα forks τρίτων φυλάσσονται χωριστά και δεν μετρούν ως δικό μου έργο: [Forks έργων τρίτων](../ECOSYSTEM.el.md#forks).

## Επόμενο βήμα

Για αρχιτεκτονική αξιολόγηση ή τεχνική συζήτηση, γράψτε στο [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
