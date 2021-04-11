import json
from botocore.vendored import requests
def lambda_handler(event, context):
  
  


  url = "https://api.spotify.com/v1/me/player?market=ES&additional_types=episode"
  token = "xxxxxx"
  headers = {'content-type': 'application/json', 'Accept': 'html/json', 'Authorization': "Bearer " + token}
  payload = {}
  r = requests.get(url, data=payload, headers=headers)
  
  #Get new token when this expires
  
  if(r.status_code==200):
    
    a= json.loads(r.content)
    lis=a['item']['album']['artists'][0]
    lis2=a['item']['album']
    print(lis2['name'])
    print(lis['name'])
    svg= """<svg fill="none" viewBox="0 0 500 500" width="500" height="500" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
    
    <style>
    #a {
      color: red
    }
    </style>
              <div id="a">
              <h1>Currently listening</h1>
              <h1>"""+lis2['name']+"""</h1>
              <h2>"""+lis['name']+"""</h2>
              </div>
            </div>
          </foreignObject>
        </svg>"""
         
    return {
        'statusCode': 200,
        'body': svg,
        'headers': {'Content-Type': "image/svg+xml", 'Cache-Control': 'no-cache'}
    }
    
  else:
    
      
    svg= """<svg fill="none" viewBox="0 0 500 500" width="500" height="500" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
               <style>
        #a {
        color: red
        }
    </style>
              <div id="a">
              <h1>Currently listening</h1>
              <h1>Nothing</h1>
              </div>
              
            </div>
          </foreignObject>
        </svg>"""
         
    return {
        'statusCode': 200,
        'body': svg,
        'headers': {'Content-Type': "image/svg+xml", 'Cache-Control': 'no-cache'}
    }
      
  
  