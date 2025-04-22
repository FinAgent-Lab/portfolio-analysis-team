import requests
import json 

def make_request_header(token: str, app_key: str, app_secret: str):
    return {
        'Content-Type': 'application/json',
        'authorization': f'Bearer {token}',
        'appkey': app_key,
        'appsecret': app_secret,
        'tr_id': 'FHKST01010100',
    }
    
def get_access_token(APP_KEY, APP_SECRET, URL_BASE):                                 
    headers = {"content-type":"application/json"}
    body = {"grant_type":"client_credentials",    
    "appkey":APP_KEY,                                   
    "appsecret":APP_SECRET}                          
    PATH = "oauth2/tokenP"                              
    URL = f"{URL_BASE}/{PATH}"                        
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    ACCESS_TOKEN = res.json()["access_token"]
    return ACCESS_TOKEN
