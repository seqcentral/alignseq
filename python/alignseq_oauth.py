import OAuthSimple
import httplib2
import urllib

class AlignSeq_OAuth(object):

    client = None

    def __init__(self, consumer_key, consumer_secret):
        self.client = OAuthSimple.OAuthSimple(apiKey=consumer_key, sharedSecret=consumer_secret)


    def make_request(self, method, url, opt):
        self.client.reset()

        obj = self.client.sign({'action':method, 'parameters':opt, 'path':url});

        if method != 'POST':
            url = obj.get('signed_url')
            body = None
        else:
            body = urllib.urlencode(opt).replace('+', '%20')


        return httplib2.Http.request(httplib2.Http(timeout=30), url, method=method, body=body, \
                   headers={'Authorization':obj.get('header'), 'Content-Type': 'application/x-www-form-urlencoded'})
