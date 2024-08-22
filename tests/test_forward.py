
import httpx
import pytest
from fastapi import HTTPException, Response
from fastapi.responses import HTMLResponse

from adapters.iris_adapter import IrisAdapter
from adapters.jitsi_adapter import JitsiAdapter
from controllers.integration_controller import IntegrationController
from use_cases.get_redirect_url import GetRedirectUrl


@pytest.mark.asyncio
async def test_forward():
    adapter = JitsiAdapter()
    use_case = GetRedirectUrl(adapter)
    controller = IntegrationController(use_case)

    forward_url = controller.get_redirect_url({"teste": "teste_url"})
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(forward_url)

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code, detail=exc.response.text)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    print(response.content)

    # return Response(
    #     content=response.content,
    #     status_code=response.status_code,
    #     headers=dict(response.headers),
    # )
    return HTMLResponse(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
    )


def add_base_url(content: bytes, base_url: str) -> bytes:
    content_str = content.decode('utf-8')
    base_tag = f'<base href="{base_url}">'
    content_str = content_str.replace('<head>', f'<head>{base_tag}', 1)
    return content_str.encode('utf-8')
