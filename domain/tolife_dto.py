
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, StringConstraints
from typing_extensions import Annotated


class PatientDataTolifeDTO(BaseModel):
    cpf: Annotated[str, StringConstraints(pattern=r'^\d{11}$')] = Field(...)  # CPF deve ter 11 dígitos
    temperature: float = Field(default=36.5, gt=30, lt=45)  # Temperatura deve estar entre 30 e 45 graus
    respiratoryFrequency: int = Field(gt=0, default=15)  # Frequência respiratória deve ser maior que 0
    heartRate: int = Field(default=85, gt=0)  # Frequência cardíaca deve ser maior que 0
    glucose: int = Field(default=90, gt=0)  # Glicose deve ser maior que 0
    saturation: int = Field(default=98, ge=0, le=100)  # Saturação deve estar entre 0 e 100
    bloodPressure: str = Field(default='120/80')  # Pressão arterial padrão 120/80
    patientName: Optional[str] = None
    socialName: Optional[str] = None
    birthDate: Optional[str] = None
    cns: Optional[Annotated[str, StringConstraints(pattern=r'^\d{15}$')]] = None  # CNS deve ter 15 dígitos
    idGender: Optional[int] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    phone: Optional[Annotated[str, StringConstraints(pattern=r'^\d{10,11}$')]] = None  # Telefone deve ter 10 ou 11 dígitos
    email: Optional[EmailStr] = None  # Validação de email
