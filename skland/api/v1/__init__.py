from skland.api import SklandApi
from skland.api.v1.auth import ZonaiAuthApiImpl, AccountAuthApiImpl
from skland.api.v1.client import HttpxClient
from skland.api.v1.game import ZonaiGameApiImpl


class SklandApiV1(SklandApi):
    def __init__(self):
        super().__init__()
        self.client = HttpxClient("https://zonai.skland.com")
        self.account = AccountAuthApiImpl()
        self.auth = ZonaiAuthApiImpl(self.client)
        self.game = ZonaiGameApiImpl(self.client)

    def init(self, cred: str):
        self.client.set_credential(cred)
