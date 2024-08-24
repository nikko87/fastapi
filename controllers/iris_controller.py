import logging

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from infra.adapters.iris_adapter import IrisAdapter
from use_cases.get_redirect_url import GetRedirectUrl

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/telemedicina/{user_id}")
async def telemedicine_redirect(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)

    # retorna https://videocalldoutorsalva.irisemergencia.com/VideoCall/VideoCall.html?MasterId=38&idChamada=ZGU1YjlkM2UtNGZkMi00MjIxLWIxMzYtNTk5Y2UyNzYwOWQ2"
    url_redirect = use_case.execute({})

    logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

    return RedirectResponse(url=url_redirect)


@router.post("/telemedicina/json/{user_id}")
async def telemedicine_post(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)

    url_redirect = use_case.execute({})

    logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

    return {"url": url_redirect}
