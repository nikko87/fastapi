
from abc import ABC, abstractmethod


class IntegrationInterface (ABC):

    @abstractmethod
    def get_redirect_url(self, patient_data: dict[str, any]):
        pass