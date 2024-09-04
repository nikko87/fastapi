from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class MeasurementBaseModel(BaseModel):
    value: Any
    address: str
    unit: str | None
    timestamp: str
    startTimestamp: str


class Temperature(MeasurementBaseModel):
    value: int


class Spo2(MeasurementBaseModel):
    value: int


class Weight(MeasurementBaseModel):
    value: float


class Height(MeasurementBaseModel):
    value: float


class BodyMassIndex(MeasurementBaseModel):
    value: float


class BPValue(BaseModel):
    systolic: int
    diastolic: int


class BloodPressure(MeasurementBaseModel):
    value: BPValue


class PulseRate(MeasurementBaseModel):
    value: int


class RespirationRate(MeasurementBaseModel):
    value: int


class ValueItem(BaseModel):
    type: str
    count: int


class Arrhythmia(MeasurementBaseModel):
    value: list[ValueItem]


class BloodGlucose(MeasurementBaseModel):
    value: int
    mealTiming: str
    mealType: str


class Measurement(BaseModel):
    temperature: Optional[Temperature] = None
    spo2: Optional[Spo2] = None
    weight: Optional[Weight] = None
    height: Optional[Height] = None
    bodyMassIndex: Optional[BodyMassIndex] = None
    bloodPressure: Optional[BloodPressure] = None
    pulseRate: Optional[PulseRate] = None
    respirationRate: Optional[RespirationRate] = None
    arrhythmia: Optional[Arrhythmia] = None
    bloodGlucose: Optional[BloodGlucose] = None


class Question(BaseModel):
    question: str
    type: str
    options: list[str]
    skippable: bool
    answer: Optional[str] = None
    choices: Optional[list[str]] = None


class Kiosk(BaseModel):
    id: str
    serialNumber: str
    hostname: str


class Sponsor(BaseModel):
    id: str
    name: str
    tradeName: Optional[str]


class Patient(BaseModel):
    id: str
    name: Optional[str]
    socialName: Optional[str]
    displayName: Optional[str]
    document: Optional[str]
    birthdate: Optional[str]


class Diabetes(BaseModel):
    type: str


class Medicine(BaseModel):
    nameAndDosage: str
    usage: bool
    timing: str


class AttendanceType(BaseModel):
    id: str
    name: str


class User(BaseModel):
    id: str
    displayName: str


class LastTracker(BaseModel):
    action: str
    user: User
    timestamp: str


class CreatedBy(BaseModel):
    id: str
    name: str
    socialName: Any
    displayName: str


class AttendedBy(BaseModel):
    id: str
    name: str
    socialName: Any
    displayName: str


class PatientDataVitaldocDTO(BaseModel):
    id: str
    attended: bool
    attendedAt: Optional[str]
    createdAt: str
    measurements: Measurement
    questions: Optional[list[Question]]
    riskClassification: str
    locator: Optional[str]
    kiosk: Optional[Kiosk] = None
    sponsor: Sponsor
    patient: Patient
    hasMedicalEvaluation: bool
    origin: str
    diabetes: Optional[Diabetes]
    medicines: Optional[list[Medicine]]
    attendanceType: Optional[AttendanceType] = None
    lastTracker: Optional[LastTracker] = None
    createdBy: Optional[CreatedBy] = None
    attendedBy: Optional[AttendedBy] = None


class PatientDataResponseVitaldocDTO(BaseModel):
    data: list[PatientDataVitaldocDTO]
    count: Optional[int] = None
