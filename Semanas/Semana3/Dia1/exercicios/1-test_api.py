import asyncio
from typing import Any, Literal
import httpx

BASE_URL = "http://localhost:8000"


async def print_response(client: httpx.AsyncClient, url: str, data: Any | None, type: Literal["get", "post"] = "get"):
    try:
        match type:
            case "get":
                response = await client.get(url)
            case "post":
                response = await client.post(url, json=data)
        
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
    except httpx.HTTPStatusError as e:
        raise Exception(f"Ocorreu um erro HTTP \nErro: {e}")
    except httpx.RequestError as e:
        raise Exception(f"Um erro ocorreu na requisição com {e.request.url!r}.")

async def send_chat():
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/chat"
        data = {
            "message": "Me diga uma curiosidade",
            "source": "web",
        }

        try:
            await print_response(client, url, data, type="post")
        except Exception as e:
            print(e)        


async def send_health():
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/health"

        try:
            await print_response(client, url, None, type="get")
        except httpx.HTTPStatusError as e:
            print(f"Ocorreu um erro HTTP \nErro: {e}")
        except httpx.RequestError as e:
            print(f"Um erro ocorreu na requisição com {e.request.url!r}.")


async def main():
    await send_chat()
    await send_health()


if __name__ == "__main__":
    asyncio.run(main())
