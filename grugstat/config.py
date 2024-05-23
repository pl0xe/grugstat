import os.path

class Config():

    def __init__(self, config_path='./config'):
        self.config_path = config_path

    def get_config(self):

        '''Initialized the config file, if it does not exist
        create a default config'''

        if not os.path.isfile(self.config_path):
            self.create_default_config()
        
    def create_default_config(self):

        '''Creates a default config for the bot'''

        print('[!] Creating default config.')
        token_key = input('[>] insert token :')

        if token_key == None:
            print('[-]')

        config = {
            'token_key': ''
        }
        
        pass