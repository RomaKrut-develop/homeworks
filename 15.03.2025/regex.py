import re
from datetime import datetime


class LogEntry:
    def __init__(self, line):
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*?)\] "(.*?) (.*?)" (\d{3}) (\d+)'
        match = re.match(pattern, line)
        if match:
            self.ip = match.group(1)
            self.datetime = datetime.strptime(match.group(2), '%d/%b/%Y:%H:%M:%S %z')
            self.method = match.group(3)
            self.url = match.group(4)
            self.status_code = int(match.group(5))
            self.response_size = int(match.group(6))
        else:
            raise ValueError(f'Invalid log entry format: {line}')

    def __str__(self):
        return f'{self.ip} - {self.datetime.strftime("%Y-%m-%d %H:%M:%S")} - {self.method} {self.url} - {self.status_code} - {self.response_size} bytes'

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_entries = []
        self.log_file = log_file

    def load_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    try:
                        log_entry = LogEntry(line.strip())
                        self.log_entries.append(log_entry)
                    except ValueError as e:
                        print(f'Error parsing log entry: {e}')
        except FileNotFoundError:
            print(f'Error: {self.log_file} not found.')

    def get_ip_stats(self):
        ip_stats = {}
        for entry in self.log_entries:
            if entry.ip in ip_stats:
                ip_stats[entry.ip] += 1
            else:
                ip_stats[entry.ip] = 1
        return ip_stats

    def most_requested_url(self):
        url_stats = {}
        for entry in self.log_entries:
            if entry.url in url_stats:
                url_stats[entry.url] += 1
            else:
                url_stats[entry.url] = 1
        return max(url_stats, key=url_stats.get)

log_analyzer = LogAnalyzer('access.log')
log_analyzer.load_logs()

print(f'Total: {len(log_analyzer.log_entries)}')
print('IP:')
for ip, count in log_analyzer.get_ip_stats().items():
    print(f'{ip}: {count} requests')
print(f'URL: {log_analyzer.most_requested_url()}')