import logging

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from infra.adapters.tolife_adapter import TolifeAdapter
from use_cases.get_attendance_data_vitaldoc import GetAttendanceDataVitalDocUseCase
from use_cases.get_redirect_url import GetRedirectUrl

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/telemedicina/{user_id}")
async def telemedicine_redirect(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = TolifeAdapter()
    use_case_get_attendance = GetAttendanceDataVitalDocUseCase()
    use_case_get_redirect = GetRedirectUrl(adapter)

    url_redirect = use_case_get_redirect.execute({})

    logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

    return RedirectResponse(url=url_redirect)


# @router.post("/telemedicina/json/{user_id}")
# async def telemedicine_post(user_id: str):
#     logger.info(f"Recebido request para o usuário {user_id}")

#     adapter = IrisAdapter()
#     use_case = GetRedirectUrl(adapter)

#     url_redirect = use_case.execute({})

#     logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

#     return {"url": url_redirect}
