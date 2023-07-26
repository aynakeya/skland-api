from skland.api.auth import *
from skland.api.client import *
from skland.api.game import *


class SklandApi:
    def __init__(self):
        self.account = AccountAuthApi()
        self.auth = ZonaiAuthApi()
        self.game = ZonaiGameApi()

    def init(self, cred: str):
        raise NotImplemented()
