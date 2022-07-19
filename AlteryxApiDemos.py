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

############## Get all collections on host ##############
print(api1.GET_endpoint('/webapi/v3/collections', ''))

############## Get all jobs of a specific workflow ##############
parameters = {
    "sortField" : "createdate",
    "direction" : "desc",
    "offset" : 0,
    "limit" : 10 
}
print(api1.GET_endpoint('/webapi/v1/workflows/' + AppId + '/jobs' , parameters))


############## Get all schedules on host with V3 o V1 ##############
#------------ V3 ------------
parameters = {
    "view" : "Default",
    "ownerId" : "",
    "workflowId" : "",
    "runsAfter" : "",
    "runsBefore" : ""
}
print(api1.GET_endpoint('/v3/schedules/', parameters))

#------------ V1 ------------
parameters = {
    "page" : 1,
    "pageSize" : 50
}
print(api1.GET_endpoint('/admin/v1/schedules', parameters))