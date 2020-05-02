#!/usr/bin/env python3
import socket
import logging 

from dns_generator import ClientHandler

root_logger = logging.getLogger()
root_logger.setLevel(level=logging.INFO)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_bind_ip_and_port():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return host_ip, 53


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip, port = get_bind_ip_and_port()
    sock.bind((ip, port))
    logger.info("DNS Listening on {0}:{1} ...".format(ip, port))
    while True:
        data, address = sock.recvfrom(650)
        client = ClientHandler(address, data, sock)
        client.run()


if __name__ == "__main__":
    main()
