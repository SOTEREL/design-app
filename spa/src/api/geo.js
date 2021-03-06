import axios from "axios";
import Gp from "geoportal-access-lib";

export const getCadastralParcelShape = (insee, section, number) => {
  // 12 -> 0012
  number = `000${number}`.slice(-4);
  return axios
    .get("https://apicarto.ign.fr/api/cadastre/parcelle", {
      params: {
        apikey: process.env.VUE_APP_GEOPORTAL_API_KEY,
        code_insee: insee,
        section: section,
        numero: number,
      },
    })
    .then(resp => resp.data);
};

export const getCadastralParcelFromPos = position =>
  new Promise((resolve, reject) => {
    Gp.Services.reverseGeocode({
      apiKey: process.env.VUE_APP_GEOPORTAL_API_KEY,
      position: { x: position.lng, y: position.lat },
      filterOptions: {
        type: ["CadastralParcel"],
      },
      onSuccess: resp => {
        const parcel = resp.locations[0];
        if (parcel === undefined) {
          reject("No parcels found.");
        }
        resolve({
          insee: parcel.placeAttributes.insee,
          section: parcel.placeAttributes.section,
          number: parcel.placeAttributes.number,
        });
      },
      onFailure: reject,
    });
  });
