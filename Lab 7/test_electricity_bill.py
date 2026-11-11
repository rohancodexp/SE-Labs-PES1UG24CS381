
from hypothesis import given, strategies as st
import pytest

from electricity_bill import (
    units_consumed,
    daily_average,
    tariff_rate
)


# -------------------------------------------------
# 1. UNITS CONSUMED
# -------------------------------------------------

@given(st.text() | st.none())
def test_units_consumed_invalid_input(s):
    try:
        units_consumed(s)
    except ValueError:
        pass
    except Exception as exc:
        pytest.fail(
            f"Unexpected exception for {s!r}: "
            f"{type(exc).__name__}: {exc}"
        )


@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=0, max_value=100000)
)
def test_units_consumed_valid_readings(previous, current):
    if current < previous:
        with pytest.raises(ValueError):
            units_consumed(f"{previous}:{current}")
    else:
        assert units_consumed(
            f"{previous}:{current}"
        ) == current - previous


# -------------------------------------------------
# 2. DAILY AVERAGE
# -------------------------------------------------

@given(st.text() | st.none())
def test_daily_average_invalid_input(s):
    try:
        daily_average(s)
    except ValueError:
        pass
    except Exception as exc:
        pytest.fail(
            f"Unexpected exception for {s!r}: "
            f"{type(exc).__name__}: {exc}"
        )


@given(
    st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=1,
        max_size=30
    )
)
def test_daily_average_valid_values(values):
    csv_input = ",".join(map(str, values))
    expected = round(sum(values) / len(values), 2)

    assert daily_average(csv_input) == expected


# -------------------------------------------------
# 3. TARIFF RATE
# -------------------------------------------------

@given(st.text() | st.none())
def test_tariff_rate_invalid_input(s):
    try:
        tariff_rate(s)
    except ValueError:
        pass
    except Exception as exc:
        pytest.fail(
            f"Unexpected exception for {s!r}: "
            f"{type(exc).__name__}: {exc}"
        )


@given(
    st.sampled_from(["DOM", "COM"]),
    st.sampled_from(["A", "B"])
)
def test_tariff_rate_valid_codes(category, slab):
    rates = {"DOM": 3, "COM": 6}
    slabs = {"A": 1, "B": 2}

    assert tariff_rate(
        f"{category}-{slab}"
    ) == rates[category] * slabs[slab]


@given(st.integers(max_value=-1))
def test_daily_average_rejects_negative_units(value):
    with pytest.raises(ValueError):
        daily_average(str(value))
