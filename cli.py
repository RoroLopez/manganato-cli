import json
from RequestHandler import RequestHandler

rq = RequestHandler()

response = rq.basic_information('record of ragnarok')
# print(dir(response))
# print(response._content)
jsonResponse = response.json()
print(jsonResponse[0]['data'][0]['id'])