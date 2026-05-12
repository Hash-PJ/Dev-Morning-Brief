from sources.base import BaseSource


class PriceSource(BaseSource):
    FEX_URL = "https://api.exchangerate-api.com/v4/latest/USD"
    METALS_URL = "https://api.gold-api.com/price/"
    TROY_GM = 31.1035

    def fetch(self, currency="USD"):
        fx = self.get(self.FEX_URL)
        if not fx:
            return None
        if currency not in fx['rates'].keys():
            currency = "USD"
            print("Conversion not possible. Hence using USD")
        usd_cur = fx['rates'].get(currency, 1)
        metals = {"Silver": "XAG", "Gold": "XAU"}
        result = [{"name": f"USD/{currency}", "price": usd_cur, "label": "Foriegn Exchange"}]
        for k, v in metals.items():
            usd_price = self.get(self.METALS_URL+v+'/'+currency)
            sym = usd_price.get('currencySymbol')
            usd_price = usd_price.get("price")
            if usd_price:
                if usd_cur != 1:
                    price = (usd_price / self.TROY_GM) * usd_cur
                else:
                    price = usd_price
                result.append({
                    "name": k.title(),
                    "price": sym + str(round(price, 2)),
                    "label": "Intl. spot price"
                })
        return result
