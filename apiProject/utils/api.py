from utils.http_method import Http_methods
"""Methods for testing Google maps api"""

base_url = "https://rahulshettyacademy.com"   # base URL
key = "?key=qaclick123"   #Parameter for all requests



class Google_maps_api():

    """Method for creating a new location"""
    @staticmethod
    def create_new_place():
         json_for_create_new_place = {
             "location":{
         "lat":-38.383494,
         "lng":33.427362
         }, "accuracy":50,
         "name":"Frontlinehouse",
         "phone_number":"(+91)9838933937",
         "address":"29,sidelayout,cohen09",
         "types":[
         "shoe park",
         "shop"
         ],
         "website":"http://google.com",
         "language":"French-IN"
         }

         post_resource = "/maps/api/place/add/json"  # Post method resource
         post_url = base_url + post_resource + key
         print(post_url)
         result_post = Http_methods.post(post_url, json_for_create_new_place)
         print(result_post.text)
         return result_post

    """Method for checking a new location"""
    @staticmethod
    def get_new_place(place_id):

         get_recource = "/maps/api/place/get/json"   # GET method resource
         get_url = base_url + get_recource + key + "&place_id=" + place_id
         print(get_url)
         result_get = Http_methods.get(get_url)
         print(result_get.text)
         return result_get

    """Method for changing a new location"""

    @staticmethod
    def put_new_place(place_id):
        put_recource = "/maps/api/place/update/json"  # PUT method resource
        put_url = base_url + put_recource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
        "address": "100Leninastreet,RU",
        "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    """Method for deleting a new location"""

    @staticmethod
    def delete_new_place(place_id):
        delete_recource = "/maps/api/place/delete/json"  # DELETE method resource
        delete_url = base_url + delete_recource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete