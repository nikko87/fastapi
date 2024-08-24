import logging

import httpx
from fastapi import APIRouter, HTTPException, Response

from infra.adapters.jitsi_adapter import JitsiAdapter
from use_cases.get_redirect_url import GetRedirectUrl

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/telemedicina/jitsi/{user_id}")
async def telemedicina_jitsi(user_id: str):
    logger.info(f"Recebido request para o usuário {user_id}")

    adapter = JitsiAdapter()
    use_case = GetRedirectUrl(adapter)

    forward_url = use_case.execute({})

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
