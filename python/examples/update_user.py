import ConfigParser

import sys
# add path to alignseq.py
sys.path.append('..')
# add path to OAuthSimple.py
sys.path.append('../../oauthsimple/python/OAuthSimple')

import alignseq

config = ConfigParser.RawConfigParser()
config.read('../../alignseq.conf')

client = alignseq.AlignSeq({ 'consumer_key': config.get('oauth', 'consumer_key'), \
    'consumer_secret': config.get('oauth', 'consumer_secret')})

response = client.update_user(1, {'name': '12'})

print response
