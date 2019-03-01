ymaps.ready(init);



function init() {
    var myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 7
    });
    var myGeoObject = new ymaps.GeoObject({
        geometry: {
            type: "Point", // тип геометрии - точка 
            coordinates: [55.9, 37.8] // координаты точки
        }
    });

    var myCircle = new ymaps.GeoObject({
        geometry: {
            type: "Circle",
            coordinates: [55.76, 37.64],
            radius: 10000
        }
    });
    // Размещение геообъекта на карте.
    myMap.geoObjects.add(myGeoObject);
    myMap.geoObjects.add(myCircle);
}