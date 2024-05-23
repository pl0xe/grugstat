import re
import os
import os.path
from grugstat.log import Log

def test_init_log():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = './tests/log'

    Log(log_path)

    assert os.path.isfile(log_path)

    os.remove(log_path)

def test_same_tags():

    '''Verify tags that are being tested are the same in the Log class'''

    log_path = './tests/log'

    test_tags = {
        'info': '[-]',
        'error': '[!]',
        'success': '[+]',
    }
    
    assert Log(log_path).valid_tags.items() == test_tags.items()

    os.remove(log_path)

def test_write_info():

    '''Test writing a single info message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 1')

    pattern = re.compile(r'\[.{26}\] : \[-\] test message 1')

    with open(log_path, 'r') as f:
        data = f.read()

    matches = pattern.match(data)

    assert matches != None

    os.remove(log_path)

def test_write_error():

    '''Test writing a single error message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 2', 'error')

    pattern = re.compile(r'\[.{26}\] : \[!\] test message 2')

    with open(log_path, 'r') as f:
        data = f.read()

    matches = pattern.match(data)

    assert matches != None

    os.remove(log_path)

def test_write_success():

    '''Test writing a single success message into a log file'''

    log_path = './tests/log'
    log = Log(log_path)
    log.log('test message 3', 'success')

    pattern = re.compile(r'\[.{26}\] : \[\+\] test message 3')

    with open(log_path, 'r') as f:
        data = f.read()

    matches = pattern.search(data)

    assert matches != None

    os.remove(log_path)