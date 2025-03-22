from typing import TypedDict, Optional
from pydantic import BaseModel


class StockDetail(BaseModel):
    stck_shrn_iscd: str # 주식 코드
    prdt_name: Optional[str] = None # 주식 이름
    rprs_mrkt_kor_name: str
    bstp_kor_isnm: str
    marg_rate: str  # 증거금률 (ex: "60.00")
    crdt_able_yn: str  # 신용거래 가능 여부 ("Y"/"N")
    temp_stop_yn: str  # 일시정지 여부
    mrkt_warn_cls_code: str  # 시장경고 코드
    invt_caful_yn: str  # 투자주의 여부
    short_over_yn: str  # 공매도 과열 여부
    mang_issu_cls_code: str  # 관리종목 코드
    ssts_yn: str  # 정리매매 여부


class StockDetailResponse(TypedDict):
    iscd_stat_cls_code: str
    marg_rate: str
    rprs_mrkt_kor_name: str
    bstp_kor_isnm: str
    temp_stop_yn: str
    oprc_rang_cont_yn: str
    clpr_rang_cont_yn: str
    crdt_able_yn: str
    grmn_rate_cls_code: str
    elw_pblc_yn: str
    stck_prpr: str
    prdy_vrss: str
    prdy_vrss_sign: str
    prdy_ctrt: str
    acml_tr_pbmn: str
    acml_vol: str
    prdy_vrss_vol_rate: str
    stck_oprc: str
    stck_hgpr: str
    stck_lwpr: str
    stck_mxpr: str
    stck_llam: str
    stck_sdpr: str
    wghn_avrg_stck_prc: str
    hts_frgn_ehrt: str
    frgn_ntby_qty: str
    pgtr_ntby_qty: str
    pvt_scnd_dmrs_prc: str
    pvt_frst_dmrs_prc: str
    pvt_pont_val: str
    pvt_frst_dmsp_prc: str
    pvt_scnd_dmsp_prc: str
    dmrs_val: str
    dmsp_val: str
    cpfn: str
    rstc_wdth_prc: str
    stck_fcam: str
    stck_sspr: str
    aspr_unit: str
    hts_deal_qty_unit_val: str
    lstn_stcn: str
    hts_avls: str
    per: str
    pbr: str
    stac_month: str
    vol_tnrt: str
    eps: str
    bps: str
    d250_hgpr: str
    d250_hgpr_date: str
    d250_hgpr_vrss_prpr_rate: str
    d250_lwpr: str
    d250_lwpr_date: str
    d250_lwpr_vrss_prpr_rate: str
    stck_dryy_hgpr: str
    dryy_hgpr_vrss_prpr_rate: str
    dryy_hgpr_date: str
    stck_dryy_lwpr: str
    dryy_lwpr_vrss_prpr_rate: str
    dryy_lwpr_date: str
    w52_hgpr: str
    w52_hgpr_vrss_prpr_ctrt: str
    w52_hgpr_date: str
    w52_lwpr: str
    w52_lwpr_vrss_prpr_ctrt: str
    w52_lwpr_date: str
    whol_loan_rmnd_rate: str
    ssts_yn: str
    stck_shrn_iscd: str
    fcam_cnnm: str
    cpfn_cnnm: str
    frgn_hldn_qty: str
    vi_cls_code: str
    ovtm_vi_cls_code: str
    last_ssts_cntg_qty: str
    invt_caful_yn: str
    mrkt_warn_cls_code: str
    short_over_yn: str
    sltr_yn: str
    mang_issu_cls_code: str
