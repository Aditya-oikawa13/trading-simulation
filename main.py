import os
from dotenv import load_dotenv
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Load environment variables
load_dotenv()

# Use local directories within the project to avoid permission issues
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_HOME = os.path.join(BASE_DIR, ".tradingagents_local")

config = DEFAULT_CONFIG.copy()
config["results_dir"] = os.path.join(LOCAL_HOME, "logs")
config["data_cache_dir"] = os.path.join(LOCAL_HOME, "cache")
config["memory_log_path"] = os.path.join(LOCAL_HOME, "memory", "trading_memory.md")

# Stick with OpenRouter but try a different model
config["llm_provider"] = "openrouter"
config["deep_think_llm"] = "google/gemini-2.0-flash-001"
config["quick_think_llm"] = "google/gemini-2.0-flash-001"

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
# Use a date that is likely to have data (e.g., yesterday or today)
_, decision = ta.propagate("AAPL", "2026-05-11")
print(decision)
