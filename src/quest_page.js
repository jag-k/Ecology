function getUserCenter(){
    console.warn('[WARN]Implement getUserCenter');
    return [53.12,45.00];
}

// var plus = document.getElementById('plus');
function addBattery(){
    var battery = document.getElementsByClassName('img_battery');
    var batteries = document.getElementById('batteries');
    //debugger;
    batteries.insertBefore(battery[0].cloneNode(),battery[-1]); //FIXME: fix insert
}
// plus.addEventListener('click',function(){
//     addBattery();
// });
var map;
DG.then(function(){
    return DG.plugin('https://2gis.github.io/mapsapi/vendors/Leaflet.markerCluster/leaflet.markercluster-src.js')
}).then(function(){
    map = DG.map('map',{
        center:getUserCenter(),
        zoom:4
    });
    var markers = DG.markerClusterGroup();
    console.warn('[WARN] fix markers');
    for(i=0;i<15;i++){
        var title = 'test'+i;
        var marker = DG.marker([54+i/10,82.89],{title:title});
        marker.bindPopup(title);
        markers.addLayer(marker);
    }
    map.addLayer(markers);
});