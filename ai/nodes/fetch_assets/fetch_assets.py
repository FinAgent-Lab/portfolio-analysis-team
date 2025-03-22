from ai.states.portfolio_state import PortfolioState
from ai.response.balance import StockBalanceResponse

import json
from typing import cast


def fetch_assets(state: PortfolioState) -> PortfolioState:
    response = cast(StockBalanceResponse, json.loads(TEST_DATA))

    return {
        **state,
        "messages": state.get("messages", []),
        "output1": response['output1'],
        "output2": response['output2']
    }


TEST_DATA = """
{
    "ctx_area_fk100": "                                                                                                    ",
    "ctx_area_nk100": "                                                                                                    ",
    "output1": [
        {
            "pdno": "000660",
            "prdt_name": "SK하이닉스",
            "trad_dvsn_name": "현금",
            "bfdy_buy_qty": "0",
            "bfdy_sll_qty": "0",
            "thdt_buyqty": "0",
            "thdt_sll_qty": "0",
            "hldg_qty": "1",
            "ord_psbl_qty": "1",
            "pchs_avg_pric": "198600.0000",
            "pchs_amt": "198600",
            "prpr": "215500",
            "evlu_amt": "215500",
            "evlu_pfls_amt": "16900",
            "evlu_pfls_rt": "8.51",
            "evlu_erng_rt": "8.50956697",
            "loan_dt": "",
            "loan_amt": "0",
            "stln_slng_chgs": "0",
            "expd_dt": "",
            "fltt_rt": "2.62000000",
            "bfdy_cprs_icdc": "5500",
            "item_mgna_rt_name": "20%",
            "grta_rt_name": "",
            "sbst_pric": "0",
            "stck_loan_unpr": "0.0000"
        },
        {
            "pdno": "114800",
            "prdt_name": "KODEX 인버스",
            "trad_dvsn_name": "현금",
            "bfdy_buy_qty": "0",
            "bfdy_sll_qty": "0",
            "thdt_buyqty": "0",
            "thdt_sll_qty": "0",
            "hldg_qty": "35",
            "ord_psbl_qty": "35",
            "pchs_avg_pric": "4482.1420",
            "pchs_amt": "156875",
            "prpr": "4290",
            "evlu_amt": "150150",
            "evlu_pfls_amt": "-6725",
            "evlu_pfls_rt": "-4.29",
            "evlu_erng_rt": "-4.28685259",
            "loan_dt": "",
            "loan_amt": "0",
            "stln_slng_chgs": "0",
            "expd_dt": "",
            "fltt_rt": "-0.58000000",
            "bfdy_cprs_icdc": "-25",
            "item_mgna_rt_name": "60%",
            "grta_rt_name": "",
            "sbst_pric": "0",
            "stck_loan_unpr": "0.0000"
        }
    ],
    "output2": [
        {
            "dnca_tot_amt": "9644485",
            "nxdy_excc_amt": "9644485",
            "prvs_rcdl_excc_amt": "9644485",
            "cma_evlu_amt": "0",
            "bfdy_buy_amt": "0",
            "thdt_buy_amt": "0",
            "nxdy_auto_rdpt_amt": "0",
            "bfdy_sll_amt": "0",
            "thdt_sll_amt": "0",
            "d2_auto_rdpt_amt": "0",
            "bfdy_tlex_amt": "0",
            "thdt_tlex_amt": "0",
            "tot_loan_amt": "0",
            "scts_evlu_amt": "365650",
            "tot_evlu_amt": "10010135",
            "nass_amt": "10010135",
            "fncg_gld_auto_rdpt_yn": "",
            "pchs_amt_smtl_amt": "355475",
            "evlu_amt_smtl_amt": "365650",
            "evlu_pfls_smtl_amt": "10175",
            "tot_stln_slng_chgs": "0",
            "bfdy_tot_asst_evlu_amt": "10005510",
            "asst_icdc_amt": "4625",
            "asst_icdc_erng_rt": "0.04622453"
        }
    ],
    "rt_cd": "0",
    "msg_cd": "20310000",
    "msg1": "모의투자 조회가 완료되었습니다.                                                 "
}
"""