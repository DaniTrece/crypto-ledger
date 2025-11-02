import requests
from datetime import datetime
from .base import PriceProvider


class BCEProvider(PriceProvider):
    def get_price(
        self, symbol: str, timestamp: datetime, currency: str = "usd"
    ) -> float:
        """Get fiat conversion rate at a given timestamp.

        Supported: USD/EUR cross only (for now)
        """

        symbol = symbol.lower()
        currency = currency.lower()

        # Only two directions supported: USD → EUR or EUR → USD
        valid_pairs = {("usd", "eur"), ("eur", "usd")}

        if (symbol, currency) not in valid_pairs:
            raise ValueError(
                f"BCE only supports USD/EUR and EUR/USD, got {symbol}/{currency}"
            )

        date_str = timestamp.strftime("%Y-%m-%d")
        url = f"https://api.exchangerate.host/{date_str}?base={symbol.upper()}&symbols={currency.upper()}"

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            rate = r.json()["rates"][currency.upper()]
            return float(rate)

        except Exception as e:
            raise ValueError(f"BCEProvider failed for {symbol}/{currency}: {e}") from e
