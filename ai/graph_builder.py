from langgraph.graph import StateGraph, START, END
from states.portfolio_state import PortfolioState
from nodes.analyze_assets_risk.analyze_assets_risk import analyze_assets_risk
from nodes.fetch_assets.fetch_assets import fetch_assets
from nodes.fetch_stock_details.fetch_stock_details import fetch_stock_details

# 그래프 생성
graph_builder = StateGraph(PortfolioState)

graph_builder.add_node("fetch_assets", fetch_assets)
graph_builder.add_node("analyze_assets_risk", analyze_assets_risk)
graph_builder.add_node("fetch_stock_details", fetch_stock_details)

graph_builder.add_conditional_edges(
    source="fetch_assets",
    path=lambda state: "output1" in state and len(state['output1']) > 0,
    path_map={
        True: "fetch_stock_details",
        False: "__end__"
    }
)
graph_builder.add_edge("fetch_stock_details", "analyze_assets_risk")

graph_builder.set_entry_point("fetch_assets")

compiled_graph = graph_builder.compile()
# print(compiled_graph.get_graph().draw_mermaid())

print(compiled_graph.invoke({"messages": []}))
