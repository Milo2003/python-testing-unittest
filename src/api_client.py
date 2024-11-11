import requests
import ipaddress


def get_location(ip):
    ipaddress.ip_address(ip)
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import pdb; pdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
        "language": data["language"],
        "currency": data["currency"]["code"],
        "zip_code": data["zipCode"],
    }


# if __name__ == "__main__":
#     print(get_location("8.8.8.8"))
