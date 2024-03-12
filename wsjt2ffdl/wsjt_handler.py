# Copyright(C) 2024 Jason D. McCormick
# Distributed under the "3 Clause BSD License"
# See LICENSE.md with the source

import logging
import pprint
import re
import socketserver
from . import wsjt_decoder, wsjt_qso

__BUILD_ID = "@@HEAD-DEVELOP@@"
log = logging.getLogger(__name__)

class WsjtHandler(socketserver.BaseRequestHandler):
    """ handler class for the UDP server """
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        #log.debug(f"Received {len(data)} bytes from {self.client_address[0]}")
        r = wsjt_decoder.decode_message(data, self.client_address[0])
        
        if r != None:
            log.debug(f"call: {r.dx_call}")
            log.debug(f"logclock: {r.datetime_on}")
            rband = self.xfreq_to_band(r.tx_freq)
            log.debug(f"band: {rband}")
            log.debug(f"exch_rcvd: {r.exch_rcvd}")
            rclass , rsect = re.split(r"\s+", r.exch_rcvd)
            log.debug(f"opclass: {rclass}")
            r.mode = "DATA"
            log.debug(f"mode: {r.mode}")
            log.debug(f"callsign: {r.de_call}")
            log.debug(f"section: {rsect}")

            if r.op_call is None or r.op_call == "":
                r.op_call = r.dx_call
            log.debug(f"operator: {r.op_call}")
            
    def xfreq_to_band(self, freq: int):
        if freq >= 1800000 and freq <= 2000000:
            return "160M"
        if freq >= 3500000 and freq <= 4000000:
            return "80M"
        if freq >= 7000000 and freq <= 7300000:
            return "40M"
        if freq >= 14000000 and freq <= 14350000:
            return "20M"
        if freq >= 21000000 and freq <= 21450000:
            return "15M"
        if freq >= 28000000 and freq <= 29700000:
            return "10M"
        if freq >= 50000000 and freq <= 54000000:
            return "6M"
        if freq >= 144000000 and freq <= 146000000:
            return "2M"
        if freq >= 420000000 and freq <= 450000000:
            return "70CM"
        
        return "UNKN"
        
