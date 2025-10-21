const map = L.map('map').setView([55.75, 37.62], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

fetch('/places.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            onEachFeature: (feature, layer) => {
                layer.on('click', () => {
                    const placeId = feature.properties.id;
                    showPlaceDetails(placeId);
                });
            }
        }).addTo(map);
    });

function showPlaceDetails(placeId) {
    fetch(`/api/places/${placeId}/`)
        .then(response => response.json())
        .then(place => {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.add('active');
            sidebar.innerHTML = `
                <h2>${place.title}</h2>
                ${place.imgs.map(img => `<img src="${img}" class="place-image">`).join('')}
                <p>${place.description_short}</p>
                <p>${place.description_long}</p>
            `;
        });
}
