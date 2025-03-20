import zmq, json, time, os
from base64 import b64encode

from modules.utils import on_pi, get_logger_params, on_windows
from ..settings.settings import save_config

class ZMQ_Server:
    def __init__(self, logger_instance=None):
        print("INIT")

        self.logger = logger_instance
        self.ON_PI = on_pi()
        self.UUID_VAL, self.USER = get_logger_params(self.ON_PI)

    def update_settings(self, command_dictionary):
        return {'Result': 'Settings Updated, Restarting Application'}

    def handle_command(self, command):
        command_dictionary = json.loads(command)
        if 'command' in command_dictionary:
            command = command_dictionary['command']
            if command == 'update settings':
                return self.update_settings(command_dictionary)
            else:
                return {'Error': 'unknown command %s' % command}
        else:
            self.logger.error(f'malformed command: {str(command_dictionary)}')
            return {'Error': 'malformed command'}


    def start_mq_server(self):
        # self.logger = Logger(log_params)
        self.zmq_context = zmq.Context()
        self.zmq_socket = self.zmq_context.socket(zmq.REP)
        self.zmq_socket.bind("tcp://*:5050")
        while True:
            message = self.zmq_socket.recv()
            response = self.handle_command(message)
            time.sleep(0.1)
            self.zmq_socket.send(json.dumps(response))