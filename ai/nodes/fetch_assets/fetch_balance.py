import os
import requests
from dotenv import load_dotenv
from ai.utils.reqeust_util import get_access_token

load_dotenv()

class StockBalanceAPI:
    def __init__(self):
        self.URL_BASE = os.getenv("URL_BASE")
        self.APP_KEY = os.getenv("APP_KEY")
        self.APP_SECRET = os.getenv("APP_SECRET")
        self.CANO = os.getenv("CANO")
        self.ACNT_PRDT_CD = os.getenv("ACNT_PRDT_CD")
        self.ACCESS_TOKEN = get_access_token(
            APP_KEY=self.APP_KEY, APP_SECRET=self.APP_SECRET, URL_BASE=self.URL_BASE
        )
        self.PATH = "/uapi/domestic-stock/v1/trading/inquire-balance"
        self.TR_ID = "TTTC8434R"
        self.HEADERS = {
            "Content-Type": "application/json",
            "authorization": f"Bearer {self.ACCESS_TOKEN}",
            "appKey": self.APP_KEY,
            "appSecret": self.APP_SECRET,
            "tr_id": self.TR_ID,
        }
        self.PARAMS = {
            "CANO": self.CANO,
            "ACNT_PRDT_CD": self.ACNT_PRDT_CD,
            "AFHR_FLPR_YN": "N",
            "OFL_YN": "",
            "INQR_DVSN": "01",
            "UNPR_DVSN": "01",
            "FUND_STTL_ICLD_YN": "N",
            "FNCG_AMT_AUTO_RDPT_YN": "N",
            "PRCS_DVSN": "01",
            "CTX_AREA_FK100": "",
            "CTX_AREA_NK100": "",
        }

    def process_output1(self, output1):
        if not output1:
            return {}

        return {
            "상품번호": output1.get("pdno", "데이터 없음"),
            "상품명": output1.get("prdt_name", "데이터 없음"),
            "보유수량": output1.get("hldg_qty", "데이터 없음"),
            "매입평균가격": output1.get("pchs_avg_pric", "데이터 없음"),
            "평가손익금액": output1.get("evlu_pfls_amt", "데이터 없음"),
            "평가손익율": output1.get("evlu_pfls_rt", "데이터 없음"),
            "평가수익율": output1.get("evlu_erng_rt", "데이터 없음"),
        }


    def process_output2(self, output2):
        if not output2 or not isinstance(output2, list) or not output2[0]:
            return {}

        data = output2[0]
        return {
            "순자산금액": data.get("nass_amt", "데이터 없음"),
            "유가평가금액": data.get("scts_evlu_amt", "데이터 없음"),
            "CMA평가금액": data.get("cma_evlu_amt", "데이터 없음"),
            "총평가금액": data.get("tot_evlu_amt", "데이터 없음"),
            "자산증감액": data.get("asst_icdc_amt", "데이터 없음"),
            "자산증감수익율(%)": data.get("asst_icdc_erng_rt", "데이터 없음"),
            "예수금총금액": data.get("dnca_tot_amt", "데이터 없음"),
            "총대출금액": data.get("tot_loan_amt", "데이터 없음"),
            "매입금액합계금액": data.get("pchs_amt_smtl_amt", "데이터 없음"),
            "평가금액합계금액": data.get("evlu_amt_smtl_amt", "데이터 없음"),
            "평가손익합계금액": data.get("evlu_pfls_smtl_amt", "데이터 없음"),
            "총대주매각대금": data.get("tot_stln_slng_chgs", "데이터 없음"),
            "전일총자산평가금액": data.get("bfdy_tot_asst_evlu_amt", "데이터 없음"),
        }


    def get_cash_balance(self):
        url = f"{self.URL_BASE}{self.PATH}"
        try:
            res = requests.get(url, headers=self.HEADERS, params=self.PARAMS)
            res.raise_for_status()
            result = res.json()
            output1 = result.get("output1")
            output2 = result.get("output2")
            return {**self.process_output1(output1), **self.process_output2(output2)}
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API 요청 오류: {e}")
        except ValueError as e:
            raise ValueError(f"JSON 디코딩 오류: {e}")
