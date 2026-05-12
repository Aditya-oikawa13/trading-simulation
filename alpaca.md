# Alpaca MCP Server: Natural Language Trading for LLMs

## Overview
The **Alpaca MCP (Model Context Protocol) Server** is a complete rewrite (v2) built with **FastMCP**. It exposes Alpaca's Trading and Market Data APIs as tools that can be dynamically discovered and invoked by MCP-compliant LLMs (like Claude, Gemini, or Cursor).

## Core Functionality
Instead of using a traditional library, the MCP server acts as a bridge:
- **Natural Language Execution**: Ask an LLM to "Buy 5 shares of AAPL" or "Show my portfolio history," and it will select and execute the correct Alpaca tool.
- **Dynamic Discovery**: Tools are generated from Alpaca's OpenAPI specs at runtime.
- **Unified Interface**: Supports Stocks, Options, Crypto, and Account Management.

## Setup & Configuration

### Prerequisites
- **uv**: Required for running the server (`uvx alpaca-mcp-server`).
- **Alpaca API Keys**: Paper or Live keys.

### Gemini CLI Configuration
Add the following to your `settings.json` for the Gemini CLI:
```json
{
  "mcpServers": {
    "alpaca": {
      "type": "stdio",
      "command": "uvx",
      "args": ["alpaca-mcp-server"],
      "env": {
        "ALPACA_API_KEY": "your_key",
        "ALPACA_SECRET_KEY": "your_secret",
        "ALPACA_PAPER_TRADE": "true"
      }
    }
  }
}
```

### Environment Variables
- `ALPACA_API_KEY`: (Required)
- `ALPACA_SECRET_KEY`: (Required)
- `ALPACA_PAPER_TRADE`: Default `true`. Set to `false` for live trading.
- `ALPACA_TOOLSETS`: Comma-separated list (e.g., `account,trading,stock-data`) to limit exposed tools.

## Available Toolsets
| Toolset | Description |
| :--- | :--- |
| `account` | Balances, portfolio history, activities. |
| `trading` | Orders, positions, options exercise. |
| `assets` | Asset lookup, calendar, market clock. |
| `stock-data` | OHLCV bars, quotes, trades, snapshots. |
| `crypto-data` | Crypto snapshots, orderbooks, historical data. |
| `options-data` | Option chains, Greeks, IV, snapshots. |
| `news` | News articles for tickers. |

## Integration with TradingAgents
The MCP server provides a powerful alternative to the `alpaca-py` library for `TradingAgents`:
1.  **Agent Tooling**: Directly provide the Alpaca tools to the `Trader` or `Portfolio Manager` agents.
2.  **Simplified Logic**: Instead of writing complex Python wrappers for Alpaca, the agents can use the MCP tools directly via the Gemini CLI's MCP support.
3.  **Human-in-the-Loop**: Use the MCP server in interactive sessions to verify agent decisions before they are executed.

---
*Created by Gemini CLI for Alpaca MCP integration guidance.*
