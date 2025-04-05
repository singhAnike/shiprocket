from .base import Resource
class LabelsManifestsInvoice(Resource):
    def __init__(self, client=None):
        super(LabelsManifestsInvoice, self).__init__(client)
    
    """
    class to manage labels, manifests, and invoices in Shiprocket.
    """

    def generate_manifest(self, data={}):
        path = 'manifests/generate'
        return self._request('POST', path, data=data)

    def print_manifest(self, data={}):
        path = 'manifests/print'
        return self._request('POST', path, data=data)

    def generate_label(self, data={}):
        path = 'courier/generate/label'
        return self._request('POST', path, data=data)

    def genrate_invoice(self, data={}):
        path = 'orders/print/invoice'
        return self._request('POST', path, data=data)