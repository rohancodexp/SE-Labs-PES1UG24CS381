import pytest

from electricity_bill import energy_charge, late_fee, subsidy


# ==========================================
# BRANCH COVERAGE TESTS
# ==========================================

# ENERGY CHARGE: connection validation

def test_unknown_connection_branch():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(100, "industrial")


def test_negative_units_branch():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


# ENERGY CHARGE: all three unit slabs

def test_units_below_or_equal_100():
    assert energy_charge(100, "domestic") == 350


def test_units_between_101_and_300():
    assert energy_charge(200, "domestic") == 850


def test_units_above_300():
    assert energy_charge(301, "domestic") == 1358


# ENERGY CHARGE: both connection types

def test_domestic_connection_branch():
    assert energy_charge(50, "domestic") == 200


def test_commercial_connection_branch():
    assert energy_charge(50, "commercial") == 450


# LATE FEE: days late conditions

def test_no_late_fee_branch():
    assert late_fee(1000, 0) == 0


def test_late_fee_within_15_days_branch():
    assert late_fee(1000, 15) == 50


def test_late_fee_after_15_days_branch():
    assert late_fee(1000, 16) == 100


# LATE FEE: bill amount conditions

def test_bill_above_2000_branch():
    assert late_fee(2500, 20) == 225


def test_bill_equal_to_2000_branch():
    assert late_fee(2000, 20) == 100


# SUBSIDY: senior citizen conditions

def test_senior_citizen_qualifies():
    assert subsidy(100, True, False) == 50


def test_units_above_100_no_senior_subsidy():
    assert subsidy(101, True, False) == 0


def test_non_senior_no_senior_subsidy():
    assert subsidy(100, False, False) == 0


# SUBSIDY: solar conditions

def test_solar_subsidy_with_low_usage():
    assert subsidy(200, False, True) == 100


def test_solar_subsidy_at_300_units():
    assert subsidy(300, False, True) == 100


def test_solar_subsidy_above_300_units():
    assert subsidy(301, False, True) == 0


def test_no_solar_subsidy():
    assert subsidy(200, False, False) == 0