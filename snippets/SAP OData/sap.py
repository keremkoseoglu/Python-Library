import requests
from material import Material

class Sap:

    _MATERIAL_URL = "/sap/opu/odata/sap/ZMM_KALIPSO_SRV/EANSet?$format=json&$top=10"
    _SAP_URL = "http://10.1.3.190:8000"
    _SAP_USER = "secret"
    _SAP_PASS = "secret"

    def __init__(self):
        pass

    def get_material_list(self):

        output = []

        url = self._SAP_URL + self._MATERIAL_URL
        resp = requests.get(url, auth=(self._SAP_USER, self._SAP_PASS))

        json = resp.json()

        results = json["d"]["results"]
        for result in results:
            material = Material()
            material.matnr = result["Matnr"]
            material.meinh = result["Meinh"]
            material.ean11 = result["Ean11"]
            output.append(material)

        return output