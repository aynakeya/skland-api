import json

from skland.api.v1 import SklandApiV1
from skland.api import SklandApi

YOUR_CRED = ""

api: SklandApi = SklandApiV1()

api.init(YOUR_CRED)

binding = api.game.player_binding()

print("binding: \n", binding)

info = api.game.player_info(binding[0].binding_list[0].uid)

print("info")
print(json.dumps(info,indent=2,ensure_ascii=False))