from .base import Resource
class ReturnOrder(Resource):
    def __init__(self, client=None):
        super(ReturnOrder, self).__init__(client)
    """
    class to manage return orders in Shiprocket.
    """
    def create_return_order(self, data={}):
        path = 'orders/create/return'
        return self._request('POST', path, data=data)

    def get_all_return_orders(self, params={}):
        path = 'orders/processing/return'
        return self._request('GET', path, params=params)