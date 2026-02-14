# HBnB Evolution

This repository contains the progressive development of the **HBnB Evolution** project. Unlike the standard console version, this project is architected into distinct layers and phases.

## 📂 Project Structure

### [Part 1: Technical Documentation](./part1/)
- **Focus:** Architecture design and business logic planning.
- **Output:** Detailed UML diagrams (Package, Class, Sequence) and flowcharts explaining the application layers.

### [Part 2: Business Logic & API](./part2/)
- **Focus:** Backend implementation using Python, Flask, and the Facade pattern.
- **Key Features:**
  - **RESTful API**: Endpoints for Users, Places, Reviews, and Amenities.
  - **Facade Pattern**: Abstraction layer between the API and the Business Logic.
  - **In-Memory Persistence**: A temporary storage system for development.
- **How to Run:** Navigate to the `part2` directory and follow the [Part 2 README](./part2/README.md).

### [Part 3: Database & Authentication](./part3/)
- **Focus:** Transitioning to persistent storage, securing the API, and refining relationships.
- **Key Features:**
  - **SQLAlchemy & SQLite**: Replaced in-memory storage with a relational database (SQLite for dev, adaptable to MySQL).
  - **JWT Authentication**: Secured endpoints using JSON Web Tokens via `Flask-JWT-Extended`.
  - **Security**: Password hashing using `bcrypt`.
  - **Complex Relationships**: Implemented One-to-Many and Many-to-Many relationships (e.g., Places ↔ Amenities).
- **How to Run:** Navigate to the `part3` directory and follow the [Part 3 README](./part3/README.md).

### [Part 4: Simple Web Client](./part4/)
- **Focus:** Building a dynamic frontend interface connected to the backend API.
- **Key Features:**
    - HTML/CSS frontend interface
    - JavaScript AJAX communication with API
    - JWT session handling via cookies
    - Dynamic places listing
    - Client-side price filtering
    - Place details rendering
    - Reviews displayed as cards
    - Add review form for authenticated users
- **How to Run:** Navigate to the `part4` directory and follow the [Part 4 README](./part4/README.md).

## 🛠 Technologies
- **Language:** Python 3.x
- **Framework:** Flask, Flask-RESTx, Flask-SQLAlchemy, Flask-JWT-Extended
- **Frontend:** HTML5, CSS3, JavaScript
- **Tools:** Git, Swagger UI, cURL, SQLite

## Authors
* **OWAYS Abdulhakim Aljbreen**
* **Rateel Mohammed Bahathek**
* **Raghad Abdullah Nassef**
