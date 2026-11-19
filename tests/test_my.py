"""네트워크 없이 가공 로직만 검사하는 테스트. 실행: pytest"""

import pandas as pd
import pytest

import stock
import policy

def test_window_60_is_allowed():
   policy.check_window(60)

def test_normalize_lowercase_us_ticker():
    result = stock.normalize_ticker("appl")
    assert result == ["APPL"]    

def test_output_without_order_id_passes():
    policy.enforce_output({"rows": [{"qty": 10}]})
