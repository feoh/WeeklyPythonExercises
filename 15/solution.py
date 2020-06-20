from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from queue import Queue
from urllib import request
from time import perf_counter
from collections import defaultdict
from statistics import mean
from pprint import pprint



URLS = ['http://www.youtube.com',
        'http://www.facebook.com',
        'http://www.baidu.com',
        'http://www.yahoo.com',
        'http://www.wikipedia.org']


def queue_url_read(url: str, q: Queue):
    start = perf_counter()
    with request.urlopen(url) as conn:
        _=conn.read()
    end = perf_counter()
    elapsed = end - start
    result_tuple = (url, elapsed)
    q.put(result_tuple)



def speed_test(*args, number_of_checks=10):
    q = Queue()
    # I can't see a way to pass number_of_checks into the threadpool 'with' context.
    # So we cheat, 'cause it's a queue, right? :)
    futures = []
    for _ in range(number_of_checks):
        with ThreadPoolExecutor() as executor:
            futures.extend([executor.submit(queue_url_read, url, q) for url in args[0]])

    # Wait until everybody finishes!
    [f.result() for f in futures]
    raw_timings = defaultdict(list)
    for timing in q.queue:
        url = timing[0]
        elapsed = timing[1]
        raw_timings[url].append(elapsed)

    mean_timings = {url:mean(raw_timings[url]) for url in raw_timings.keys()}
    pprint(mean_timings)



if __name__ == '__main__':
    speed_test(URLS, 10)
