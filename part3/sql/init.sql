-- User Table
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Place Table
CREATE TABLE IF NOT EXISTS places (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- Review Table
CREATE TABLE IF NOT EXISTS reviews (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INTEGER NOT NULL,
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    UNIQUE(user_id, place_id)
);

-- Amenity Table
CREATE TABLE IF NOT EXISTS amenities (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Place-Amenity Join Table
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);

-- Initial Data (Admin User)
-- Password hash for 'admin1234' (example hash)
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES ('36c9050e-577e-44d2-a4f6-bd98e5d51327', 'Admin', 'HBnB', 'admin@hbnb.io', '$2b$12$YourHashedPasswordHere...', TRUE);

-- Initial Data (Amenities)
INSERT INTO amenities (id, name) VALUES (lower(hex(randomblob(16))), 'WiFi');
INSERT INTO amenities (id, name) VALUES (lower(hex(randomblob(16))), 'Swimming Pool');
INSERT INTO amenities (id, name) VALUES (lower(hex(randomblob(16))), 'Air Conditioning');
