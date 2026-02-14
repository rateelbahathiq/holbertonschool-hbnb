# HBnB – Part 4: Frontend Integration & Client Interaction

This project is the fourth phase of the **HBnB Evolution** application.  
In this phase, we implemented the **frontend interface** and connected it to the backend API. The application now supports authentication, dynamic content rendering, and user interaction using JavaScript and AJAX.

The goal of Part 4 is to transform the backend API into a usable web application.

---

## 🏗 Architecture Overview



Frontend stack:

- HTML5 (semantic structure)
- CSS3 (custom styling)
- JavaScript (AJAX + DOM manipulation)

The frontend dynamically loads:

- Places list
- Place details
- Reviews
- Authentication state

The application uses JWT tokens stored in cookies to maintain user sessions.

---

## 🚀 Key Features

### 🔐 Authentication
- Login via API
- JWT token stored in browser cookies
- Session persists across pages
- Login link hidden when authenticated

### 🏠 Dynamic Places List
- Fetches places from API
- Renders place cards dynamically
- Client-side filtering by price
- No page reload required

### 📄 Place Details Page
- Loads place data using URL ID
- Displays amenities and reviews
- Reviews rendered as cards
- Add review option only for authenticated users

### ✍ Add Review
- Only authenticated users allowed
- Redirects guests to index
- Sends review via AJAX POST
- Displays success/error feedback

### 🎨 UI Features
- Card-based layout
- Responsive structure
- Custom favicon
- Header/footer styling
- Image assets included locally

---

## 📂 Project Structure


