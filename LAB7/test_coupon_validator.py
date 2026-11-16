
from hypothesis import given, strategies as st
from coupon_validator import split_code, most_expensive, expiry_days


@given(st.text() | st.none())
def test_split_code_no_crash(s):
    try:
        split_code(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"Unexpected crash in split_code: {e}"


@given(st.text() | st.none())
def test_most_expensive_no_crash(s):
    try:
        most_expensive(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"Unexpected crash in most_expensive: {e}"


@given(st.text() | st.none())
def test_expiry_days_no_crash(s):
    try:
        expiry_days(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"Unexpected crash in expiry_days: {e}"

