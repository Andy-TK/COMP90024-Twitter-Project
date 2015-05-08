# argParser.py
# ~Jun Min (542339)

import argparse

class ArgParser:
    '''Argument parsing simplified'''

    def __init__(self):
        '''Grab args and parse with argparse'''
        parser = argparse.ArgumentParser(
                description = 'Specify whether to write to File or send to \
                        REST API route')

        # Dump to specified file
        parser.add_argument('--dump')

        # Send to REST API
        parser.add_argument('--ip')

        # Rest API Route (defaults to 80)
        parser.add_argument('--port', type=int, default=80)

        args = parser.parse_args()

        if not (args.dump or args.ip):
            parser.error('No api or file specified, set --ip or --dump')

        self.args = args

    def getArgs(self):
        '''Get Arguments'''
        return self.args
