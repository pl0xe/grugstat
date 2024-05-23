import os.path
from datetime import datetime

class Log():

    log_path = None

    valid_tags = {
        'info': '[-]',
        'error': '[!]',
        'success': '[+]',
    }

    def __init__(self, log_path='./log', verbose=False):

        # path to where file is saved
        self.log_path = log_path

        # print log messages to console
        self.verbose = verbose

        # check if log file exists if not create one
        if not os.path.isfile(self.log_path):
            self.create_log()

    def log_tagger(self, log_tag):

        '''Tags all log messages with a prefix to help identify certain messages'''

        # verify tag exists
        if log_tag not in self.valid_tags.keys():
            if self.verbose:
                print(f'{self.valid_tags['error']} Invalid tag used for logging message.')
            return None
        
        return self.valid_tags[log_tag]


    def create_log(self):

        '''Creates the initial file for the log if it does not exist'''

        if self.verbose:
            print(f'{self.valid_tags['info']} Creating log file.')

        with open(self.log_path, 'w') as f:
            f.write(f'Log created on {datetime.now()}')

        if self.verbose:
            print(f'{self.valid_tags['success']} Creating log file.')

    def log(self, msg, log_tag='info'):
        
        '''Writes to the log file'''

        tag = self.log_tagger(log_tag)

        if not tag:
            print(f'{self.valid_tags['error']} Invalid tags not logging message : {msg}')
            return None

        time = datetime.now()

        message = f'[{time}] : {tag} {msg}\n'

        if self.verbose:
            print(message)

        with open(self.log_path, 'w') as f:
            f.write(message)