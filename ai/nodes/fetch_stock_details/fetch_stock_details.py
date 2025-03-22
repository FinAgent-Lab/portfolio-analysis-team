import os
import requests
from typing import List

from ai.states.portfolio_state import PortfolioState
from ai.utils.reqeust_util import make_request_header
from ai.response.stock_detail import StockDetail


def fetch_stock_details(state: PortfolioState) -> PortfolioState:
    stocks = state['output1']
    stocks = call_stock_details(stocks)

    return {
        **state,
        "messages": state.get("messages", []),
        "stock_details": stocks
    }


def call_stock_details(stocks) -> List[StockDetail]:
    url = 'https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/quotations/inquire-price'
    header = make_request_header(os.getenv('VTS_TOKEN'), os.getenv('VTS_APPKEY'), os.getenv('VTS_APPSECRET'))
    result: List[StockDetail] = []

    for stock in stocks:
        params = {
            'fid_cond_mrkt_div_code': 'J',  # 거래소: 'J', 코스닥: 'Q'
            'fid_input_iscd': stock['pdno']  # 종목 코드
        }
        response = requests.get(url, headers=header, params=params)
        if response.status_code == 200:
            data = response.json()['output']
            stock_detail = StockDetail(**data)
            stock_detail.prdt_name = stock['prdt_name']
            result.append(stock_detail)

    return result
