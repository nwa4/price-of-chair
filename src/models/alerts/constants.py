__author__ = 'jslvtr'

import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_APY_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"