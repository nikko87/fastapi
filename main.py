import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from adapters.iris_adapter import IrisAdapter
from adapters.jitsi_adapter import JitsiAdapter
from controllers.integration_controller import IntegrationController
from use_cases.get_redirect_url import GetRedirectUrl

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# from tolife import TolifeApi


app = FastAPI()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


@app.middleware("http")
async def redirect_to_https(request, call_next):
    # Redireciona para HTTPS se a requisição não estiver segura
    if request.url.scheme != "https":
        url = request.url.replace(scheme="https")
        return RedirectResponse(url)
    return await call_next(request)

# test IRIS


@app.get("/telemedicina/{user_id}")
async def telemedicine(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    url_redirect = controller.get_redirect_url('teste_url')

    logger.info(f"Sucesso. Usuário"
                f"{user_id}." f"redirecionado para {url_redirect}")

    return RedirectResponse(url=url_redirect)
