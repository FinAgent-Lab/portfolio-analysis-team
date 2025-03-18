import requests
import json
import os

class StockAPI:
    """자산 조회 API"""
    def __init__(self, customer_id: str):
        self.APP_KEY = os.environ.get("APP_KEY")
        self.APP_SECRET = os.environ.get("APP_SECRET")
        self.CANO = customer_id[:8]  # 고객 ID 앞 8자리
        self.ACNT_PRDT_CD = customer_id[8:]  # 고객 ID 뒤 2자리
        self.PDNO = os.environ.get("PDNO")
        self.ORD_UNPR = os.environ.get("ORD_UNPR")
        self.URL_BASE = "https://openapi.koreainvestment.com:9443"
        self.PATH = "uapi/domestic-stock/v1/trading/inquire-psbl-order"
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        try:
            headers = {"content-type": "application/json"}
            body = {
                "grant_type": "client_credentials",
                "appkey": self.APP_KEY,
                "appsecret": self.APP_SECRET,
            }
            url = f"{self.URL_BASE}/oauth2/tokenP"
            res = requests.post(url, headers=headers, data=json.dumps(body))
            res.raise_for_status()
            return res.json()["access_token"]
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve access token: {e}")
            return None
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Failed to process access token response: {e}")
            return None

    def get_orderable_cash(self):
        """Retrieves the orderable cash balance."""
        if not self.access_token:
            print("Access token is missing.")
            return None
        try:
            url = f"{self.URL_BASE}/{self.PATH}"
            headers = {
                "Content-Type": "application/json",
                "authorization": f"Bearer {self.access_token}",
                "appKey": self.APP_KEY,
                "appSecret": self.APP_SECRET,
                "tr_id": "TTTC8908R",
                "custtype": "P",
            }
            params = {
                "CANO": self.CANO,
                "ACNT_PRDT_CD": self.ACNT_PRDT_CD,
                "PDNO": self.PDNO,
                "ORD_UNPR": self.ORD_UNPR,
                "ORD_DVSN": "00",
                "CMA_EVLU_AMT_ICLD_YN": "N",
                "OVRS_ICLD_YN": "N",
            }
            res = requests.get(url, headers=headers, params=params)
            res.raise_for_status()
            return int(res.json()["output"]["ord_psbl_cash"])
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve orderable cash: {e}")
            return None
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Failed to process orderable cash response: {e}")
            return None
    
