
from domain.models import PatientData
from interfaces.integration_interface import IntegrationInterface


class IrisAdapter(IntegrationInterface):
    def get_redirect_url(self, patient_data: dict[str, any]) -> str:
        return "https://videocalldoutorsalva.irisemergencia.com/VideoCall/VideoCall.html?MasterId=38&idChamada=ZDNjM2RkNGUtNTE1My00MTIyLTk0NDEtYjQ2MGI4ZDU4ODA2"
