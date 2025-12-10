# 🔒 Malicious Website Detection using Flask & Machine Learning

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![REST API](https://img.shields.io/badge/REST-API-green)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

This project is a **Flask-based Malicious Website Detection System** that identifies **potentially harmful URLs in real time** using **Machine Learning and feature-engineered URL analysis**. The application calculates a **trust score** and classifies URLs as **Safe or Malicious**, simulating real-world **security monitoring and application support workflows**.

---

## 💡 Key Features

- 🧠 **Random Forest–based ML detection** for malicious URLs  
- 🔍 **Trust score system (0–100)** for URL risk evaluation  
- 🧾 Feature-based analysis including:
  - Suspicious keywords (`login`, `win`, `mod`, `update`, etc.)
  - IP address detection in URLs  
  - Dangerous file extensions (`.apk`, `.exe`, `.zip`, etc.)
  - Malicious query parameters (`token`, `session`, `id=`)  
  - HTTPS validation and URL length checks  
- 🌐 **Flask-powered web interface**
- 🔄 **REST-style request handling for URL scanning**
- ✅ **Result verification and validation workflow**
- 🛠 **Version controlled with Git & GitHub**

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **NumPy**
- **TF-IDF Vectorizer**
- **REST API Architecture**
- **Git & GitHub**
- **VS Code**
- **HTML + Jinja Templates**

---

## 👨‍💻 Project Responsibilities (Internship / Real-Time Exposure)

- Built and maintained a **Flask-based security application** for malicious website detection  
- Implemented **Random Forest–based URL classification** with **feature-engineered URL analysis**  
- Managed **REST API–based URL scanning and response handling**  
- Performed **request validation and result verification**  
- Used **Git & GitHub for version control and collaboration**  
- Gained exposure to **IT infrastructure, application support, and security workflows**

---

## 🔧 How It Works

1. User submits a URL through the web interface  
2. URL is vectorized using **TF-IDF character-level n-grams**  
3. Feature-engineered parameters (length, HTTPS, keywords, extensions) are added  
4. **Random Forest model predicts threat level**  
5. **Trust score is calculated** using heuristic rules  
6. Result is rendered on a styled results page  

---

## 📸 Screenshots

<img width="893" alt="Image" src="https://github.com/user-attachments/assets/c35bcf45-bf4d-44e2-868d-7d97f9fb1ab2" />

<img width="890" alt="Image" src="https://github.com/user-attachments/assets/c488ec73-2252-4fde-b160-6f88f58fccda" />

---

## ✅ Example URL Testing

### ✅ Safe URLs
https://www.google.com
https://www.github.com
https://www.amazon.com

shell
Copy code

### ❌ Malicious URLs
http://phishing-example.com/login?session=1234
http://modapk-download.com/free
http://fakebanking-login.com/secure-login

yaml
Copy code

---

## 📁 Project Structure

├── templates/
│ ├── index.html
│ └── result.html
├── app.py
├── model.pkl
├── requirements.txt

yaml
Copy code

---

## 📌 Future Enhancements

- Real-time **domain reputation API** integration  
- Advanced UI with **Bootstrap or Tailwind CSS**  
- **User authentication and URL scan history**  
- **Email alerts** for malicious detection  
- Cloud deployment with security monitoring  

---

## 📦 Installation & Usage

```bash
git clone https://github.com/yourusername/malicious-website-detector.git
cd malicious-website-detector
pip install -r requirements.txt
python app.py
```

📄 License
This project is licensed under the MIT License.
