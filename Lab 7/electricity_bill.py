
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str) or not reading.strip():
        raise ValueError("Reading must be a non-empty string.")

    parts = reading.split(":")

    if len(parts) != 2:
        raise ValueError("Reading must contain exactly one colon.")

    try:
        previous = int(parts[0].strip())
        current = int(parts[1].strip())
    except ValueError:
        raise ValueError("Meter readings must be integers.")

    if previous < 0 or current < 0:
        raise ValueError("Meter readings cannot be negative.")

    if current < previous:
        raise ValueError("Current reading cannot be less than previous reading.")

    return current - previous


def daily_average(units_csv):
    if not isinstance(units_csv, str) or not units_csv.strip():
        raise ValueError("Daily units must be a non-empty CSV string.")

    try:
        units = [int(value.strip()) for value in units_csv.split(",")]
    except ValueError:
        raise ValueError("Daily units must contain valid integers.")

    if not units:
        raise ValueError("At least one daily reading is required.")

    if any(unit < 0 for unit in units):
        raise ValueError("Daily units cannot be negative.")

    return round(sum(units) / len(units), 2)


def tariff_rate(code):
    if not isinstance(code, str) or not code.strip():
        raise ValueError("Tariff code must be a non-empty string.")

    parts = code.strip().split("-")

    if len(parts) != 2:
        raise ValueError("Tariff code must follow CATEGORY-SLAB format.")

    category, slab = [part.strip().upper() for part in parts]

    if category not in RATES:
        raise ValueError("Invalid tariff category.")

    if slab not in SLAB:
        raise ValueError("Invalid tariff slab.")

    return RATES[category] * SLAB[slab]


def main():
    print("==== Running units_consumed ====")
    try:
        user_input = input(
            "Enter meter readings as previous:current (e.g. 1200:1350): "
        )
        print("Units Consumed:", units_consumed(user_input))
    except ValueError as exc:
        print("Invalid meter reading:", exc)

    print("\n==== Running daily_average ====")
    try:
        user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
        print("Daily Average:", daily_average(user_input))
    except ValueError as exc:
        print("Invalid daily units:", exc)

    print("\n==== Running tariff_rate ====")
    try:
        user_input = input("Enter a tariff code (e.g. DOM-A): ")
        print("Rate per Unit:", tariff_rate(user_input))
    except ValueError as exc:
        print("Invalid tariff code:", exc)


if __name__ == "__main__":
    main()
