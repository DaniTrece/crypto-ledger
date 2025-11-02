from abc import ABC, abstractmethod
from datetime import datetime


class PriceProvider(ABC):
    @abstractmethod
    def get_price(
        self, symbol: str, timestamp: datetime, currency: str = "usd"
    ) -> float:
        """Retrieve the asset price at a specific point in time.

        Args:
            symbol: The asset ticker or symbol (e.g., "BTC", "ETH").
            timestamp: The timestamp for which the price should be retrieved.
            currency: Currency code for the price (default "usd").

        Returns:
            float: The price of the asset in the given currency at the given timestamp.

        Raises:
            ValueError: If the symbol or currency is invalid or the price cannot be retrieved.
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
