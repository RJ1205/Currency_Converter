import requests

BASE_URL = "http://www.floatrates.com/daily"
DEFAULT_CACHE = ["usd", "eur"]


def fetch_exchange_data(base_currency: str) -> dict:
    """Fetch exchange rate data from FloatRates for the given base currency."""
    url = f"{BASE_URL}/{base_currency.lower()}.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def initialize_cache(data: dict) -> dict:
    """Initialize the cache with USD and EUR if available."""
    cache = {}
    for curr in DEFAULT_CACHE:
        if curr in data:
            cache[curr] = data[curr]["rate"]
    return cache


def get_rate(currency: str, cache: dict, data: dict) -> float:
    """Retrieve the rate from cache or fetch it from data."""
    print("Checking the cache...")
    if currency in cache:
        print("Oh! It is in the cache!")
        return cache[currency]
    else:
        print("Sorry, but it is not in the cache!")
        rate = data[currency]["rate"]
        cache[currency] = rate
        return rate



def main():
    base_currency = input().lower()
    data = fetch_exchange_data(base_currency)
    cache = initialize_cache(data)

    while True:
        target_currency = input().lower()
        if not target_currency:
            break

        amount = float(input())
        rate = get_rate(target_currency, cache, data)

        if rate is not None:
            received = amount * rate
            print(f"You received {received:.2f} {target_currency.upper()}.")


if __name__ == "__main__":
    main()
