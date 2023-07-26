from skland.api.v1 import SklandApiV1


api = SklandApiV1()

account_token = api.account.token_by_phone_password("YOUR_PHONE","YOUR_PASSWORD")

print("account token", account_token)

oauth_code = api.account.grant_code(account_token)

print("oauth code", oauth_code)

cred = api.auth.generate_cred_by_code(oauth_code)

print("skland cred", cred)

api.init(cred.cred)