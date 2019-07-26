import re


NGINX_AUTOINDEX_RE = re.compile(r'\<a href="([^"]+)"\>')


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
