from engine4 import ENGINE4, FetchFilterOptions, HttpResponseException
from getpass import getpass

password = getpass()

try:
    engine4 = ENGINE4('https://dev.engine4.io/')
    authentication_result = engine4.authenticate('robin.genz@mobile-function.com', password, 'mfInternal')

    print(authentication_result.access_token)

    fetch_filter = FetchFilterOptions('CreatedDate', '>', '2018-01-01T00:00:00.000Z')
    result = engine4.fetch(authentication_result.access_token, '868d3b4e-cf31-4c33-8462-e16837c06706', 0, 2, False, True, fetch_filter)

    print(result["items"])
except HttpResponseException as exception:
  print(exception.to_json()) 
