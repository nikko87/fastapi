
# src/controllers/integration_controller.py
from use_cases.get_redirect_url import GetRedirectUrl


class IntegrationController:
    def __init__(self, get_redirect_url_use_case: GetRedirectUrl):
        self.get_redirect_url_use_case = get_redirect_url_use_case

    def get_redirect_url(self, patient_data: dict[str, any]) -> str:
        return self.get_redirect_url_use_case.execute(patient_data)
