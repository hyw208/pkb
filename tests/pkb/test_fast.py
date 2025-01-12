import pytest 

def test_fast():
    from pkb.fast import app
    _app = app()
    assert _app