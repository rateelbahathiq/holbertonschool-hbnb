# HBnB Evolution - Part 2: Business Logic & API

This project is the second phase of the **HBnB Evolution** application. It implements the core Business Logic and a RESTful API using Flask and Flask-RESTx.

## 📂 Project Structure

The project follows a layered architecture pattern:

- **app/models/**: Business Logic Layer (User, Place, Review, Amenity entities).
- **app/persistence/**: Persistence Layer (In-memory repository for storage).
- **app/services/**: Service Layer (Facade pattern to manage logic between API and persistence).
- **app/api/v1/**: Presentation Layer (API endpoints).

## 🚀 Setup & Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone [https://github.com/oways-work/holbertonschool-hbnb](https://github.com/oways-work/holbertonschool-hbnb)
   cd holbertonschool-hbnb/part2
