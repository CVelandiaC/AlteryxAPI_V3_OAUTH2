from AlteryxApiV3OaV2 import ayx_api_v3
import json 

with open('Alteryx_Creds.json') as json_file:
    creds = json.load(json_file)

# Core variables
apiKey = creds["Key"]
apiSecret = creds["Secret"]
Gallery = creds["Gallery"]
AppId = creds["DataFlowID"]


api1 = ayx_api_v3(apiKey, apiSecret, Gallery)

# Step 1: Request Auth toke it will expire in 3600 secs
api1.req_auth_token()

# Get all collections on host
print(api1.GET_endpoint('/webapi/v3/collections', ''))

# Get all collections on host
parameters = {
    "sortField" : "createdate",
    "direction" : "desc",
    "offset" : 0,
    "limit" : 10 
}
print(api1.GET_endpoint('/webapi/v1/workflows/' + AppId + '/jobs' , parameters))