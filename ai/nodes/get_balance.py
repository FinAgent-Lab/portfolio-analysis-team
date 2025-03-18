from langchain_core.tools import tool
from utils.fetch_asset import StockAPI

# @tool
# def get_stock_balance(query) -> int:
#     """주식 계좌의 현금 잔고를 조회합니다."""
#     api = StockAPI()
#     balance = api.get_orderable_cash()
#     if balance is not None:
#         return balance
#     else:
#         return "잔고 조회에 실패했습니다."


from typing import Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
from pydantic import BaseModel, Field

class StockBalanceInput(BaseModel):
    customer_id: str = Field(description="Customer ID. Identifier of the customer whose stock balance is to be retrieved.")

class StockBalanceTool(BaseTool):
    name = "stock_balance"
    description = "Retrieves the stock balance for a specific customer using their customer ID."
    args_schema: Type[BaseModel] = StockBalanceInput

    def _run(
        self, customer_id: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        raise NotImplementedError("비동기 호출만 지원합니다.")

    async def _arun(
        self, customer_id: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        data = StockAPI(customer_id=customer_id).get_orderable_cash()
        # TODO 데이터 전처리 로직 필요
        return data
