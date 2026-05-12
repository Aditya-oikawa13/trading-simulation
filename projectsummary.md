# Project Summary: TradingAgents & Alpaca Integration

## 📌 Project Overview
Integration of the **TradingAgents** multi-agent LLM framework with an **Alpaca Paper Trading** account for automated, transparent, and research-driven trading.

## 🛠 Tech Stack
- **Framework**: [TradingAgents](https://github.com/TauricResearch/TradingAgents) (LangGraph)
- **Primary LLM**: `inclusionai/ring-2.6-1t:free` (via OpenRouter)
- **Execution**: [Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server) (Manual Agent Execution - Approach A)
- **Data Sources**: yfinance (Technical, Fundamental, News)

## ⚙️ Configuration & Environment
- **Environment**: `.env` configured with OpenRouter and Alpaca keys.
- **Risk Constraint**: **15% Maximum Position Size** per trade (Hard-coded in `Portfolio Manager`).
- **Transparency**: Enhanced logging added to `tradingagents/graph/trading_graph.py`, `trader.py`, and `portfolio_manager.py`.
- **Session Logs**: All agent outputs and decision states are saved to `/session_logs`.

## 📈 Work Completed
1.  **Codebase Setup**: Repository cloned, dependencies installed, and package set up in editable mode.
2.  **Model Integration**: Successfully switched to OpenRouter and the Ring-1T model.
3.  **Risk Guardrails**: Modified the `Portfolio Manager` agent to enforce the 15% position size cap.
4.  **Transparency Layer**: Injected print statements across the graph to surface "thought processes" and raw agent reports in the console.
5.  **Initial Validation**: Performed a test run for `NVDA` (May 10, 2024), resulting in a disciplined **HOLD** decision.

## 🚀 How to Run
To run the analysis for a specific ticker and date:
```bash
# Direct script execution (customized with transparency logs)
python main.py

# To change the ticker/date, edit main.py or run via CLI:
python -m cli.main
```

## 📋 Next Session Goals
...
- [ ] Monitor and log performance for future reflection.

## 📦 Versioning
This project is maintained as a standalone repository to track integration changes and session logs.

---
*Last Updated: Monday, May 11, 2026*
