

class EndpointFactory:

    BASE_URL = "https://api.exchangeratesapi.io/v1/"
    API_KEY = "17c2b9fd0b3746fbbe13f0b0479a4bbf"

    @classmethod
    def get_historical_rates_endpoint(cls, date, base, quote_symbols):
        """Get Historical End points"""
        return f"{cls.BASE_URL}/{date.strftime("%Y-%m-%d")}?access_key={cls.API_KEY}&base=GBP&symbols={quote_symbols.join(",")}"