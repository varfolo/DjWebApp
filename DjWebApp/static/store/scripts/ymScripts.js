ymaps.ready(init);



//function init() {
//    var myMap = new ymaps.Map("map", {
//        center: [55.76, 37.64],
//        zoom: 7
//    });
//    var myGeoObject = new ymaps.GeoObject({
//        geometry: {
//            type: "Point", // ��� ��������� - ����� 
//            coordinates: [55.9, 37.8] // ���������� �����
//        }
//    });
//    // ���������� ���������� �� �����.
//    myMap.geoObjects.add(myGeoObject);
//}


function init() {
    var myMap = new ymaps.Map('map', {
        center: [55.76, 37.64],
        zoom: 10
    }, {
            searchControlProvider: 'yandex#search'
        }
        //,
        //{
        //    projection: ymaps.projection.sphericalMercator
        //}
    ),
        objectManager = new ymaps.ObjectManager({
            // ����� ����� ������ ����������������, ���������� �����.
            clusterize: false,
            // ObjectManager ��������� �� �� �����, ��� � �������������.
            gridSize: 32,
            clusterDisableClickZoom: true
        });

    // ����� ������ ����� ��������� �������� � ���������,
    // ��������� � �������� ���������� ObjectManager.
    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        //url: "/static/store/scripts/data.json"
        url: "/static/store/data/pareas.json"
    }).done(function (data) {
        objectManager.add(data);
    });
};