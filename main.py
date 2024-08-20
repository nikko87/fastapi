import logging
import sys

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from adapters.iris_adapter import IrisAdapter
from controllers.integration_controller import IntegrationController
from use_cases.get_redirect_url import GetRedirectUrl

# from tolife import TolifeApi


app = FastAPI()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


# test IRIS
@app.get("/telemedicina/{user_id}")
async def telemedicine(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    url_redirect = controller.get_redirect_url('')

    logger.info(f"Sucesso. Usuário {
                user_id}." f"Redirecionado para {url_redirect}")

    return RedirectResponse(url=url_redirect)
