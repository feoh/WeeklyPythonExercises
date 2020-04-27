#!/usr/bin/env python3

import re
from time import strptime

class LogDicts:
    def re_logtolist(self, lines):
        log_lines = lines
        log_dict_list = []
        for log_line in log_lines:
            log_dict = self.re_parse_log(log_line)
            if log_dict:
                log_dict_list.extend(log_dict)

        # Tests want an empty dict wrapped in a list. Don't get it. (╯°□°)╯︵ ┻━┻
        if not log_dict_list:
            return [{}]
        else:
            return log_dict_list

    def re_parse_log(self, line):
        try:
            m = re.match(r'(?P<ip_address>\d+.\d+.\d+.\d+) - - \[(?P<timestamp>.+)\] \"(?P<request>.+)\" \d+.+$', line)
            if m:
                parsed_dict = m.groupdict()
                ts = parsed_dict['timestamp']
                timeobject = strptime(ts, "%d/%b/%Y:%H:%M:%S %z")
                parsed_dict['timestamp'] = timeobject
                return [parsed_dict]
            else:
                return [{'ip_address': 'No IP address found', 'timestamp': 'No timestamp found',
                         'request': 'No request found'}]
        except TypeError:
            return [
                {'ip_address': 'No IP address found', 'timestamp': 'No timestamp found', 'request': 'No request found'}]

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as log_dict_lines:
            self.log_dict_list = self.re_logtolist(log_dict_lines)

    def dicts(self, key=None):
        if key:
            sorted_logdicts = sorted(self.log_dict_list, key=key)
            return sorted_logdicts
        else:
            return self.log_dict_list

    def iterdicts(self, key=None):
        if key:
            for d in sorted(self.log_dict_list, key=key):
                yield d
        else:
            for d in self.log_dict_list:
                yield d

    def earliest(self):
        if self.log_dict_list:
            return self.log_dict_list[0]
        else:
            return None

    def latest(self):
        if self.log_dict_list:
            return self.log_dict_list[-1]
        else:
            return None

    def for_ip(self, ip_address):
        return [dict for dict in self.log_dict_list if dict['ip_address'] == ip_address]

    def for_request(self, request):
        matches = [dict for dict in self.log_dict_list if request in dict['request']]
        return matches
