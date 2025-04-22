from typing import Dict, Any, Optional
from pycoingecko import CoinGeckoAPI as CG
import asyncio
from functools import partial

class CoinGeckoAPI:
    def __init__(self):
        self.cg = CG()
        
    async def get_price(self, coin_id: str, vs_currency: str = "usd") -> Dict[str, float]:
        """获取加密货币当前价格"""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            partial(self.cg.get_price, ids=coin_id, vs_currencies=vs_currency)
        )
        return result

    async def get_market_chart(
        self, 
        coin_id: str,
        vs_currency: str = "usd",
        days: str = "1"
    ) -> Dict[str, Any]:
        """获取加密货币历史价格数据"""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            partial(
                self.cg.get_coin_market_chart_by_id,
                id=coin_id,
                vs_currency=vs_currency,
                days=days
            )
        )
        return result

    async def get_coin_info(self, coin_id: str) -> Dict[str, Any]:
        """获取加密货币详细信息"""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            partial(self.cg.get_coin_by_id, id=coin_id)
        )
        return result

    async def get_trending(self) -> Dict[str, Any]:
        """获取趋势币种"""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            self.cg.get_search_trending
        )
        return result