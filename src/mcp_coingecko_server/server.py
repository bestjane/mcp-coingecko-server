import logging
import asyncio
from typing import Optional, Dict, Any
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from .coingecko_api import CoinGeckoAPI

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("mcp-coingecko.log")
    ],
    force=True
)

logger = logging.getLogger("mcp-coingecko")

# 初始化 FastMCP 服务器
mcp = FastMCP(
    "mcp-coingecko",
    version="0.1.0",
    description="MCP CoinGecko Server for cryptocurrency data",
    dependencies=["pycoingecko"],
    env_vars={},
    debug=True,
    port=8003
)

coin_api = CoinGeckoAPI()

@mcp.tool()
async def get_current_time() -> str:
    """Get current time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
async def get_coin_price(coin_id: str, vs_currency: str = "usd") -> Dict[str, float]:
    """Get current price of a cryptocurrency
    
    Args:
        coin_id: The coin ID (e.g., 'bitcoin', 'ethereum')
        vs_currency: The target currency (default: 'usd')
    """
    data = await coin_api.get_price(coin_id, vs_currency)
    return data

@mcp.tool()
async def get_coin_history(coin_id: str, days: str, vs_currency: str = "usd") -> Dict[str, Any]:
    """Get historical price data of a cryptocurrency
    
    Args:
        coin_id: The coin ID (e.g., 'bitcoin', 'ethereum')
        days: Number of days (1/7/14/30/90/180/365/max)
        vs_currency: The target currency (default: 'usd')
    """
    data = await coin_api.get_market_chart(coin_id, vs_currency, days)
    return data

@mcp.tool()
async def get_coin_info(coin_id: str) -> Dict[str, Any]:
    """Get detailed information about a cryptocurrency
    
    Args:
        coin_id: The coin ID (e.g., 'bitcoin', 'ethereum')
    """
    data = await coin_api.get_coin_info(coin_id)
    return data

@mcp.tool()
async def get_trending_coins() -> Dict[str, Any]:
    """Get list of trending coins in the last 24 hours"""
    data = await coin_api.get_trending()
    return data

async def run_server():
    """运行 MCP CoinGecko 服务器"""
    logger.info("正在初始化 CoinGecko 服务器...")
    try:
        logger.info("正在启动 MCP CoinGecko 服务器...")
        await mcp.run_sse_async()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        await mcp.shutdown()
    except Exception as e:
        logger.error(f"Server failed: {e}")
        raise
    finally:
        logger.info("Server shutdown complete")

def main():
    """Start the CoinGecko MCP server."""
    try:
        print("CoinGecko MCP Server")
        print("Starting server... Press Ctrl+C to exit")
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Server stopped.")