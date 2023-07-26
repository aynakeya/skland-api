import httpx

from skland.api import ZonaiApiClient
from skland.api import AuthCredInfo, ZonaiAuthApi, AccountAuthApi
from skland.model.exception import SklandApiException


class AccountAuthApiImpl(AccountAuthApi):

    def token_by_phone_password(self, phone: str, password: str) -> str:
        resp = httpx.post(
            "https://as.hypergryph.com/user/auth/v1/token_by_phone_password",
            json={"phone": phone, "password": password}
        ).json()
        if resp["status"] != 0:
            raise SklandApiException(resp["status"], resp["msg"])
        return resp["data"]["token"]

    def grant_code(self, token: str, token_type: int = 0) -> str:
        resp = httpx.post(
            "https://as.hypergryph.com/user/oauth2/v2/grant",
            json={
                "token": token,
                "appCode": "4ca99fa6b56cc2ba",  # oauth app code
                "type": token_type
            }
        ).json()
        if resp["status"] != 0:
            raise SklandApiException(resp["status"], resp["msg"])
        return resp["data"]["code"]


class ZonaiAuthApiImpl(ZonaiAuthApi):
    def __init__(self, client: ZonaiApiClient):
        self.client = client

    def generate_cred_by_code(self, code: str) -> AuthCredInfo:
        resp = self.client.post(
            "/api/v1/user/auth/generate_cred_by_code",
            data={
                "code": code,
                "kind": 1
            }
        )
        return AuthCredInfo(cred=resp.data["cred"], user_id=resp.data["userId"])
