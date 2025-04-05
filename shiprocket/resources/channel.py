from .base import Resource
class Channel(Resource):
    def __init__(self, client=None):
        super(Channel, self).__init__(client)
    
    """
    class to GET channels of the Shiprocket.
    """
    def get_channels(self, params={}):
        path = 'channels'
        return self._request('GET', path, params=params)