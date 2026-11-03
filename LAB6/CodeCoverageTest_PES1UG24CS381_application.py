import pytest

from electricity_bill import energy_charge, late_fee, subsidy


# ==========================================
# CODE COVERAGE TESTS
# ==========================================

# Energy charge tests

def test_domestic_low_usage():
    assert energy_charge(50, "domestic") == 200


def test_domestic_middle_slab():
    assert energy_charge(200, "domestic") == 850


def test_commercial_high_usage():
    assert energy_charge(400, "commercial") == 4350


def test_invalid_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(100, "industrial")


def test_negative_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")


# Late fee tests

def test_payment_on_time():
    assert late_fee(500, 0) == 0


def test_payment_within_15_days():
    assert late_fee(1000, 10) == 50


def test_payment_after_15_days():
    assert late_fee(2500, 20) == 225


# Subsidy tests

def test_senior_citizen_subsidy():
    assert subsidy(50, True, False) == 50


def test_solar_subsidy():
    assert subsidy(150, False, True) == 100


def test_high_usage_solar_subsidy():
    assert subsidy(400, True, True) == 0


def test_no_subsidy():
    assert subsidy(200, False, False) == 0