#!/usr/bin/env python3

import re


def logtolist(filename):
    log_dict_list = []
    with open(filename,"r") as logfile:
        for log_line in logfile:
            log_dict = re_logtolist(log_line)
            if log_dict:
                log_dict_list.append(log_dict)
    return log_dict_list


def re_logtolist(line):
    m = re.match(r'(?P<ip_address>\d+.\d+.\d+.\d+).+-.+-.+\[(?P<timestamp>.+)\].+\"(?P<request>GET.+)\"', line)
    if m:
        return m.groupdict()
    else:
        return None

if __name__ == '__main__':
    log_dict_list = logtolist("wp03_loglines.txt")
    for log_dict in log_dict_list:
        print(log_dict)
