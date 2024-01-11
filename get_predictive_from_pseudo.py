#script dostane na vstupe prediktivne čislo, napr. 3d4-21
#pozrie sa do pseudoy_table a nájde pseudo prediktívne číslo: mmci_predictive_514d5162-9f59-4ed0-91b3-f52797d522db
#nájde cestu k uloženej zložke na SC, ktorá obsahuje dáta pre dané prediktívne číslo:
# /muni-ss/OrganisedRuns/2021/MiSEQ/02340/210909_M02340_0270_000000000-JVYB6/Samples/mmci_predictive_514d5162-9f59-4ed0-91b3-f52797d522db
import json
import os

predictive = "3d4-21"

pseudo_table_path = "pseudo_table_predictive.json"
with open(pseudo_table_path, "r") as file:
    pseudo_table = json.load(file)

def find_predictive(predictive):
    for item in pseudo_table.get("predictive", []):
        if item.get("predictive_number") == predictive:
            return item.get("pseudo_number")
    return "No pseudo-predictive found."

def find_seq_data_path(pseudo_predictive, aktualna_zlozka):
    OrganisedRuns = os.listdir(aktualna_zlozka)
    for year in OrganisedRuns:
        runs = os.listdir(aktualna_zlozka + "/" + year + "/MiSEQ/02340")
        for run in runs:
            pseudo_predictives = os.listdir(aktualna_zlozka + "/" + year + "/MiSEQ/02340/" + run + "/Samples")
            for ps_id in pseudo_predictives:
                if ps_id == pseudo_predictive:
                    return aktualna_zlozka + "/" + year + "/MiSEQ/02340/" + run + "/Samples/" + ps_id


pseudo_predictive = find_predictive(predictive)
print("Prediktívne číslo je: ", predictive)
print("Pseudo prediktívne čislo je: ", pseudo_predictive)
print("Cesta k zložke s dátami k prediktivnemu čislu je: ", find_seq_data_path(pseudo_predictive, "OrganisedRuns"))

