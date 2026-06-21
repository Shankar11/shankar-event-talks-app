# BigQuery Release Notes Web App Checklist

Checklist of project setup, requirements implementation, environment configuration, and verification steps.

---

## 📋 Task Checklist

- [x] **Project Scoping and Setup**
  - [x] View and analyze raw XML feed format ([bigquery_release_notes.xml](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/bigquery_release_notes.xml))
  - [x] Create [requirements.txt](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/requirements.txt) listing server dependencies
  - [x] Create [.gitignore](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/.gitignore) to exclude local cache and environment files
  - [x] Create [project_architecture_guide.md](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/project_architecture_guide.md) detailing architecture, component breakdown, and request-response flow lifecycle
  - [x] Create [README.md](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/README.md) for quick setup and project layout overview


- [x] **Backend Implementation ([app.py](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/app.py))**
  - [x] Connect feed parser and BeautifulSoup parsing engine
  - [x] Parse entries into micro-updates by `<h3>` tags
  - [x] Implement standard link sanitization (`target="_blank"`)
  - [x] Set up local cache logic (1-hour memory TTL cache)
  - [x] Add `/api/releases` JSON endpoints with force refresh (`?refresh=true`) support

- [x] **Frontend Design ([templates/index.html](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/templates/index.html))**
  - [x] Style dark mode layout (Slate-Obsidian gradient, glassmorphic panels)
  - [x] Add Search inputs and Category filter buttons (Features, Announcements, Issues, Deprecations)
  - [x] Style glowing animated checklist toggles for selecting updates
  - [x] Implement animated loading skeletons during fetches
  - [x] Implement Floating Selection Bar / Selected updates drawer
  - [x] Build Tweet Composer modal with character limit validation and X/Twitter intent sharing
  - [x] Add "Copy to Clipboard" button on cards and "Export to CSV" button next to refresh control
  - [x] Add theme toggler (light/dark mode) button and CSS variables overrides

- [x] **Environment Configuration**
  - [x] Build local virtual environment (`.venv`) using `uv venv`
  - [x] Install dependencies inside `.venv` using `uv pip install`
  - [x] Run Flask server inside virtual environment context (running on `http://127.0.0.1:5000`)

- [x] **Source Control (GitHub)**
  - [x] Initialize git repository and configure [.gitignore](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/.gitignore)
  - [x] Create initial commit on `main` branch
  - [x] Push project codebase to remote GitHub repository [shankar-event-talks-app](https://github.com/Shankar11/shankar-event-talks-app.git)

---

## 📝 Ongoing / Next Steps
- [ ] Review and debug bugs inside [demo_bad_code.py](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/demo_bad_code.py)

