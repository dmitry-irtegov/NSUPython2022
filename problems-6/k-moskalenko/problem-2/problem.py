import re

_pct_encoded = r'(?:%[a-fA-F\d]{2})'  # RFC3986 (Section 2.1)
_sub_delims = r'(?:[!$&\'()*+,;=])'  # RFC3986 (Section 2.2)
_unreserved = r'(?:[a-zA-Z\d\-._~])'  # RFC3986 (Section 2.3)

_scheme = r'(?:[a-zA-Z][a-zA-Z\d+-.]*://)'  # RFC3986 (Section 3.1)
_userinfo = rf'(?:(?:{_unreserved}|{_pct_encoded}|{_sub_delims}|:)*@)?'  # RFC3986 (Section 3.2.1)

# RFC3986 (Section 3.2.2) + RFC1034 (Section 3.5)
_ip = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}'
_label = r'(?:[a-zA-Z](?:[a-zA-Z\d-]*[a-zA-Z\d])?)'
_host = rf'(?:{_label}(?:\.{_label})*\.?)'

_port = r'(?::\d*)?'  # RFC3986 (Section 3.2.3)

# RFC3986 (Section 3.3)
_pchar = rf'(?:{_unreserved}|{_pct_encoded}|{_sub_delims}|[:@])'
_path_abempty = rf'(?:/{_pchar}*)*'
_path_absolute = rf'(?:/(?:{_pchar}+{_path_abempty})?)'
_path = rf'(?:{_path_abempty}|{_path_absolute})'

_querystr = rf'(?:\?(?:{_pchar}|[/?])*)?'  # RFC3986 (Section 3.4)
_fragment = rf'(?:\#(?:{_pchar}|[/?])*)?'  # RFC3986 (Section 3.5)

url_regex = rf'(?:{_scheme}|www\.){_userinfo}(?:{_ip}|{_host}){_port}{_path}{_querystr}{_fragment}'


def extract_urls(string):
    return re.findall(url_regex, string, flags=re.IGNORECASE)
