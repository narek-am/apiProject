import json

from requests import Response
import allure
from utils.checking import Checking

from utils.api import Google_maps_api

"""Creating, changing and deleting a new location"""


@allure.epic("Test create place")
class TestCreatePlace:

    @allure.description("Test create,update, delete new place")
    def test_crate_new_place(self):
        print("Method POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_tocken(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_tocken(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '29,sidelayout,cohen09')

        print("Method PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_tocken(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Method GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_tocken(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '100Leninastreet,RU')

        print("Method DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_tocken(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Nethod GET DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_tocken(result_get, ['msg'])
        Checking.check_json_searh_vord_in_value(result_get, 'msg', 'Get operation failed,')

        print("Testing creating, changing and deleting a new location was successful!!!")
