import requests
from datetime import datetime
from .base import PriceProvider


class BinanceProvider(PriceProvider):
    def get_price(
        self, symbol: str, timestamp: datetime, currency: str = "usd"
    ) -> float:
        """Get price from Binance using minute-level historical kline data."""
        if currency.lower() != "usd":
            raise ValueError(
                "Binance provider supports only USD. Convert later via BCE"
            )

        url = "https://api.binance.com/api/v3/klines"
        ts_ms = int(timestamp.timestamp() * 1000)

        params = {
            "symbol": f"{symbol.upper()}USDT",
            "interval": "1m",
            "startTime": ts_ms,
            "limit": 1,
        }

        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            data = r.json()

            if not data:
                raise ValueError(
                    f"Price not found for {symbol} on Binance at {timestamp}"
                )

            open_price = float(data[0][1])
            return open_price

        except Exception as e:
            raise ValueError(f"Binance price fetch error: {e}") from e
