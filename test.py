from engine4 import ENGINE4, FetchFilterOptions
from getpass import getpass

password = getpass()

engine4 = ENGINE4('https://dev.engine4.io/')
authentication_result = engine4.authenticate('', password, 'mfInternal')

fetch_filter = FetchFilterOptions('CreatedDate', '>', '2018-01-01T00:00:00.000Z')
result = engine4.fetch(authentication_result.access_token, '868d3b4e-cf31-4c33-8462-e16837c06706', 0, 2, False, True, fetch_filter)

print(result["items"])
