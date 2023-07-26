# 森空岛API SDK (非官方)

## Build

1. install build
```bash
python3 -m pip install --upgrade build
```

2. build wheel
```bash
python3 -m build
```


## 安装

*replace \* with current version*

```bash
pip3 install skland_api-*-py3-none-any.whl
```

## 使用方法 Example

**获取credential**

```
api = SklandApiV1()

account_token = api.account.token_by_phone_password("YOUR_PHONE","YOUR_PASSWORD")

print("account token", account_token)

oauth_code = api.account.grant_code(account_token)

print("oauth code", oauth_code)

cred = api.auth.generate_cred_by_code(oauth_code)

print("skland cred", cred)

api.init(cred.cred)
```

**获取游戏信息**

```
YOUR_CRED = ""

api: SklandApi = SklandApiV1()
# 初始化API
api.init(YOUR_CRED)
# 获取游戏帐号绑定
binding = api.game.player_binding()
print("binding: \n", binding)
# 获取游戏信息
info = api.game.player_info(binding[0].binding_list[0].uid)
print(json.dumps(info,indent=2,ensure_ascii=False))
```