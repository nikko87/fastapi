from unittest.mock import AsyncMock, patch

import httpx
import pytest

from use_cases.get_attendance_data_vitaldoc import GetAttendanceData

mock_response = {
    "patient": {
        "name": "John Doe",
        "document": "05973085945",
        "birthdate": "2024-08-20",
    },
    "measurements": {
        "temperature": {"value": 36.5},
        "pulseRate": {"value": 60},
        "spo2": {"value": 98},
        "bloodPressure": {"value": {"systolic": 120, "diastolic": 80}},
    },
}


@pytest.mark.asyncio
@patch('main.make_request_vitaldoc', new_callable=AsyncMock)
async def test_make_request_vitaldoc(monkeypatch):
    # mock_make_request.return_value = mock_response

    async def mock_post(*args, **kwargs):
        return httpx.Response(200, json=mock_response)

    monkeypatch.setattr(httpx.AsyncClient, 'post', mock_post)

    use_case = GetAttendanceData()
    controller = ApiRequestController(use_case)
    r = await controller.request_data(httpx.AsyncClient(), mock_response)

    # assert r['patient']['name'] == mock_response['patient']['name']
    assert r == mock_response
