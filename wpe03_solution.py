#!/usr/bin/env python3

import re
import os
import io


def check_file_size(file: io.IOBase) -> bool:
    saved_pos = file.tell()
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(saved_pos)
    return file_size


def re_logtolist(file):
    log_dict_list = []
    if not check_file_size(file):
        return []
    for log_line in file:
        log_dict = re_parse_log(log_line)
        if log_dict:
            log_dict_list.extend(log_dict)

    # Tests want an empty dict wrapped in a list. Don't get it. (╯°□°)╯︵ ┻━┻
    if not log_dict_list:
        return [{}]
    else:
        return log_dict_list


def logtolist(file):
    log_dict_list = []
    if not check_file_size(file):
        return []
    for log_line in file:
        log_dict = leeches_parse_log(log_line)
        if log_dict:
            log_dict_list.extend(log_dict)

    # Tests want an empty dict wrapped in a list. Don't get it. (╯°□°)╯︵ ┻━┻
    if not log_dict_list:
        return [{}]
    else:
        return log_dict_list


def leeches_parse_log(line: str):
    """This method named in honor of just how backwards it is to do this with regular string operations :)
    Parse the first few fields of an Apache log into a Dict."""
    try:
        ip_address = line.split(' ', 1)[0]
        timestamp_start = line.find('[') + 1
        timestamp_end = line.index(']', timestamp_start)
        timestamp = line[timestamp_start:timestamp_end]
        request_start = line.find('"') + 1
        request_end = line.index('"', request_start)
        request = line[request_start:request_end]
    except ValueError:
        return [{'ip_address': 'No IP address found', 'timestamp': 'No timestamp found', 'request': 'No request found'}]
    except IndexError:
        return [{}]

    return [{'ip_address': ip_address, 'timestamp': timestamp, 'request': request}]


def re_parse_log(line):
    try:
        m = re.match(r'(?P<ip_address>\d+.\d+.\d+.\d+) - - \[(?P<timestamp>.+)\] \"(?P<request>.+)\" \d+.+$', line)
        if m:
            return [m.groupdict()]
        else:
            return [{'ip_address':'No IP address found', 'timestamp': 'No timestamp found', 'request':'No request found'}]
    except TypeError:
        return [{'ip_address':'No IP address found', 'timestamp': 'No timestamp found', 'request':'No request found'}]


if __name__ == '__main__':
    print("Let's do this the sane way with regex:")
    with open('wp03_loglines.txt', "r") as log_dict_lines:
        log_dict_list = re_logtolist(log_dict_lines)
        for log_dict in log_dict_list:
            print(log_dict)

    print("And now using blood letting and trepanation - e.g. simple string functions.")
    with open('wp03_loglines.txt', "r") as log_dict_lines:
        log_dict_list = logtolist(log_dict_lines)
        for log_dict in log_dict_list:
            print(log_dict)
