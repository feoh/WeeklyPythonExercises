#!/usr/bin/env python3

import pytest
from wpe03_solution import logtolist, re_logtolist
from io import StringIO

@pytest.fixture
def mini_mini_file():
    return StringIO('''67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"
66.249.71.65 - - [30/Jan/2010:00:12:06 +0200] "GET /browse/one_node/1557 HTTP/1.1" 200 39208 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
65.55.106.183 - - [30/Jan/2010:01:29:23 +0200] "GET /robots.txt HTTP/1.1" 200 99 "-" "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
65.55.106.183 - - [30/Jan/2010:01:30:06 +0200] "GET /browse/one_model/2162 HTTP/1.1" 200 2181 "-" "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
66.249.71.65 - - [30/Jan/2010:02:07:14 +0200] "GET /browse/browse_applet_tab/2593 HTTP/1.1" 200 10305 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.71.65 - - [30/Jan/2010:02:10:39 +0200] "GET /browse/browse_files_tab/2499?tab=true HTTP/1.1" 200 446 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:13:34 +0200] "GET /robots.txt HTTP/1.1" 200 99 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:13:34 +0200] "GET /browse/one_node/2715 HTTP/1.1" 200 26433 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:43:39 +0200] "GET /browse/download_model/1969 HTTP/1.1" 200 31713 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:04:05:43 +0200] "GET /browse/one_node/1406 HTTP/1.1" 302 118 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
''')

def test_read_empty_file(mini_mini_file):
    log_list = logtolist(StringIO(''))
    assert len(log_list) == 0
    assert log_list == []

def test_read_empty_line(mini_mini_file):
    log_list = logtolist(StringIO('\n'))
    assert len(log_list) == 1

def test_read_logs(mini_mini_file):
    log_list = logtolist(mini_mini_file)
    assert len(log_list) == 10

def test_got_a_list(mini_mini_file):
    log_list = logtolist(mini_mini_file)
    assert type(log_list) is list

def test_all_are_dicts(mini_mini_file):
    log_list = logtolist(mini_mini_file)
    assert all([type(x) is dict
                for x in log_list])

def test_check_keys(mini_mini_file):
    log_list = logtolist(mini_mini_file)
    assert set(log_list[0].keys()) == {'ip_address', 'timestamp', 'request'}

def test_check_values(mini_mini_file):
    log_list = logtolist(mini_mini_file)
    first_log_dict = log_list[0]

    assert first_log_dict['ip_address'] == '67.218.116.165'
    assert first_log_dict['timestamp'] == '30/Jan/2010:00:03:18 +0200'
    assert first_log_dict['request'] == 'GET /robots.txt HTTP/1.0'

# Below here are regexp tests, for the function re_logtolist
# Don't feel obligated to implement this if regular expressions are hard for you!
# But if you know and like them, then go for it!

def test_re_read_empty_file(mini_mini_file):
    log_list = logtolist(StringIO(''))
    assert len(log_list) == 0
    assert log_list == []

def test_re_read_empty_line(mini_mini_file):
    log_list = re_logtolist(StringIO('\n'))
    assert len(log_list) == 1

def test_re_read_bad_line(mini_mini_file):
    log_list = re_logtolist(StringIO('abc def ghi\n'))
    assert len(log_list) == 1

    first_log_dict = log_list[0]
    assert first_log_dict['ip_address'] == 'No IP address found'
    assert first_log_dict['timestamp'] == 'No timestamp found'
    assert first_log_dict['request'] == 'No request found'

def test_re_read_logs(mini_mini_file):
    log_list = re_logtolist(mini_mini_file)
    assert len(log_list) == 10

def test_re_got_a_list(mini_mini_file):
    log_list = re_logtolist(mini_mini_file)
    assert type(log_list) is list

def test_re_all_are_dicts(mini_mini_file):
    log_list = re_logtolist(mini_mini_file)
    assert all([type(x) is dict
                for x in log_list])

def test_re_check_keys(mini_mini_file):
    log_list = re_logtolist(mini_mini_file)
    assert set(log_list[0].keys()) == {'ip_address', 'timestamp', 'request'}

def test_re_check_values(mini_mini_file):
    log_list = re_logtolist(mini_mini_file)
    first_log_dict = log_list[0]

    assert first_log_dict['ip_address'] == '67.218.116.165'
    assert first_log_dict['timestamp'] == '30/Jan/2010:00:03:18 +0200'
    assert first_log_dict['request'] == 'GET /robots.txt HTTP/1.0'