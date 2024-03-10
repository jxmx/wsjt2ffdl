# Copyright(C) 2024 Jason D. McCormick
# Distributed under the "3 Clause BSD License"
# See LICENSE.md with the source

import logging
import pprint
import socketserver
from . import wsjt_decoder, wsjt_qso

__BUILD_ID = "@@HEAD-DEVELOP@@"
log = logging.getLogger(__name__)

class WsjtHandler(socketserver.BaseRequestHandler):
    """ handler class for the UDP server """
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        log.debug(f"Received {len(data)} bytes from {self.client_address[0]}")
        r = wsjt_decoder.decode_message(data, self.client_address[0])
        pprint.pprint(r)