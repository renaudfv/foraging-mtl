document.addEventListener("DOMContentLoaded", function(event) {
  // Zoom on Montreal, associate with DOM
  var map = L.map(
    'mapId',
    {
      preferCanvas: true // Ensures suitable performances
    }).setView([45.50866990,-73.55399250], 13);

  // Set background styling and source
  const tiles = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
    maxZoom: 18
  }).addTo(map);

  // To not create in memory for each line
  let trees, lat, lng, markers;
  // Asynchronously loads the data, if download:true provided
  Papa.parse('/static/arbres-publics.csv', {
    download: true,
    header: true, // Puts every line in an object
    complete: function(res) {
      trees = res.data;
      markers = L.markerClusterGroup({
        disableClusteringAtZoom: 17,
        chunkedLoading: true // For better performances
      });

      trees.forEach(function(tree) {
        lat = parseFloat(tree.Latitude);
        lon = parseFloat(tree.Longitude);

        if(!!lat && !!lon)
          markers.addLayer(L.circleMarker([lat, lon]));
      });
      map.addLayer(markers);
    },
    error: function(err) {
      console.error(err);
    }
  });
});
