import os

from openpilot.common.api.base import BaseApi

# rbpilot: talk to the self-hosted connect server on skynet (Home Assistant app rbconnect), never comma's.
API_HOST = os.getenv('API_HOST', 'https://skynet.tssnc.net:3443')
CONNECT_URL = os.getenv('CONNECT_URL', 'https://skynet.tssnc.net:3443')


class CommaConnectApi(BaseApi):
  def __init__(self, dongle_id):
    super().__init__(dongle_id, API_HOST)
    self.user_agent = "openpilot-"
