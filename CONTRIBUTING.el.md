# Οδηγός συνεισφοράς

**Γλώσσες:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Ευχαριστούμε που σκέφτεστε να συνεισφέρετε σε αυτό το οικοσύστημα. Επειδή έχει σχεδιαστεί γύρω από την **παρατηρησιμότητα**, την **αναπαραγωγιμότητα**, την **ποιότητα local-first** και την **ιδεοδυναμία (idempotency)**, διατηρούμε υψηλές απαιτήσεις για την ακεραιότητα του κώδικα, ώστε το χαρτοφυλάκιο να παραμένει αντανάκλαση της σύγχρονης μηχανικής.

## Συνεισφορές που καλωσορίζουμε

- 🐛 **Διορθώσεις σφαλμάτων:** Επιλύστε εντοπισμένα προβλήματα, κατά προτίμηση με αυτοματοποιημένο τεστ (`pytest` κ.λπ.) που αποδεικνύει τη διόρθωση.
- 🚀 **Νέες λειτουργίες:** Βελτιώσεις αρχιτεκτονικής και νέες ενσωματώσεις, για παράδειγμα με n8n, Ollama ή LangGraph.
- 📖 **Τεκμηρίωση:** Σαφέστερες εξηγήσεις, μεταφράσεις ή ρητά διαγράμματα αρχιτεκτονικής (Mermaid ή draw.io).
- 🏗️ **Υποδομή:** Βελτιώσεις στις ροές DevOps (Kubernetes, CI/CD, Makefiles και ρύθμιση PWA).

## Ροή εργασίας (Git Flow)

Το έργο χρησιμοποιεί τυποποιημένη ροή εργασίας με feature branches:

1. Κάντε **fork** το αποθετήριο στον λογαριασμό σας.
2. **Δημιουργήστε ένα branch** για τη λειτουργία ή τη διόρθωσή σας από το πιο πρόσφατο branch `main`:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Αναπτύξτε** την αλλαγή σας.
   - Ακολουθήστε την καθιερωμένη προσέγγιση του αποθετηρίου. Αν χρησιμοποιεί `uv` για ροές Python υψηλής απόδοσης, μην το αντικαταστήσετε χωρίς να δικαιολογήσετε την αλλαγή.
   - Εκτελέστε τους υπάρχοντες μηχανισμούς προστασίας του έργου.
4. Κάντε **commit** τις αλλαγές σας. Χρησιμοποιούμε **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` κ.λπ.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. Κάντε **push** το branch σας:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Ανοίξτε ένα Pull Request (PR)** προς το branch `main` αυτού του αποθετηρίου.

## Πρότυπα κώδικα

- **Ανάπτυξη καθοδηγούμενη από τεστ (προαιρετική αλλά συνιστώμενη):** Συμπεριλάβετε εντολές εκτέλεσης των τεστ. Αν το αποθετήριο έχει GitHub Actions για `mypy` ή `bandit`, βεβαιωθείτε ότι οι αλλαγές περνούν τοπικά (`make test`, `make lint` ή τα διαθέσιμα σενάρια του οικοσυστήματος).
- **Docker-first:** Κάθε απαιτούμενη εξάρτηση πρέπει να τεκμηριώνεται και να είναι διαθέσιμη μέσω `docker-compose.yml`, ώστε η αρχιτεκτονική να ξεκινά σε λιγότερο από 60 δευτερόλεπτα ή να αποφεύγεται η περιττή τριβή τοπικής ρύθμισης.
- **Η τεκμηρίωση είναι υποχρεωτική:** Για μεγάλη αλλαγή, ενημερώστε το README και, όπου ταιριάζει, προσθέστε επεξηγηματικό διάγραμμα.
