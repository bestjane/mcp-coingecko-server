# mcp-server-coingecko: A CoinGecko MCP server

## 概述

一个用于加密货币数据查询的 Model Context Protocol 服务器。该服务器提供了通过大语言模型与 CoinGecko API 交互的工具，可以查询加密货币的价格、历史数据和市场信息。

### 工具函数

1. `get_current_time`
   - 获取当前时间
   - 返回: 当前时间的字符串格式 (YYYY-MM-DD HH:MM:SS)

2. `get_coin_price`
   - 获取加密货币当前价格
   - 输入:
     - `coin_id` (string): 币种ID (如 'bitcoin', 'ethereum')
     - `vs_currency` (string, 可选): 目标货币单位 (默认: 'usd')
   - 返回: 当前价格数据

3. `get_coin_history`
   - 获取加密货币历史价格数据
   - 输入:
     - `coin_id` (string): 币种ID
     - `days` (string): 时间范围 (1/7/14/30/90/180/365/max)
     - `vs_currency` (string, 可选): 目标货币单位 (默认: 'usd')
   - 返回: 历史价格数据

4. `get_coin_info`
   - 获取加密货币详细信息
   - 输入:
     - `coin_id` (string): 币种ID
   - 返回: 币种详细信息

5. `get_trending_coins`
   - 获取24小时内热门币种
   - 返回: 热门币种列表
   
## 运行步骤

直接运行：
```bash
uv run mcp-coingecko-server
```