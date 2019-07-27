import re

NGINX_AUTOINDEX_RE = re.compile(r'\<a href="([^"]+)"\>')


def nginx_autoindex(storage, path):
    directories, files = [], []

    response = storage.webdav('GET', path)

    for link in NGINX_AUTOINDEX_RE.findall(response.content.decode('utf-8')):
        if link == '../':
            continue

        if link.endswith('/'):
            directories.append(link[:-1])
        else:
            files.append(link)

    return directories, files
