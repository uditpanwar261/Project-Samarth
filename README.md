# Project-Samarth
# 🌾 Project Samarth – Intelligent Q&A System for Agricultural and Climate Data

## 🧠 Overview
**Project Samarth** is an intelligent **Flask-based Q&A system** designed to interact with real Indian government datasets from **data.gov.in**.  
It allows users to ask natural language questions related to **agriculture and climate patterns** — and get **data-driven answers** with dynamic graphs.

This project is developed as part of the **AI-for-Good Challenge**, focusing on India's agricultural economy and its correlation with climate behavior.

---

## 🚀 Features
- 🧮 **Intelligent Question Processing** – Understands user queries in plain English (e.g., “Show rainfall trend in Odisha”).
- 🌧️ **Rainfall Analysis** – Uses IMD (India Meteorological Department) data to show year-wise rainfall trends.
- 🌾 **Crop Production Trends** – Displays total crop output across states based on agricultural datasets.
- 📊 **Dynamic Graphs** – Auto-generates visual trend graphs for rainfall or production using `matplotlib`.
- 🔍 **Dataset Traceability** – Each insight is backed by open government data (from data.gov.in).
- 💬 **Simple Chat Interface** – Type questions and get instant visual responses.

---
---

## ⚙️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Data Handling:** Pandas
- **Visualization:** Matplotlib
- **Datasets:** Data sourced from [data.gov.in](https://data.gov.in/)

---

## 🧩 How It Works
1. User enters a query like  
   → *“Show rainfall trend in Odisha”*  
2. Flask backend parses keywords (like `rainfall`, `Odisha`)  
3. Matches against datasets:
   - `rainfall.csv` → finds “SUBDIVISION = Odisha”
   - `crop_production.json` → finds “StateName = Odisha”
4. Generates graphs dynamically using `matplotlib`
5. Returns a natural language summary + chart to the frontend.

---

## 💻 How to Run Locally

### 1️⃣ Clone or download this repository
```bash
git clone https://github.com/uditpanwar261/Project-Samarth.git
cd Project-Samarth
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Flask app
bash
Copy code
python app.py
4️⃣ Open in browser
cpp
Copy code
http://127.0.0.1:5000/
Then try sample queries like:

“Show rainfall trend in Odisha”

“Show total output trend in West Bengal”

“Show crop production trend in Andhra Pradesh”

🧠 Sample Queries
Query Example	What It Does
“Show rainfall trend in Odisha”	Displays rainfall trend (year vs annual rainfall)
“Show rainfall trend in Kerala”	Shows Kerala’s rainfall pattern
“Show crop production trend in West Bengal”	Displays agricultural output over time
“Show total output trend in Andhra Pradesh”	Combines JSON data to show total yield

🎥 Loom Demo Video
👉 Add your 2-minute Loom video link here

(Demonstrate dataset overview, system design, and one working query.)

🔗 Data Sources
Crop Production Dataset – Ministry of Agriculture & Farmers Welfare
Rainfall Data – India Meteorological Department (IMD)

🏁 Summary
Project Samarth demonstrates the power of open government data — enabling data-backed insights into the agricultural economy and its relation with climate change.
This prototype shows how AI + data integration can help policymakers and researchers make informed, data-driven decisions.

![App Screenshot](https://github.com/uditpanwar261/Project-Samarth/blob/main/project%20saamarth.png)
