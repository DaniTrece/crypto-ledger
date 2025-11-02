import requests
from datetime import datetime
from .base import PriceProvider


class CoinGeckoProvider(PriceProvider):
    def get_price(
        self, symbol: str, timestamp: datetime, currency: str = "usd"
    ) -> float:
        """Get historical daily price from CoinGecko."""

        currency = currency.lower()
        if currency not in ("usd", "eur"):
            raise ValueError("CoinGecko only supports USD and EUR")

        date_str = timestamp.strftime("%d-%m-%Y")
        url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}/history?date={date_str}"

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()

            return float(data["market_data"]["current_price"][currency])

        except Exception as e:
            raise ValueError(f"CoinGecko price fetch error: {e}") from e
