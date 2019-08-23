import sys
import time

class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger('{}.log'.format(time.strftime('%Y-%m-%d-%H-%M-%S')), sys.stdout)
sys.stderr = Logger('{}.log'.format(time.strftime('%Y-%m-%d-%H-%M-%S')), sys.stderr)


print('djjj')
