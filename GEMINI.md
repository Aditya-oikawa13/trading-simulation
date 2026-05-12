# TradingAgents: Multi-Agent LLM Financial Trading Framework

## Overview
TradingAgents is a multi-agent framework built with **LangGraph** that simulates a professional trading firm. It employs specialized LLM-powered agents to perform market analysis, debate strategies, and manage risk.

## Core Architecture
The framework follows a structured workflow:
1.  **Analyst Team**: Fetches and analyzes data.
    -   `Fundamentals Analyst`: Financial metrics.
    -   `Sentiment Analyst`: News and social media mood.
    -   `Technical Analyst`: MACD, RSI, etc.
    -   `News Analyst`: Macroeconomic events.
2.  **Researcher Team**: Bullish and Bearish researchers debate the analysts' reports.
3.  **Trader Agent**: Composes an investment plan based on the research.
4.  **Risk Management & Portfolio Manager**: A final debate on risk followed by PM approval/rejection.

## Key Files
- `main.py`: Entry point for running the framework programmatically.
- `cli/main.py`: Interactive CLI interface.
- `tradingagents/graph/trading_graph.py`: The core LangGraph orchestration logic.
- `tradingagents/default_config.py`: Global configuration settings.
- `tradingagents/agents/`: Definitions of agent prompts and behaviors.

## Setup & Usage
### Environment Variables
Ensure the following keys are set in your `.env` file:
- `GOOGLE_API_KEY`: For Gemini models (highly recommended for this agent).
- `OPENROUTER_API_KEY`: If using OpenRouter.
- `ALPHA_VANTAGE_API_KEY`: For some data providers (optional).

### Running the CLI
```bash
tradingagents
# or
python -m cli.main
```

### Programmatic Usage
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(config=DEFAULT_CONFIG)
_, decision = ta.propagate("AAPL", "2024-05-10")
print(decision)
```

## Development Guidelines
- **LangGraph**: Modifications to the flow should be made in `tradingagents/graph/setup.py` and `tradingagents/graph/trading_graph.py`.
- **Agents**: Prompts are located in `tradingagents/agents/prompts/`.
- **Data**: Data fetching logic is in `tradingagents/dataflows/`.

## Integration Ideas
- **Alpaca/Paper Trading**: Connect the Portfolio Manager's decision to a live paper trading account.
- **Custom Analysts**: Add specific analysts for crypto, commodities, or alternative data.
- **Enhanced Reflection**: Use more granular performance metrics for the memory log.

---
*Created by Gemini CLI for project management and architectural guidance.*
