# 🔒 Malicious URL Detector using Flask & Machine Learning

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![HTML](https://img.shields.io/badge/HTML-Templates-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

A Flask web application that detects **potentially malicious URLs** using a combination of **Machine Learning** and **heuristic rules**. The app computes a **trust score** and flags suspicious URLs based on several risk indicators like keywords, file extensions, HTTPS usage, and more.

---

## 💡 Features

- 🧠 **Machine Learning detection** with `RandomForestClassifier`
- 🔍 **Trust score system** (0–100) for URL safety evaluation
- 🧾 Checks for:
  - Suspicious keywords (e.g., `login`, `win`, `mod`, `update`)
  - IP address presence in URL
  - Dangerous file extensions (`.apk`, `.exe`, `.zip`, etc.)
  - Suspicious query parameters (`token`, `id=`, `session`, etc.)
  - Domain reputation
  - HTTPS usage and URL length
- 🌐 **Web interface** built with Flask and HTML templates

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **NumPy**
- **TfidfVectorizer**
- **HTML + Jinja Templates**

---

## 📸 Screenshots *(optional)*

> Add screenshots of `index.html` and `result.html` pages here.

---

## 🔧 How It Works
URL input is vectorized with TF-IDF (character-level n-grams)

Heuristic features (length, https, etc.) are added

Model predicts if URL is malicious

Trust score is calculated based on multiple rules

Result is rendered on a styled result page

Visit the app: http://127.0.0.1:5000/

---

## 📁 Project Structure
pgsql
Copy
Edit
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── requirements.txt

---

## ✅ Example URLs
# Safe:

https://www.google.com

https://www.github.com

https://www.amazon.com

# Malicious:

http://phishing-example.com/login?session=1234

http://modapk-download.com/free

http://fakebanking-login.com/secure-login

---

## 📌 Future Enhancements
Real-time domain reputation API integration

Responsive UI with Bootstrap or Tailwind

User login and URL history log

Email alerts for suspicious URL detection

---

## 📦 Installation & Usage

```bash
git clone https://github.com/yourusername/url-safety-detector.git
cd url-safety-detector
pip install -r requirements.txt
python app.py

