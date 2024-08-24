from interfaces.integration_interface import IntegrationInterface


class JitsiAdapter(IntegrationInterface):
    def get_redirect_url(self, patient_data: dict[str, any]) -> str:
        return "https://meet.jit.si/telemed-drsalva-teste"
