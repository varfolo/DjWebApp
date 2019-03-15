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
    // Размещение геообъекта на карте.

    myRectangle = new ymaps.Rectangle([
        // Задаем координаты диагональных углов прямоугольника.
        [55.66, 37.60],
        [55.71, 37.69]
    ], {
            //Свойства
            hintContent: 'Перетащи меня!',
            balloonContent: 'Прямоугольник'
        }
        , {
            // Опции.
            // Можно перетаскивать        
            draggable: true,
            // Цвет и прозрачность заливки.
            fillColor: '#7df9ff33',
            // Дополнительная прозрачность заливки..
            // Итоговая прозрачность будет не #33(0.2), а 0.1(0.2*0.5).
            fillOpacity: 0.5,
            // Цвет обводки.
            strokeColor: '#0000FF',
            // Прозрачность обводки.
            strokeOpacity: 0.5
        });
    myMap.geoObjects.add(myGeoObject);
    myMap.geoObjects.add(myRectangle);


    objectManager = new ymaps.ObjectManager();

    // Загружаем GeoJSON файл с описанием объектов.
    $.getJSON('../../static/store/scripts/data.json')
        .done(function (geoJson) {
            // Добавляем описание объектов в формате JSON в менеджер объектов.
            objectManager.add(geoJson);
            // Добавляем объекты на карту.
            myMap.geoObjects.add(objectManager);
        });
}