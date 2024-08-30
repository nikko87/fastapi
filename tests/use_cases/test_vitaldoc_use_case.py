from use_cases.get_attendance_data_vitaldoc import GetAttendanceDataVitalDocUseCase


def test_get_attendances_use_case():
    use_case = GetAttendanceDataVitalDocUseCase
    
    data = use_case.execute()