from .base import Resource
class Shipment(Resource):
    def __init__(self, client=None):
        super(Shipment, self).__init__(client)
    
    """
    class to manage shipments in Shiprocket.
    """
    def get_all_shipments(self, params={}):
        path = 'shipments'
        return self._request('GET', path, params=params)

    def get_shipment_details(self, shipment_id, params={}):
        path = f'shipments/{shipment_id}'
        return self._request('GET', path, params=params)

    def cancel_shipment(self, data={}):
        path = 'orders/cancel/shipment/awbs'
        return self._request('POST', path, data=data)
