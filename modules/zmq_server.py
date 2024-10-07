import zmq, json, time, os
from base64 import b64encode

from modules.utils import on_pi


class ZMQ_Server:
    def __init__(self):
        print("INIT")