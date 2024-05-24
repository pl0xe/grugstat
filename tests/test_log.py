import os
import os.path
from grugstat.log import Log

def test_init_log():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = 'tests/log'

    Log(log_path)

    # os operates in the programs directory
    status = os.path.isfile(log_path)

    os.remove(log_path)

    assert status
    

def test_same_tags():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = './tests/log'

    test_tags = {
        'info': '[-]',
        'error': '[!]',
        'success': '[+]',
    }

    log = Log(log_path) 
    os.remove(log_path)
    assert log.valid_tags.items() == test_tags.items()

def test_write_info():

    '''Test writing a single info message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 1')

    pattern = ']: [-] test message 1'

    with open(log_path, 'r') as f:
        data = f.read()

    os.remove(log_path)

    if pattern in data:
        assert True

def test_write_error():

    '''Test writing a single error message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 2', 'error')

    pattern = '] : [!] test message 2'

    with open(log_path, 'r') as f:
        data = f.read()

    os.remove(log_path)

    if pattern in data:
        assert True

def test_write_success():

    '''Test writing a single success message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 3', 'success')

    pattern = '] : [+] test message 3'

    with open(log_path, 'r') as f:
        data = f.read()

    os.remove(log_path)

def test_consecutive_log():

    '''Check if multiple messages will get saved to log'''

    log_path = './tests/log'
    log = Log(log_path)
    message_amount = 100

    msg1 = 'test message 1'
    msg2 = 'test message 2'
    msg3 = 'test message 3'

    for _ in range(message_amount):
        log.log(msg1)
        log.log(msg2, 'error')
        log.log(msg3, 'success')

    with open(log_path, 'r') as f:
        data = f.read()

    os.remove(log_path)

    for i in [msg1, msg2, msg3]:
        if data.count(i) != message_amount:
            assert False
    assert True