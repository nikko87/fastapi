from interfaces.integration_interface import IntegrationInterface


class IrisAdapter(IntegrationInterface):
    def get_redirect_url(self, patient_data: dict[str, any]) -> str:
        return "https://videocalldoutorsalva.irisemergencia.com/VideoCall/VideoCall.html?MasterId=38&idChamada=ZjEzYzdhNGMtOWQ3OC00OTY0LTk4ZDYtYzFjYThjYWQxYjgy"
