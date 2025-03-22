from typing import Dict, List

from ai.states.portfolio_state import PortfolioState
from ai.response.stock_detail import StockDetail


def analyze_assets_risk(state: PortfolioState) -> PortfolioState:
    stock_details = state['stock_details']

    risky_assets = is_risky_asset(stock_details)
    return {
        **state,
        "messages": state.get("messages", []),
        'risky_assets': {
            'is_risky_assets': risky_assets,
            'total_percent': calculate_risky_asset(risky_assets) / len(risky_assets)
        }
    }


def is_risky_asset(stock_details: List[StockDetail]) -> Dict[str, bool]:
    result: Dict[str, bool] = dict()
    # TODO 하드코딩 -> llm 이용해서 판단해보기
    keywords = {'인버스', '레버리지', '파생', '선물', '곱버스'}
    for stock in stock_details:
        result[stock.stck_shrn_iscd] = (
                float(stock.marg_rate) > 60 or
                stock.crdt_able_yn == "N" or
                stock.temp_stop_yn == "Y" or
                stock.mrkt_warn_cls_code != "00" or
                stock.invt_caful_yn == "Y" or
                stock.short_over_yn == "Y" or
                stock.mang_issu_cls_code != "N" or
                stock.ssts_yn == "Y" or
                any(keyword in stock.prdt_name for keyword in keywords)
        )

    return result


def calculate_risky_asset(is_risky_assets: Dict[str, bool]) -> int:
    result = 0
    for stock, is_risky in is_risky_assets.items():
        result += (1 if is_risky else 0)

    return result
