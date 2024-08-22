import logging
import sys

import httpx
from fastapi import FastAPI, HTTPException, Request, Response
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

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


# def add_base_url(content: bytes, base_url: str) -> bytes:
#     content_str = content.decode('utf-8')
#     base_tag = f'<base href="{base_url}">'
#     content_str = content_str.replace('<head>', f'<head>{base_tag}', 1)
#     return content_str.encode('utf-8')


@app.get("/telemedicina/jitsi/{user_id}")
async def telemedicina_jitsi(request: Request, user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = JitsiAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    forward_url = controller.get_redirect_url({"teste": "teste_url"})

    async with httpx.AsyncClient(verify=False) as client:
        try:

            response = await client.get(
                forward_url,
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                },
            )
            response.raise_for_status()

        except httpx.RequestError as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    headers = dict(response.headers)
    headers.pop("content-length", None)
    headers.pop("content-encoding", None)
    headers["Access-Control-Allow-Origin"] = "*"
    headers["Access-Control-Allow-Headers"] = "Content-Type"

    return Response(
        content=response.content, status_code=response.status_code, headers=headers
    )


@app.get("/telemedicina/{user_id}")
async def telemedicine_redirect(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    # retorna https://videocalldoutorsalva.irisemergencia.com/VideoCall/VideoCall.html?MasterId=38&idChamada=ZGU1YjlkM2UtNGZkMi00MjIxLWIxMzYtNTk5Y2UyNzYwOWQ2"
    url_redirect = controller.get_redirect_url({"teste": "teste_url"})

    logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

    return RedirectResponse(url=url_redirect)


@app.post("/telemedicina/iris/{user_id}")
async def telemedicine_post(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = IrisAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    url_redirect = controller.get_redirect_url({"teste": "teste_url"})

    logger.info(f"Sucesso. Usuário {user_id}. Redirecionado para {url_redirect}")

    return {"url": url_redirect}
