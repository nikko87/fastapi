
from interfaces.integration_interface import IntegrationInterface


class GetRedirectUrl:

    def __init__(self, adapter: IntegrationInterface):
        self.adapter = adapter

    def execute(self, patient_data: dict[str, any]) -> str:
        return self.adapter.get_redirect_url(patient_data)
