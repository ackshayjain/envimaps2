var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {lat: 26.8854479, lng: 75.6504697},
        mapTypeId: 'terrain'
    });


    // // Create a <script> tag and set the USGS URL as the source.
    // var script = document.createElement('script');
    //
    // // This example uses a local copy of the GeoJSON stored at
    // // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
    // script.src = 'https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js';
    // document.getElementsByTagName('head')[0].appendChild(script);

}

function updateDataPoints(data) {
    var heatmapData = [];
    for (var i = 0; i < data.length; i++) {
        var latLng = new google.maps.LatLng(data[i][0], data[i][1]);
        heatmapData.push(latLng);
    }
    var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData,
        dissipating: false,
        map: map
    });
}

// function eqfeed_callback(results) {
//     var heatmapData = [];
//     for (var i = 0; i < results.features.length; i++) {
//         var coords = results.features[i].geometry.coordinates;
//         var latLng = new google.maps.LatLng(coords[1], coords[0]);
//         heatmapData.push(latLng);
//         heatmapData.push(new google.maps.LatLng(28.7407673,77.0227279));
//         heatmapData.push(new google.maps.LatLng(26.8854479,75.6504697));
//         heatmapData.push(new google.maps.LatLng(26.9854479,75.4504697));
//         heatmapData.push(new google.maps.LatLng(25.3904409,75.7808301));
//     }
//     var heatmap = new google.maps.visualization.HeatmapLayer({
//         data: heatmapData,
//         dissipating: false,
//         map: map
//     });
// }
