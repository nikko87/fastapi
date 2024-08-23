import pytest

from adapters.iris_adapter import IrisAdapter
from adapters.tolife_adapter import TolifeAdapter
from use_cases.get_redirect_url import GetRedirectUrl


def test_integ_iris():
    patient_data = {
        "patientName": "John Doe",
        "socialName": "",
        "cpf": "12345678900",
        "birthDate": "1985-05-15",
        "cns": "",
        "idGender": 4,
        "neighborhood": "",
        "city": "",
        "state": "",
        "phone": "",
        "email": "",
        "temperature": 37.2,
        "respiratoryFrequency": 18,
        "heartRate": 72,
        "glucose": 100,
        "saturation": 97,
        "bloodPressure": "130/85",
    }
    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)

    url = use_case.execute(patient_data)

    assert (
        url
        == "https://videocalldoutorsalva.irisemergencia.com/VideoCall/VideoCall.html?MasterId=38&idChamada=ZDNjM2RkNGUtNTE1My00MTIyLTk0NDEtYjQ2MGI4ZDU4ODA2"
    )


# @pytest.mark.asyncio
# async def test_integ_tolife():
#     patient_data = {
#         "patientName": "John Doe",
#         "socialName": "",
#         "cpf": "05973085945",
#         "birthDate": "1985-05-15",
#         "cns": "",
#         "idGender": 4,
#         "neighborhood": "",
#         "city": "",
#         "state": "",
#         "phone": "",
#         "email": "",
#         "temperature": 37.2,
#         "respiratoryFrequency": 18,
#         "heartRate": 72,
#         "glucose": 100,
#         "saturation": 97,
#         "bloodPressure": "130/85"
#     }
#     adapter = TolifeAdapter()
#     use_case = GetRedirectUrl(adapter)

#     url = await controller.get_redirect_url(patient_data)
#     print(url)

#     assert url.startswith(
#         "https://patient.clusterstaging.tolife.app/telemedicine/drsalva-tolife/iframe/")


@pytest.mark.asyncio
async def test_tolife_adapter():
    patient_data = {
        "patient": {
            "name": "John Doe",
            "document": "05973085945",
            "birthdate": "1980-01-01",
        },
        "measurements": {
            "temperature": {"value": 36.5},
            "pulseRate": {"value": 60},
            "spo2": {"value": 98},
            "bloodPressure": {"value": {"systolic": 120, "diastolic": 80}},
        },
    }
    adapter = TolifeAdapter()

    response = await adapter.get_telemedicine_room(patient_data)

    assert response["isError"] is False
