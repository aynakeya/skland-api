from dataclasses import dataclass


class AccountAuthApi:
    def token_by_phone_password(self,phone: str, password: str) -> str:
        raise NotImplemented()

    def grant_code(self, token: str, token_type: int) -> str:
        raise NotImplemented()


@dataclass
class AuthCredInfo:
    cred: str
    user_id: str


class ZonaiAuthApi:
    def generate_cred_by_code(self, code: str) -> AuthCredInfo:
        raise NotImplemented()
