import os.path
from datetime import datetime
from pathlib import Path

class Log():

    valid_tags = {
        'info': '[-]',
        'error': '[!]',
        'success': '[+]',
    }

    def __init__(self, path='./log', verbose=False, name='app.log'):

        self.path = None
        self.name = None
        self.abs_path = None
        self.verbose = verbose

        # handles setting path, name and abs_path properly
        self.set_path(path, name)
        self.log_filename = name

        # check if log file exists if not create one
        if not os.path.exists(self.abs_path):
            self.create_log()

    def set_path(self, path, name):

        '''Ensures paths are valid for the creation of file'''
        self.path = os.path.abspath(path)
        self.name = name
        self.abs_path = os.path.join(self.path, self.name)

    def create_log(self):

        '''Creates the log file'''
        
        # Will create directories up to the designated path
        Path(self.path).mkdir(parents=True, exist_ok=True)
        self.log('Creating log')


    def log_tagger(self, log_tag):

        '''Tags all log messages with a prefix to help identify certain messages'''

        # verify tag exists
        if log_tag not in self.valid_tags.keys():
            if self.verbose:
                self.log('Invalid tag used for logging message.', log_tag='error')
            return None
        
        return self.valid_tags[log_tag]

    def log(self, msg, log_tag='info'):
        
        '''Writes to the log file'''

        tag = self.log_tagger(log_tag)

        if not tag:
            self.log(f'Invalid tags not logging message : {msg}', log_tag='error')
            return None

        time = datetime.now()

        message = f'[{time}] : {tag} {msg}\n'

        if self.verbose:
            print(message, end='')

        with open(self.abs_path, 'a') as f:
            f.write(message)