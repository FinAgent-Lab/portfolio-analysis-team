# Portfolio Analysis Team

Portfolio Analysis 팀의 프로젝트입니다.

## 폴더구조

``` bash
├── frontend/
├── backend/ 
└── ai/         
    └── nodes/
        ├── fetch_assets/                # API로 고객 주식 자산 가져오기
        │   ├── __init__.py         
        │   └── fetch_assets.py 
        ├── analyze_assets_risk/         # 주식 자산 중 위험 자산이 얼마나 되는지 분석
        │   ├── __init__.py         
        │   └── analyze_assets_risk.py
        ├── analyze_assets_ratio/        # 주식 자산 중 각 테마별 주식이 몇퍼센트 되는지 분석 (ex. 기술주 25%, 바이오주 10%, ...)
        │   ├── __init__.py         
        │   └── analyze_assets_ratio.py
        └── analyze_asset_timeline/      # 특정 기간 동안 주식 변화를 분석 (정확히 주식의 어떤 변화를 보여줄 것인지는 아직 미정)
            ├── __init__.py        
            └── analyze_asset_timeline.py
```

각자 담당한 부분에 해당하는 폴더에 프로젝트를 생성하고 커밋해주시면 됩니다.

## Framework
- Frontend: React
- Backend: FastAPI, Nest.js
- AI: LangChain
