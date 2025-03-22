from typing import Annotated, Optional, Dict, Any
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class PortfolioState(TypedDict):
    messages: Annotated[list, add_messages]
    output1: Optional[list]
    output2: Optional[list]
    stock_details: Optional[list]
    risky_assets: Optional[Dict[str, Any]]
