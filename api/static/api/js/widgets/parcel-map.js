function ParcelMapWidget(config, kwargs) {
  var widget = MapWidget(config, kwargs);
  var parcel;

  widget.isDataValid = function(data) {
    return data.insee !== "" && data.section !== "" && data.number !== "";
  };

  widget.centerFromData = function(data) {
    if (!data.coordinates) return;
    return MapTools.geo.center.fromMultiPolygon(data.coordinates);
  };

  widget.postUpdate = function(data) {
    if (parcel) {
      widget.map.removeLayer(parcel);
    }
    parcel = L.geoJSON(
      {
        type: "Feature",
        geometry: {
          type: "MultiPolygon",
          coordinates: data.coordinates,
        },
        properties: {
          insee: data.insee,
          section: data.section,
          number: data.number,
        },
      },
      {
        style: {
          fillColor: "white",
          fillOpacity: 0.5,
          color: "#000",
          weight: 1,
        },
        onEachFeature: function(feature, layer) {
          var html = "";
          for (var k in feature.properties) {
            html +=
              "<div><strong>" +
              k +
              ":</strong> " +
              feature.properties[k] +
              "</div>";
          }
          layer.bindPopup(html);
        },
      }
    ).addTo(widget.map);
    widget.loading(false);
  };

  widget.map.on("click", function(e) {
    if (widget.loading()) {
      return;
    }
    widget.loading(true);
    MapTools.geo
      .parcelFromPos(e.latlng)
      .then(function(parcel) {
        MapTools.geo
          .parcelShape(parcel)
          .then(function(geom) {
            parcel.coordinates = geom.coordinates;
            widget.update(parcel);
          })
          .catch(widget.apiError);
      })
      .catch(widget.apiError);
  });

  widget.init(
    "Satellite",
    {
      Satellite: MapTools.layers.satellite(),
      IGN: MapTools.layers.ign(),
    },
    {
      Cadastre: MapTools.layers.cadastral(),
    },
    ["Cadastre"]
  );
}
