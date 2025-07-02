import pytest

def pytest_collection_modifyitems(items):
    order = {
        "test_TC001_Login_Success": 1,
        "test_TC002_Login_Fail_Using_Wrong_Password": 2,
        "test_TC003_Login_Fail_Using_User_Not_Registered_In_Group": 3,
        "test_TC004_Login_Fail_Using_Inactive_User": 4,
        "test_TC005_Create_New_Customer_And_Veryfy_Data":5
    }
    items.sort(key=lambda item: order.get(item.name, 100))