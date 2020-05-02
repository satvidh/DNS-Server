import threading
from dns_generator import DNSGen
import logging 

logger = logging.getLogger(__name__)


class ClientHandler(threading.Thread):
    """
    Class to handle multiple client DNS requests
    """

    def __init__(self, address, data, sock):
        threading.Thread.__init__(self)
        logger.info("Connection from {0}".format(address))
        self.client_address = address
        self.dns_gen = DNSGen(data)
        self.sock = sock

    def run(self):
        resp = self.dns_gen.make_response()
        self.sock.sendto(self.dns_gen.make_response(), self.client_address)
        logger.info("Request from {0} for {1}".format(self.client_address, self.dns_gen.domain))
