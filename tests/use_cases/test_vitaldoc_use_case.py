from datetime import date

import pytest

from use_cases.get_attendance_data_vitaldoc import GetAttendanceDataVitalDocUseCase


@pytest.mark.asyncio
async def test_get_attendances_use_case_execute():
    use_case = GetAttendanceDataVitalDocUseCase()

    user_id = "1ce09866-c945-4f25-ba7a-f6bed5335b51"
    data = await use_case.execute(user_id, date(2024, 8, 6))

    assert data["data"][0]["id"] == "1f898b54-09d9-486e-a253-cd74aa7dcbbd"


def test_get_yesterday():
    d = date(2024, 8, 6)

    use_case = GetAttendanceDataVitalDocUseCase()

    assert use_case.get_yesterday(d) == date(2024, 8, 5)


def test_create_vitaldoc_api_url():
    attendance_date = date(2024, 8, 6)
    user_id = "1ce09866-c945-4f25-ba7a-f6bed5335b51"

    use_case = GetAttendanceDataVitalDocUseCase()

    url = use_case.create_vitaldoc_api_url(attendance_date, user_id)

    assert (
        url
        == "https://h-mj.vitaldoc.com.br/admin/v1/attendance/history?start=2024-08-06&sponsorId=1ce09866-c945-4f25-ba7a-f6bed5335b51"
    )
