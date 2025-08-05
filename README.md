# PitIQ - Raspberry Pi BBQ Temperature Monitoring

Phase 1 Goal: Local-first temperature monitoring with **FastAPI** & **SQLite**.
Designed to run locally first, with no cloud dependency, and later deployable on Raspberry Pi 4 with 4–6 thermistor probes.

---

## 📦 Project Structure

```
PitIQ/
│
├─ app/
│   ├─ __init__.py
│   ├─ main.py          # FastAPI entry point
│   ├─ db.py            # SQLite connection & helper functions
│   ├─ probes.py        # Probe reading logic (simulated in Phase 1)
│   ├─ models.py        # Database schema and creation script
│   ├─ routes.py        # FastAPI routes
│   └─ static/          # Static JS/CSS for web dashboard
│
├─ tests/
│   └─ test_probes.py   # Placeholder for probe tests
│
├─ pitiq.db             # SQLite database (auto-created)
├─ requirements.txt      # Python dependencies
├─ README.md
└─ .gitignore
```

---

## 🚀 Setup Instructions (Windows + VSCode)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/moodywaters/PitIQ.git
cd PitIQ
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\Activate
```

> You should see `(venv)` in the terminal.

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Initialize the Database

```bash
python app/models.py
```

This will create `pitiq.db` with the required tables:

* **`probes`** – stores probe configurations
* **`temperatures`** – logs temperature readings

---

### 5️⃣ Verify the Setup

```bash
python app/db_test.py
```

You should see inserted test data for both **probes** and **temperatures**.

---

### 6️⃣ Git Workflow Notes

* **Do not commit your `venv` folder.** It is ignored via `.gitignore`.
* If you add new packages:

  ```bash
  pip freeze > requirements.txt
  git add requirements.txt
  git commit -m "Update requirements"
  git push origin main
  ```

---

## ✅ Next Step

Proceed to **Task 1.3**:
Simulate probe readings to generate fake BBQ temperatures and prepare for the FastAPI dashboard.
