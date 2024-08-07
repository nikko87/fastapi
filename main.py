from datetime import date, timedelta

import httpx
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tenacity import (retry, retry_if_result, stop_after_attempt,
                      stop_after_delay, wait_fixed)

app = FastAPI()

VITAL_DOC_BASE_URL = "https://h-mj.vitaldoc.com.br/admin/v1/attendance"
SPONSOR_ID = "1ce09866-c945-4f25-ba7a-f6bed5335b51"
TOKEN = "X-APPLICATION-TOKEN--bc73978d4d533a69c7a10b5fca98339799ebd50eae4560455d4793718baacb2c"

URL_TOLIFE = "https://api.clusterstaging.tolife.app/integration/api/v1/Telemedicine"
TOKEN_TOLIFE = "8319054d-0df2-414e-93f1-31e865279c2a"

URL_BASE_ROOM = (
    "https://patient.clusterstaging.tolife.app/telemedicine/drsalva-tolife/iframe"
)

# TODO: repetir request para api vitaldoc até pegar resultado


@app.get("/telemedicina/{user_id}")
async def telemedicine(user_id: str):

    try:
        attendances = await get_attendances_vitaldoc()
    except Exception as e:
        print(e)
        return {"error": "Ocorreu uma falha na integração com o sistema da VitalDoc."}

    try:
        attendance = find_attendance(attendances, user_id)
        room = await get_telemedicine_room(attendance)
    except Exception as e:
        print(e)
        return {"error": "Ocorreu uma falha na integração com o sistema da Tolife."}

    return RedirectResponse(f'{URL_BASE_ROOM}/{room["hash"]}')


def create_url(data: str) -> str:
    return f"{VITAL_DOC_BASE_URL}/history?start={data}&sponsorId={SPONSOR_ID}"


async def make_request_vitaldoc(client: httpx.AsyncClient, data: str):
    url = create_url(data)
    headers = {"Authorization": "Bearer " + TOKEN}

    r = await client.get(url, headers=headers)
    return r.json()


def attendances_not_found(value):
    return value['data'] == []


@retry(
    retry=retry_if_result(attendances_not_found),
    wait=wait_fixed(5),
    stop=stop_after_attempt(6)
)
async def get_attendances_vitaldoc():
    data = date.today().isoformat()

    async with httpx.AsyncClient() as client:
        r_json = await make_request_vitaldoc(client, data)
        print(r_json)

        if attendances_not_found(r_json):
            # tenta novamente com data de ontem
            data = (date.today()).isoformat()
            r_json = await make_request_vitaldoc(client, data)

        return r_json


def find_attendance(attendances: dict, user_id: str) -> dict:
    for data in attendances["data"]:
        patient_id = data["patient"]["id"]
        if patient_id == user_id:
            return data
    return {}


async def get_telemedicine_room(a: dict):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": TOKEN_TOLIFE}
        systolic = get_or_default(
            a, 'measurements.bloodPressure.value.systolic', 120)
        diastolic = get_or_default(
            a, 'measurements.bloodPressure.value.diastolic', 80)
        payload = {
            "patientName": get_or_default(a, 'patient.name', 'teste teste'),
            "socialName": "",
            "cpf": get_or_default(a, 'patient.document', '00000000000'),
            "birthDate": get_or_default(a, 'patient.birthdate', '1900-01-01'),
            "cns": "",
            "idGender": 4,
            "neighborhood": "",
            "city": "",
            "state": "",
            "phone": "",
            "email": "",
            "temperature": get_or_default(a, 'measurements.temperature.value', 36.5),
            "respiratoryFrequency": get_or_default(a, 'measurements.respirationRate.value', 15),
            "heartRate": get_or_default(a, 'measurements.pulseRate.value', 0),
            "glucose": 100,
            "saturation": get_or_default(a, 'measurements.spo2.value', 98),
            "bloodPressure": f'{systolic}/{diastolic}',
        }

        r = await client.post(URL_TOLIFE, headers=headers, json=payload)
        return r.json()


def get_or_default(nested_dict, nested_key, default_value):
    keys = nested_key.split('.')
    current_dict = nested_dict

    for key in keys:
        if key in current_dict and current_dict[key]:
            current_dict = current_dict[key]
        else:
            return default_value

    return current_dict


# url teste
# http://localhost:8000/telemedicina/d339eb6f-6421-4c83-a734-2a8decfc6ec8
