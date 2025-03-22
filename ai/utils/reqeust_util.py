def make_request_header(token: str, app_key: str, app_secret: str):
    return {
        'Content-Type': 'application/json',
        'authorization': f'Bearer {token}',
        'appkey': app_key,
        'appsecret': app_secret,
        'tr_id': 'FHKST01010100',
    }