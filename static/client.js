document.addEventListener("DOMContentLoaded", function(event) {
  // Zoom on Montreal
  var map = L.map('mapId').setView([45.50866990,-73.55399250], 13);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
});



