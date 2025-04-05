from .base import Resource
class Order(Resource):
    def __init__(self, client=None):
        super(Order, self).__init__(client)
    """
    class to manage orders in Shiprocket.
    """
    def create_custom_order(self, data={}):
        path = 'orders/create/adhoc'
        return self._request('POST', path, data=data)

    def create_channel_specific_order(self, data={}):
        path = 'orders/create'
        return self._request('POST', path, data=data)

    def change_pickup_location(self, data={}):
        path = 'orders/address/pickup'
        return self._request('PATCH', path, data=data)

    def update_customer_delivery_address(self, data={}):
        path = 'orders/address/update'
        return self._request('POST', path, data=data)

    def update_order(self, data={}):
        path = 'orders/update/adhoc'
        return self._request('POST', path, data=data)

    def cancel_order(self, data={}):
        path = 'orders/cancel'
        return self._request('POST', path, data=data)

    def add_inventory(self, data={}):
        path = 'orders/fulfill'
        return self._request('PATCH', path, data=data)

    def map_unmapped_products(self, data={}):
        path = 'orders/mapping'
        return self._request('PATCH', path, data=data)

    # there is some issue with this API
    def import_orders_in_bulk(self, data={}):
       pass

    def get_all_orders(self, params={}):
        path = 'orders'
        return self._request('GET', path, params=params)

    def get_specific_order_details(self, order_id, params={}):
        path = f'orders/show/{order_id}'
        return self._request('GET', path, params=params)

    def export_orders(self, data={}):
        path = 'orders/export'
        return self._request('POST', path, data=data)
