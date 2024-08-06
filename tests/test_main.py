import pytest

from main import get_or_default, get_telemedicine_room


@pytest.mark.asyncio
async def test_get_telemedicine_room(monkeypatch):
    test_data = {
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
    expected = {
        "hash": "123456789",
        "room": "https://patient.clusterstaging.tolife.app/telemedicine/drsalva-tolife/iframe/123456789",
    }

    # async def mock_post(*args, **kwargs):
    #     return httpx.Response(200, json=expected)

    # monkeypatch.setattr(httpx.AsyncClient, 'post', mock_post)

    r = await get_telemedicine_room(test_data)
    print(r)

    assert r['isError'] is not True


def test_json_with_defaults():
    a = {
        "patient": {
            "name": "",
            "document": "05973085945",
            "birthdate": "1980-01-01",
        },
        "measurements": {
            # "temperature": {"value": 36.5},
            "pulseRate": {"value": 60},
            "spo2": {"value": 98},
            "bloodPressure": {"value": {"systolic": 120, "diastolic": 80}},
        },
    }

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
        "respiratoryFrequency": get_or_default(a, 'measurements.respirationRate.value', 16),
        "heartRate": get_or_default(a, 'measurements.pulseRate.value', 0),
        "glucose": 100,
        "saturation": get_or_default(a, 'measurements.spo2.value', 98),
        "bloodPressure": f'{systolic}/{diastolic}',
    }

    assert payload['patientName'] == 'teste teste'
    assert payload['temperature'] == 36.5
    assert payload['saturation'] == 98
