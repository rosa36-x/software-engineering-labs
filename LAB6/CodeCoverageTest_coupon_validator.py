
import pytest
from coupon_validator import coupon_discount, best_discount, is_expired


# ==========================================
# 1. TESTS FOR coupon_discount()
# ==========================================

def test_empty_cart():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome10_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome10_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend20_high_cart():
    assert coupon_discount("WEEKEND20", 600, True, "sat") == 120


def test_weekend20_low_cart():
    assert coupon_discount("WEEKEND20", 400, True, "sun") == 50


def test_weekend20_weekday():
    assert coupon_discount("WEEKEND20", 600, True, "mon") == 0


def test_flat100_above_threshold():
    assert coupon_discount("FLAT100", 400, True, "mon") == 100


def test_flat100_below_threshold():
    assert coupon_discount("FLAT100", 300, True, "mon") == 0


def test_unknown_coupon():
    assert coupon_discount("INVALID", 500, True, "sat") == 0


# ==========================================
# 2. TESTS FOR best_discount()
# ==========================================

def test_best_discount_empty_list():
    assert best_discount([], 500, True, "sat") == 0


def test_best_discount_selects_highest():
    assert best_discount(
        ["WELCOME10", "WEEKEND20"], 600, True, "sat"
    ) == 120


def test_best_discount_no_valid_coupon():
    assert best_discount(["INVALID"], 500, True, "mon") == 0


def test_best_discount_below_cap():
    assert best_discount(["WEEKEND20"], 500, True, "sat") == 100


# ==========================================
# 3. TESTS FOR is_expired()
# ==========================================

def test_expiry_negative_validity():
    assert is_expired(10, 5, -1) is True


def test_expiry_within_validity():
    assert is_expired(10, 5, 10) is False


def test_expiry_after_validity():
    assert is_expired(16, 5, 10) is True
