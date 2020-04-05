import wpe04_solution
import operator

logfilename = 'mini-access-log.txt'


def test_dicts_returns_list_of_dicts():
    ld = wpe04_solution.LogDicts(logfilename)
    result = ld.dicts()
    assert type(result) == list
    assert all([type(one_item) == dict
                for one_item in result])


def test_iterdicts_returns_iterator_dicts():
    ld = wpe04_solution.LogDicts(logfilename)
    result = ld.iterdicts()
    assert iter(result) == result

    result_list = list(result)
    assert type(result_list) == list

    assert all([type(one_item) == dict
                for one_item in result])

def test_sort_by_ip_address():
    ld = wpe04_solution.LogDicts(logfilename)
    sorted_ld = ld.dicts(key=operator.itemgetter('ip_address'))

    assert sorted_ld[0]['ip_address'] <= sorted_ld[1]['ip_address']
    assert sorted_ld[0]['ip_address'] <= sorted_ld[-1]['ip_address']
    assert sorted_ld[-2]['ip_address'] <= sorted_ld[-1]['ip_address']

def test_sort_by_request():
    ld = wpe04_solution.LogDicts(logfilename)
    sorted_ld = ld.dicts(key=operator.itemgetter('request'))

    assert sorted_ld[0]['request'] <= sorted_ld[1]['request']
    assert sorted_ld[0]['request'] <= sorted_ld[-1]['request']
    assert sorted_ld[-2]['request'] <= sorted_ld[-1]['request']

def test_earliest():
    ld = wpe04_solution.LogDicts(logfilename)
    earliest = ld.earliest()

    sorted_ld = ld.dicts(key=operator.itemgetter('timestamp'))
    assert sorted_ld[0]['timestamp'] == earliest['timestamp']

def test_latest():
    ld = wpe04_solution.LogDicts(logfilename)
    latest = ld.latest()

    sorted_ld = ld.dicts(key=operator.itemgetter('timestamp'))
    assert sorted_ld[-1]['timestamp'] == latest['timestamp']

def test_for_ip():
    ld = wpe04_solution.LogDicts(logfilename)
    matching_requests = ld.for_ip("65.55.106.183")
    assert len(matching_requests) == 2
    assert all([one_item['ip_address'] == '65.55.106.183'
                for one_item in matching_requests])

def test_for_request():
    ld = wpe04_solution.LogDicts(logfilename)
    matching_requests = ld.for_request("/robots.txt")
    assert len(matching_requests) == 16
    assert all(['/robots.txt' in one_item['request']
                for one_item in matching_requests])