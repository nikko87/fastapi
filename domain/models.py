
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PatientData:
    cpf: str
    temperature: float
    respiratoryFrequency: int
    heartRate: int
    glucose: int
    saturation: int
    bloodPressure: str
    patientName: str | None = None
    socialName: str | None = None
    birthDate: str | None = None
    cns: str | None = None
    idGender: int | None = None
    neighborhood: str | None = None
    city: str | None = None
    state: str | None = None
    phone: str | None = None
    email: str | None = None