var map = L.map('map').setView([0,0], 1);
var currentZoomLevel = map.getZoom();

L.tileLayer('http://{s}.tile.cloudmade.com/37d359fe74f049e9983dcfb6c8aa7413/997/256/{z}/{x}/{y}.png', {
  maxZoom: 18,
  zindex:1,
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery ?<a href="http://cloudmade.com">CloudMade</a>'
})

L.tileLayer('http://hack.galv.in/tile/{y}/{x}/{z}', {
  minZoom:1,
  maxZoom:5,
  opacity:1.0,
  //attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery ?<a href="http://cloudmade.com">CloudMade</a>'
}).addTo(map);
