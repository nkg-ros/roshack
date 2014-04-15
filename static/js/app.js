    console.log("ROSHACK");

    var map = L.map('map').setView([51.505, -0.09], 13);
    var currentZoomLevel = map.getZoom()

    L.tileLayer('http://{s}.tile.cloudmade.com/37d359fe74f049e9983dcfb6c8aa7413/997/256/{z}/{x}/{y}.png', {
      maxZoom: 18,
      zindex:1,
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery ?<a href="http://cloudmade.com">CloudMade</a>'
    })

    L.tileLayer('http://hack.galv.in/tile/{y}/{x}/{z}', {
      minZoom:1,
      maxZoom:5,
      zindex:2,
      opacity:1.0,
      //attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery ?<a href="http://cloudmade.com">CloudMade</a>'
    }).addTo(map);

    /*
    L.marker([51.5, -0.09]).addTo(map)
      .bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

    L.circle([51.508, -0.11], 500, {
      color: 'red',
      fillColor: '#f03',
      fillOpacity: 0.5
    }).addTo(map).bindPopup("I am a circle.");

    L.polygon([
      [51.509, -0.08],
      [51.503, -0.06],
      [51.51, -0.047]
    ]).addTo(map).bindPopup("I am a polygon.");
    */

    var popup = L.popup();

    function onMapClick(e) {
      popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
    }

    map.on('click', onMapClick);

