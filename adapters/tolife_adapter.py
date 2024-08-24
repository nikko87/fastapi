from typing import Any

import httpx

from interfaces.integration_interface import IntegrationInterface

URL_TOLIFE = "https://api.clusterstaging.tolife.app/integration/api/v1/Telemedicine"
TOKEN_TOLIFE = "8319054d-0df2-414e-93f1-31e865279c2a"

URL_BASE_ROOM = (
    "https://patient.clusterstaging.tolife.app/telemedicine/drsalva-tolife/iframe"
)


def get_or_default(nested_dict, nested_key, default_value):
    keys = nested_key.split(".")
    current_dict = nested_dict

    for key in keys:
        if key in current_dict and current_dict[key]:
            current_dict = current_dict[key]
        else:
            return default_value

    return current_dict


def create_headers() -> dict[str, str]:
    return {"Authorization": TOKEN_TOLIFE}


def create_payload(attendance_json: dict[str, Any]) -> dict[str, Any]:
    systolic = get_or_default(
        attendance_json, "measurements.bloodPressure.value.systolic", 120
    )
    diastolic = get_or_default(
        attendance_json, "measurements.bloodPressure.value.diastolic", 80
    )
    payload = {
        "patientName": get_or_default(attendance_json, "patient.name", "teste teste"),
        "socialName": "",
        "cpf": get_or_default(attendance_json, "patient.document", "00000000000"),
        "birthDate": get_or_default(attendance_json, "patient.birthdate", "1900-01-01"),
        "cns": "",
        "idGender": 4,
        "neighborhood": "",
        "city": "",
        "state": "",
        "phone": "",
        "email": "",
        "temperature": get_or_default(
            attendance_json, "measurements.temperature.value", 36.5
        ),
        "respiratoryFrequency": get_or_default(
            attendance_json, "measurements.respirationRate.value", 15
        ),
        "heartRate": get_or_default(attendance_json, "measurements.pulseRate.value", 0),
        "glucose": 100,
        "saturation": get_or_default(attendance_json, "measurements.spo2.value", 98),
        "bloodPressure": f"{systolic}/{diastolic}",
    }

    return payload


class TolifeAdapter(IntegrationInterface):

    async def get_redirect_url(self, patient_data: dict[str, Any]) -> str:
        response = await self.get_telemedicine_room(patient_data)
        return f"{URL_BASE_ROOM}/{response['hash']}"

    async def get_telemedicine_room(self, attendance_dict: dict[str, Any]):
        async with httpx.AsyncClient() as client:
            headers = create_headers()
            payload = create_payload(attendance_dict)

            r = await client.post(URL_TOLIFE, headers=headers, json=payload)
            return r.json()
