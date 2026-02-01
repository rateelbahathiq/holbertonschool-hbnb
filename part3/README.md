<<<<<<< HEAD
# HBnB - Part 3: Database & Relationships

This project is the **third phase** of the HBnB (Holberton BnB) application. In this phase, we have transitioned from simple file-based storage to a robust **SQL Database** using SQLAlchemy. We have also implemented complex database relationships (One-to-Many, Many-to-Many) and secured the API with JWT Authentication.

## 🏗 Architecture

The application is built using a layered architecture to ensure separation of concerns:

* **API Layer (`app/api`):** Handles HTTP requests, input validation, and sends JSON responses. Built with `Flask-RESTx`.
* **Service Layer (`app/services`):** Contains the business logic (e.g., creating users, verifying passwords, linking amenities).
* **Persistence Layer (`app/models`):** Defines the SQL database schema using `SQLAlchemy`.
* **Database:** SQLite (for development), easily switchable to MySQL/PostgreSQL.

## 🚀 Key Features

* **User Authentication:** Secure login system using JWT (JSON Web Tokens). Passwords are hashed using `bcrypt`.
* **Database Relationships:**
    * **Users ↔ Places:** A User can own multiple Places.
    * **Places ↔ Reviews:** A Place can have many Reviews.
    * **Places ↔ Amenities:** A Place can have many Amenities (e.g., WiFi, Pool).
* **RBAC (Role-Based Access Control):** Only Admins can create new Amenities.
* **Swagger Documentation:** Auto-generated interactive API documentation.

## 🛠 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Clone the Repository
```bash
git clone [https://github.com/yourusername/holbertonschool-hbnb.git](https://github.com/yourusername/holbertonschool-hbnb.git)
cd holbertonschool-hbnb
=======
# HBnB Evolution – Part 3: Security & Configuration

This project is the third phase of the **HBnB Evolution** application.  
In this phase, the application is extended with **secure password handling**, **application configuration**, and preparation for **JWT-based authentication**, while maintaining a clean, layered architecture.


## 📂 Project Structure


## 🚀 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/oways-work/holbertonschool-hbnb](https://github.com/oways-work/holbertonschool-hbnb)
   cd holbertonschool-hbnb/part3
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
