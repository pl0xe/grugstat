import os
import os.path
import hashlib
from grugstat.log import Log

def test_init_log():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name, verbose=True)

    print(log.abs_path)

    # os operates in the programs directory
    status = os.path.isfile(log_path + name)

    os.remove(log.abs_path)

    assert status
    

def test_same_tags():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = 'tests/'
    name = 'log'

    test_tags = {
        'info': '[-]',
        'error': '[!]',
        'success': '[+]',
    }

    log = Log(path=log_path, name=name) 
    os.remove(log.abs_path)
    assert log.valid_tags.items() == test_tags.items()

def test_write_info():

    '''Test writing a single info message into a log file'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name)
    log.log('test message 1')

    pattern = ']: [-] test message 1'

    with open(log_path + name, 'r') as f:
        data = f.read()

    os.remove(log.abs_path)

    if pattern in data:
        assert True

def test_write_error():

    '''Test writing a single error message into a log file'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name)
    log.log('test message 2', 'error')

    pattern = '] : [!] test message 2'

    with open(log_path + name, 'r') as f:
        data = f.read()

    os.remove(log_path + name)

    if pattern in data:
        assert True

def test_write_success():

    '''Test writing a single success message into a log file'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name)
    log.log('test message 3', 'success')

    pattern = '] : [+] test message 3'

    with open(log_path + name, 'r') as f:
        data = f.read()

    os.remove(log_path + name)

def test_consecutive_log():

    '''Check if multiple messages will get saved to log'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name)
    message_amount = 100

    msg1 = 'test message 1'
    msg2 = 'test message 2'
    msg3 = 'test message 3'

    for _ in range(message_amount):
        log.log(msg1)
        log.log(msg2, 'error')
        log.log(msg3, 'success')

    with open(log_path + name, 'r') as f:
        data = f.read()

    os.remove(log_path + name)

    for i in [msg1, msg2, msg3]:
        if data.count(i) != message_amount:
            assert False
    assert True

def test_log_overwrite():

    '''Test to ensure initiating another log will not overwrite a previously made log'''

    log_path = 'tests/'
    name = 'log'

    log = Log(log_path, name=name)
    log.log('foo')
    log.log('bar')

    with open(log_path + name, 'rb') as f:
        data = f.read()

    original_md5 = hashlib.md5(data).hexdigest()
    log = Log(log_path)

    with open(log_path + name, 'rb') as f:
        data = f.read()

    test_md5 = hashlib.md5(data).hexdigest()

    assert original_md5 == test_md5

    os.remove(log_path + name)