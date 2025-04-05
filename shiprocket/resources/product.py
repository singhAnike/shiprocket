from .base import Resource

class Product(Resource):
    def __init__(self, client=None):
        super(Product, self).__init__(client)

    """
    class to GET products from the Shiprocket.
    """
    def get_all_products(self, params={}):
        path = 'products'
        return self._request('GET', path, params=params)
    
    def get_specific_product_details(self, product_id, params={}):
        path = f'products/show/{product_id}'
        return self._request('GET', path, params=params)
    
    def add_product(self, data={}):
        path = 'products'
        return self._request('POST', path, data=data)