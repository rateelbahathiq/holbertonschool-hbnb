function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return null;
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

function getAuthToken() {
    return getCookie('token');
}



async function loginUser(email, password) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html';
        } else {
            alert('Login failed. Wrong email or password.');
        }
    } catch (error) {
        console.error(error);
        alert('Error connecting to server');
    }
}



let allPlaces = [];

function checkAuthenticationForIndex() {
    const token = getAuthToken();
    const loginLink = document.getElementById('login-link');

    if (loginLink) {
        loginLink.style.display = token ? 'none' : 'block';
    }

    // Always fetch places
    fetchPlaces(token);
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            headers: token ? { Authorization: `Bearer ${token}` } : {}
        });

        if (!response.ok) throw new Error('Failed to fetch places');

        const places = await response.json();
        allPlaces = places;
        displayPlaces(places);
    } catch (error) {
        console.error(error);
        alert('Error loading places');
    }
}

function displayPlaces(places) {
    const list = document.getElementById('places-list');
    if (!list) return;

    list.innerHTML = '';

    places.forEach(place => {
        const div = document.createElement('div');
        div.className = 'place-card';
        div.dataset.price = place.price;

        const link = `place.html?id=${place.id}`;

        div.innerHTML = `
            <h3>${place.name}</h3>
            <p>${place.description || ''}</p>
            <p><strong>Location:</strong> ${place.location || ''}</p>
            <p><strong>Price:</strong> $${place.price}</p>
            <a href="${link}" class="details-button">View Details</a>
        `;

        list.appendChild(div);
    });
}

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    if (!priceFilter) return;

    priceFilter.addEventListener('change', (event) => {
        const maxPrice = event.target.value;

        const filtered = allPlaces.filter(place => {
            if (maxPrice === 'All') return true;
            return Number(place.price) <= Number(maxPrice);
        });

        displayPlaces(filtered);
    });
}



function checkAuthenticationForPlaceDetails() {
    const token = getAuthToken();
    const addReviewSection = document.getElementById('add-review');

    if (addReviewSection) {
        addReviewSection.style.display = token ? 'block' : 'none';
    }

    return token;
}

async function fetchPlaceDetails(token, placeId) {
    if (!placeId) return;

    try {
        const response = await fetch(
            `http://127.0.0.1:5000/api/v1/places/${placeId}`,
            {
                headers: token ? { Authorization: `Bearer ${token}` } : {}
            }
        );

        if (!response.ok) throw new Error('Failed to fetch place');

        const place = await response.json();
        displayPlaceDetails(place);
    } catch (error) {
        console.error(error);
        alert('Error loading place details');
    }
}

function displayPlaceDetails(place) {
    const section = document.getElementById('place-details');
    if (!section) return;

    section.innerHTML = '';

    const container = document.createElement('div');
    container.className = 'place-info';

    const amenities = place.amenities || [];
    const reviews = place.reviews || [];

    const amenitiesHTML =
        amenities.map(a => `<li>${a}</li>`).join('') ||
        '<li>No amenities</li>';

    const reviewsHTML =
        reviews
            .map(r => {
                const user = r.user || r.user_name || 'Anonymous';
                const comment = r.comment || r.text || '';

                return `
                <div class="review-card">
                    <p><strong>${user}</strong></p>
                    <p>${comment}</p>
                </div>
            `;
            })
            .join('') || '<p>No reviews yet</p>';

    container.innerHTML = `
        <h2>${place.name}</h2>
        <p>${place.description || ''}</p>
        <p><strong>Price:</strong> $${place.price}</p>

        <h3>Amenities</h3>
        <ul>${amenitiesHTML}</ul>

        <h3>Reviews</h3>
        ${reviewsHTML}
    `;

    section.appendChild(container);
}



function checkAuthenticationForAddReviewPage() {
    const token = getAuthToken();

    if (!token) {
        window.location.href = 'index.html';
        return null;
    }

    return token;
}

async function submitReview(token, placeId, reviewText, form) {
    try {
        const response = await fetch(
            'http://127.0.0.1:5000/api/v1/reviews',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({
                    place_id: placeId,
                    text: reviewText
                })
            }
        );

        if (response.ok) {
            alert('Review submitted successfully!');
            form.reset();
        } else {
            alert('Failed to submit review');
        }
    } catch (error) {
        console.error(error);
        alert('Error submitting review');
    }
}

function setupAddReviewForm() {
    const form = document.getElementById('review-form');
    if (!form) return;

    const token = checkAuthenticationForAddReviewPage();
    if (!token) return;

    const placeId = getPlaceIdFromURL();
    if (!placeId) return;

    form.addEventListener('submit', async event => {
        event.preventDefault();

        const textarea = document.getElementById('comment');
        const text = textarea ? textarea.value : '';

        await submitReview(token, placeId, text, form);
    });
}



document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async event => {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            await loginUser(email, password);
        });
    }

    if (document.getElementById('places-list')) {
        checkAuthenticationForIndex();
        setupPriceFilter();
    }

    if (document.getElementById('place-details')) {
        const token = checkAuthenticationForPlaceDetails();
        const placeId = getPlaceIdFromURL();
        fetchPlaceDetails(token, placeId);
    }

    setupAddReviewForm();
});
