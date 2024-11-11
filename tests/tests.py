def calculate_total(products, discount):
    total = 0
    for product in products:
        total += product["price"] - discount / 100 * product["price"]
    return total.__int__()


def test_calculate_total_with_empty_list():
    assert calculate_total([], 0) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "iPhone", "price": 1000}]
    print(calculate_total(products, 30))
    assert calculate_total(products, 30) == 700


def test_calculate_total_with_multiple_products():
    products = [
        {"name": "iPhone", "price": 1000},
        {"name": "MacBook", "price": 2000},
        {"name": "iPad", "price": 500},
    ]
    print(calculate_total(products, 20))
    assert calculate_total(products, 20) == 2800


if __name__ == "__main__":
    test_calculate_total_with_multiple_products()
