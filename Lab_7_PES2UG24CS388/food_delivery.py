import math
import re

def parse_order(items_csv):
    """
    Parses a CSV string of items formatted as 'name:qty' into a dictionary.
    Handles unexpected, empty, malformed, non-string, or None inputs safely.
    """
    order = {}
    if not isinstance(items_csv, str):
        return order

    for item in items_csv.split(','):
        item = item.strip()
        if not item or ':' not in item:
            continue
        parts = item.split(':')
        if len(parts) != 2:
            continue
        name, qty_str = parts[0].strip(), parts[1].strip()
        if not name:
            continue
        try:
            qty = int(qty_str)
            if qty > 0:
                order[name] = qty
        except (ValueError, TypeError):
            continue
    return order

def delivery_eta(distance_km):
    """
    Calculates estimated delivery time in minutes based on distance in km:
    ETA = 15 + distance_km * 4.
    Safely handles non-numeric strings, negative numbers, None, NaN, and Inf.
    """
    if distance_km is None:
        return 0
    try:
        dist = float(distance_km)
        if math.isnan(dist) or math.isinf(dist) or dist < 0:
            return 0
        return int(15 + dist * 4)
    except (ValueError, TypeError, OverflowError):
        return 0

def coupon_discount(code):
    """
    Extracts the numerical discount percentage/value from a coupon code with prefix 'SAVE'.
    Safely handles non-string values, missing prefixes, malformed formats, and None.
    """
    if not isinstance(code, str):
        return 0
    
    match = re.search(r'SAVE(\d+)', code.upper())
    if match:
        try:
            return int(match.group(1))
        except (ValueError, TypeError):
            return 0
    return 0

def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)

if __name__ == "__main__":
    main()
