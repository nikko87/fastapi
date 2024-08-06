from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Temperature(BaseModel):
    value: float
    unit: str
    address: str
    timestamp: str
    startTimestamp: str


class Spo2(BaseModel):
    value: int
    address: str
    timestamp: str
    startTimestamp: str


class Weight(BaseModel):
    value: float
    unit: str
    address: str
    timestamp: str
    startTimestamp: str


class Height(BaseModel):
    value: float
    unit: str
    address: str
    timestamp: str
    startTimestamp: str


class BodyMassIndex(BaseModel):
    value: float
    address: str
    timestamp: str
    startTimestamp: str


class Value(BaseModel):
    systolic: int
    diastolic: int


class BloodPressure(BaseModel):
    value: Value
    unit: str
    address: str
    timestamp: str
    startTimestamp: str


class PulseRate(BaseModel):
    value: int
    address: str
    timestamp: str
    startTimestamp: str


class Measurements(BaseModel):
    temperature: Optional[Temperature]
    spo2: Optional[Spo2]
    weight: Optional[Weight]
    height: Optional[Height]
    bodyMassIndex: Optional[BodyMassIndex]
    bloodPressure: Optional[BloodPressure]
    pulseRate: Optional[PulseRate]


class Question(BaseModel):
    question: str
    type: str
    options: List[str]
    skippable: bool
    answer: str


class Kiosk(BaseModel):
    id: str
    serialNumber: str
    hostname: str


class AttendanceType(BaseModel):
    id: str
    name: str


class Sponsor(BaseModel):
    id: str
    name: str
    tradeName: str


class Patient(BaseModel):
    id: str
    name: str
    socialName: Any
    displayName: str
    document: str
    birthdate: str


class Data(BaseModel):
    id: str
    attended: bool
    attendedAt: Any
    createdAt: str
    measurements: Measurements
    questions: List[Question]
    riskClassification: str
    locator: str
    kiosk: Kiosk
    attendanceType: AttendanceType
    sponsor: Sponsor
    patient: Patient
    hasMedicalEvaluation: bool
    origin: str
    diabetes: Any
    medicines: Any


class ApiVitalDocResponse(BaseModel):
    data: Optional[List[Data]] = None
