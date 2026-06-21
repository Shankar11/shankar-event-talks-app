# BigQuery Release Explorer

A modern, glassmorphic single-page web application to browse, filter, search, and share Google Cloud BigQuery release notes. Built using a Python Flask backend and a responsive Vanilla HTML/CSS/JS frontend.

---

## ✨ Features

*   **Granular Release Feed**: Automatically parses official BigQuery release updates and splits daily release logs into atomic, tag-categorized notes.
*   **Vibrant Category Badges**: Color-coded badges for easy tracking of `Features`, `Announcements`, `Issues & Fixes`, and `Deprecations`.
*   **Intelligent Local Caching**: Fast 1-hour in-memory TTL cache with support for forced user-triggered updates.
*   **Interactive Multi-Selection Drawer**: Glow-styled checks enable you to select multiple updates to queue up.
*   **Custom Tweet Composer**: Real-time 280-character limitation validation checks and X/Twitter Web Intent integration.

---

## 🛠️ Tech Stack

*   **Backend**: Python 3.12, Flask, Feedparser, BeautifulSoup4, Requests
*   **Frontend**: Vanilla HTML5, CSS3 (Glassmorphic variables, flex/grid layouts), Vanilla ES6 JavaScript
*   **Package Management**: `uv` (Astral's ultra-fast resolver)

---

## 🚀 Quick Start

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed.

### Setup & Run
1.  **Clone this repository**:
    ```bash
    git clone https://github.com/Shankar11/shankar-event-talks-app.git
    cd shankar-event-talks-app
    ```
2.  **Initialize Virtual Environment**:
    ```bash
    uv venv
    ```
3.  **Install dependencies**:
    ```bash
    uv pip install -r requirements.txt
    ```
4.  **Launch the development server**:
    ```bash
    .venv\Scripts\python.exe app.py
    ```
5.  **Access the application** at:
    *   🚀 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Structure

*   [app.py](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/app.py): Entry point, routing, cache controller, and parsing module.
*   [templates/index.html](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/templates/index.html): SPA dashboard with responsive grids, selection dock, and composer modal.
*   [requirements.txt](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/requirements.txt): List of python requirements.
*   [task.md](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/task.md): Project task checklists.
*   [project_architecture_guide.md](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/project_architecture_guide.md): In-depth system design document.
*   [implementation_plan.md](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/implementation_plan.md): Functional and aesthetic style guides.
