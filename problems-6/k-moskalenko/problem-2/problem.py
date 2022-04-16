import re

_protocol = r'(?:https?://)'
_auth = r'(?:\S+(?::\S*)?@)?'
_ip = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}'
_host = r'(?:(?:[a-z\u00a1-\uffff0-9][-_]*)*[a-z\u00a1-\uffff0-9]+)'
_domain = r'(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*'
_tld = r'(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?'
_port = r'(?::\d{2,5})?'
_path = r'(?:[/?#][^\s"]*)?'

url_regex = rf'(?:{_protocol}|www\.){_auth}(?:localhost|{_ip}|{_host}{_domain}{_tld}){_port}{_path}'


def extract_urls(string):
    return re.findall(url_regex, string, flags=re.IGNORECASE)
