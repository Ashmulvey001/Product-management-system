
# Client–Server Product Management System

A client-server application for product management with Android scanning and AI integration.

---

## 🏗️ Architecture & Tech Stack

* **Client Application:** Android (Java/Kotlin)
  * Barcode & QR code scanning via device camera
  * REST API integration for real-time server communication
  * Shopping & purchasing list management UI
* **Backend Server:** Flask (Python)
  * RESTful API endpoints for user authentication & product management
  * Relational database for products, users, and lists
  * Dynamic AI Integration (Modular support for Anthropic Claude & OpenAI GPT models)

---

## 🎯 Key Features

* **Instant Lookup:** Rapid barcode/QR code product identification.
* **AI-Assisted Entry:** Automatic product metadata generation when an item is not found in the database.
* **Purchasing Lists:** Real-time list creation, updating, and sync across authenticated sessions.
* **Secure Authentication:** User profiles, encrypted credentials, and role management.

---

## 📅 Delivery Roadmap

* **Stage 1 & 2:** Repository setup, licensing, and public documentation *(Completed)*
* **Monday Preview (3rd):** Initial system architecture draft and structured monthly release schedule.
* **Phase 1 (MVP Delivery):** Core Flask server, basic Android scanning app, and dynamic AI fallback.
