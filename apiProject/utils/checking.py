"""Methods for checking the responses of our requests"""
import json
from requests import Response


class Checking():

    """Method for checking code status"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully!!! Status code = " + str(response.status_code))
        else:
            print("Failure!!! Status code = " + str(response.status_code))


    """Method for checking the presence of required fields in the response"""
    @staticmethod
    def check_json_tocken(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields are present")

    """Method for checking the value of required fields in the response"""
    @staticmethod
    def check_json_value(response: Response,field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " is correct!!!")

    """Method for checking the value of the required fields in the response of the backword request"""
    @staticmethod
    def check_json_searh_vord_in_value(response: Response,field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in  check_info:
            print("The " + search_word + "  word there is!!!")
        else:
            print("The  " + search_word + "  word is absent!!!")


