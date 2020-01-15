import re

from .compat import PY3

NGINX_AUTOINDEX_RE = re.compile(b'<a href="([^"]+)">')

WSGIDAV_REGEX = (
    r'<tr class=".*?">\s*?<td>\s*?'
    r'<a.*?href="(?P<path>[^"]+)".*?>\s*?(?P<name>[^\s]+)\s*?</a>\s*?'
    r'</td>\s*?<td>(?P<type>.*?)</td>'
)

if PY3:
    WSGIDAV_REGEX = WSGIDAV_REGEX.encode()

WSGIDAV_AUTOINDEX_RE = re.compile(WSGIDAV_REGEX)


def nginx_autoindex(storage, path):
    directories, files = [], []

    response = storage.webdav('GET', path)

    for link in NGINX_AUTOINDEX_RE.findall(response.content):
        if link == b'../':
            continue
        if link.endswith(b'/'):
            directories.append(link[:-1])
        else:
            files.append(link)

    return directories, files


def wsgidav_autoindex(storage, path):
    directories, files = [], []
    response = storage.webdav('GET', path)
    for row in WSGIDAV_AUTOINDEX_RE.findall(response.content):
        path, name, type = row
        if name == b'..':
            continue
        if path.endswith(b'/') or type == b'Directory':
            directories.append(name)
        else:
            files.append(name)
    return directories, files
