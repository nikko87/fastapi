from abc import ABC, abstractmethod
from typing import Any


class IntegrationInterface(ABC):

    @abstractmethod
    def get_redirect_url(self, patient_data: dict[str, Any]):
        pass
