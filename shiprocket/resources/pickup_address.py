from .base import Resource
class PickupAddress(Resource):
    def __init__(self, client=None):
        super(PickupAddress, self).__init__(client)
    
    """
    class to manage pickup addresses in Shiprocket.
    """
    def get_all_pickup_locations(self, params={}):
        path = 'settings/company/pickup'
        return self._request('GET', path, params=params)

    def add_new_pickup_location(self, data={}):
        path = 'settings/company/addpickup'
        return self._request('POST', path, data=data)
