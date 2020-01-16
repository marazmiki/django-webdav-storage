import re


NGINX_AUTOINDEX_RE = re.compile(b'\<a href="([^"]+)"\>')  # noqa:W605
WSGIDAV_AUTOINDEX_RE = re.compile(
    b'<tr><td><a href="([^"]+)" class="">(.*?)</a></td>\s+<td>(.*?)</td>'  # noqa:W605
)


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

        if path.endswith(b'/') or type == b'Directory':
            directories.append(name)
        else:
            files.append(name)

    return directories, files
