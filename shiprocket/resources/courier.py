from .base import Resource
class Courier(Resource):
    def __init__(self, client=None):
        super(Courier, self).__init__(client)

    """
    class to manage couriers in Shiprocket.
    """

    def genrate_awb_for_shipment(self, data={}):
        path = 'courier/assign/awb'
        return self._request('POST', path, data=data)

    def check_courier_serviceability(self, params={}):
        path = 'courier/serviceability'
        return self._request('GET', path, params=params)

    def get_list_of_couriers(self, params={}):
        path = 'courier/courierListWithCounts'
        return self._request('GET', path, params=params)

    def request_for_shipment_pickup(self, data={}):
        path = 'courier/generate/pickup'
        return self._request('POST', path, data=data)
