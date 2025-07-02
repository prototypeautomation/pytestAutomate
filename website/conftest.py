import pytest

def pytest_collection_modifyitems(items):
    order = {
        "test_TC001_Login_Success": 1,
        "test_TC002_Login_Fail":2,
        "test_TC003_Add_New_Company": 3,
        "test_TC004_Validate_New_Company": 4
    }
    items.sort(key=lambda item: order.get(item.name, 100))