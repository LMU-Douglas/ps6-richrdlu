import pytest
from balancing_power import * 
# -------------------------------
# Tests for Problem 1: Balancing Power
# -------------------------------

def test_power_balanced_case():
    assert is_power_balanced(5, "1 2 1 3 2") == "Power Balanced"

def test_future_one_dominates():
    assert is_power_balanced(5, "1 2 1 3 1") == "Future One Dominates"

def test_two_gether_dominates():
    assert is_power_balanced(6, "2 2 2 1 3 2") == "Two-gether Dominates"

def test_triple_harmony_dominates():
    assert is_power_balanced(4, "3 3 3 2") == "Triple Harmony Dominates"
    
def test_equal():
    assert is_power_balanced(3, "1 2 3") == "Power Balanced" 

    is_power_balanced(5, [1, 1, 2, 2, 3])
# Output: Power Balanced
