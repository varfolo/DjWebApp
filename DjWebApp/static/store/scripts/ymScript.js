ymaps.ready(init);



function init() {
    var myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 7
    });
    var myGeoObject = new ymaps.GeoObject({
        geometry: {
            type: "Point", // ��� ��������� - ����� 
            coordinates: [55.9, 37.8] // ���������� �����
        }
    });
    // ���������� ���������� �� �����.
    myMap.geoObjects.add(myGeoObject);
    myMap.geoObjects.add(myCircle);
}