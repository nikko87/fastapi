from domain.tolife_dto import PatientDataTolifeDTO
from domain.vitaldoc_dto import PatientDataVitaldocDTO


def get_id_gender(vitaldoc_data: PatientDataVitaldocDTO) -> int:
    return 4


def map_vitaldoc_to_tolife(
    vitaldoc_data: PatientDataVitaldocDTO,
) -> PatientDataTolifeDTO:
    return PatientDataTolifeDTO(
        cpf=vitaldoc_data.patient.document,
        temperature=vitaldoc_data.measurements.temperature.value,
        heartRate=vitaldoc_data.measurements.pulseRate.value,
        glucose=vitaldoc_data.measurements.bloodGlucose.value,
        saturation=vitaldoc_data.measurements.spo2.value,
        bloodPressure=f"{vitaldoc_data.measurements.bloodPressure.value.systolic}"
        "/{vitaldoc_data.measurements.bloodPressure.value.diastolic}",
        patientName=vitaldoc_data.patient.name,
        socialName=vitaldoc_data.patient.socialName,
        birthDate=vitaldoc_data.patient.birthdate,
        cns=None,
        idGender=get_id_gender(vitaldoc_data),  # desconhecido
    )

    # TODO: implementar mapeamento dos demais campos
