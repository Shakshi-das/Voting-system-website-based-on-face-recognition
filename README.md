
# 🗳️ Voting System Website Using Face Recognition

A secure, web-based smart voting system that uses real-time **facial recognition** for voter authentication, enhancing election integrity by reducing fraud, manual errors, and inefficiencies. This project leverages **OpenCV**, **FastAP**, **Spring Boot** and face recognition libraries to offer a modern, tamper-resistant alternative to traditional voting processes.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#%EF%B8%8F-system-architecture)
- [Getting Started](#%EF%B8%8F-getting-started)
- [API Endpoints](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
---

## 📖 Overview

This project introduces an innovative **facial recognition-based voting platform** that allows voters to securely authenticate and cast votes through a web interface. It eliminates the need for manual ID verification, supports **real-time face scanning**, and ensures high security through **JWT**, **OAuth2**, and **data encryption**.

🔐 **Key Benefits**:
- Enhanced security and transparency
- Real-time authentication
- Voter-friendly and accessible interface
- Compliance with privacy laws (e.g., GDPR)

---

## 🚀 Features

### 🔐 Core Voting Flow
- **User Registration** with biometric (facial) data
- **Login Authentication** using face recognition + password
- **Vote Casting Interface** with candidate confirmation
- **Candidate Management**: Admins can add, update, and manage candidate information.
- **Vote Casting**: Authenticated voters can cast their votes securely.
- **One-Vote Policy**: Ensures that each voter can vote only once.
- **Admin Dashboard**: View statistics, manage voter registrations, and oversee election data.
- **Results Tallying**: Automatically count and display election results with integrity.

---

### ⚙️ Security & Verification
- Facial recognition via Haar Cascade + LBPH (OpenCV)
- Liveness detection (blink/head movement)
- End-to-end encryption & JWT session management
- GDPR-compliant data handling

### 🌐 Admin Panel
- Secure login for election officers
- Real-time monitoring of voter activity
- Access to logs and audit trails

---

## 🧰 Tech Stack

| Layer        | Technology                        |
|-------------|-----------------------------------|
| **Frontend** | HTML, CSS, JS, Bootstrap     |
| **Backend**  | FastAPI, Spring Boot, JWT, OAuth2          |
| **Database** | MySQL / MongoDB    |
| **Face Recognition** | OpenCV (Haar Cascade, LBPH) |
| **Deployment** |    Uvicorn server     |

---

## 🏗️ System Architecture

- **Frontend** captures user data and facial image
- **Backend** authenticates via face match & manages session
- **Database** stores encrypted credentials and vote logs
- **Authentication** uses facial match + optional 2FA
- **Vote Casting** stores encrypted vote after validation

### 🔄 Data Flow Diagram (DFD Level 0)
1. **User → Registration** → Store facial + ID data
2. **User → Login** → Face verification → JWT token issued
3. **User → Vote** → Submit & store encrypted vote
4. **Admin → Dashboard** → Monitor system + logs

---

## ⚙️ Getting Started

> 🔧 **Note:** Project is still under active development. Setup instructions may evolve.

### Prerequisites
- Java 11+ (for Spring Boot)
- MySQL/MongoDB
- Python & OpenCV (for face data capture)
- pip

### Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Shakshi-das/Voting-system-website-based-on-face-recognition.git
   cd Voting-system-website-based-on-face-recognition
   ```

2. **Run backend (Spring Boot):**
   ```bash
   cd backend
   ./mvnw spring-boot:run
   ```

3. **Face Recognition Module (Python):**
   - Run training and recognition scripts using OpenCV.
   - Ensure Haar Cascade XML and LBPH training data are correctly configured.

---


## 📡 API Endpoints

### Authentication

* `POST /register-html/`: Register a new voter with facial data.
* `POST /login-html/`: Authenticate a voter using facial recognition.
* `POST /index-html/`: Home page of the site

### Voting

* `GET /candidates/`: Retrieve the list of candidates.
* `POST /vote/`: Cast a vote for a verified user.

### Admin

* `GET /admin/vote_results/`: View election results.
* `GET /admin/voters/`: View registered voters.

---

## 🔮 Future Enhancements

- 🧠 **AI-based liveness detection** (deepfake prevention)
- 📱 **Mobile app** with camera-based authentication
- 🗣️ **Voice/multilingual support** for accessibility
- ☁️ **Cloud deployment** for national-scale elections
---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
