import requests
import json
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def run_test():
    # 1. Create a User (AS ADMIN)
    print("🔹 Creating Admin User...")
    unique_email = f"admin_{uuid.uuid4()}@verify.com"
    user_payload = {
        "first_name": "Admin",
        "last_name": "User",
        "email": unique_email,
        "password": "password123",
        "is_admin": True
    }
    
    user_res = requests.post(f"{BASE_URL}/users/", json=user_payload)
    if user_res.status_code != 201:
        print(f"❌ Failed to create user: {user_res.text}")
        return
    user_id = user_res.json()['id']
    print(f"✅ Admin User Created: {user_id}")

    # 2. LOGIN
    print("🔹 Logging in to get Token...")
    auth_res = requests.post(f"{BASE_URL}/auth/login", json={
        "email": unique_email, 
        "password": "password123"
    })
    
    if auth_res.status_code != 200:
        print(f"❌ Login failed: {auth_res.text}")
        return
        
    token = auth_res.json().get('access_token')
    headers = {"Authorization": f"Bearer {token}"}
    print(f"✅ Login Successful! Token acquired.")

    # 3. Create an Amenity
    print("🔹 Creating Amenity...")
    amenity_payload = {"name": "Super WiFi"}
    amenity_res = requests.post(f"{BASE_URL}/amenities/", json=amenity_payload, headers=headers)
    
    if amenity_res.status_code != 201:
        print(f"❌ Failed to create amenity: {amenity_res.text}")
        return
    amenity_id = amenity_res.json()['id']
    print(f"✅ Amenity Created: {amenity_id}")

    # 4. Create a Place WITH the Amenity
    print("🔹 Creating Place with Amenity...")
    place_payload = {
        "title": "Smart House",
        "description": "Has great WiFi",
        "price": 150.0,
        "latitude": 12.34,
        "longitude": 56.78,
        "owner_id": user_id,
        "amenities": [amenity_id]
    }
    
    place_res = requests.post(f"{BASE_URL}/places/", json=place_payload, headers=headers)
    
    if place_res.status_code != 201:
        print(f"❌ Failed to create place: {place_res.text}")
        return

    place_data = place_res.json()
    print(f"✅ Place Created: {place_data['id']}")

    # 5. Verify the Link
    print("🔹 Verifying Link...")
    linked_amenities = place_data.get('amenities', [])
    
    if linked_amenities and linked_amenities[0]['id'] == amenity_id:
        print(f"🎉 SUCCESS! Place has amenity: {linked_amenities[0]['name']}")
    else:
        print(f"❌ FAILED. Amenities list: {linked_amenities}")

if __name__ == "__main__":
    try:
        run_test()
    except ImportError:
        print("Please run: pip install requests")
