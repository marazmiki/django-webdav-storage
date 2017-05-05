Examples
========

Add WebDAV support to nginx
---------------------------

.. code:: nginx

    # Public readonly media server.
    server {
        listen 80;
        charset        utf-8;
        server_tokens  off;
        server_name    media.example.com;

        access_log     /var/log/nginx/media_access.log;
        error_log      /var/log/nginx/media_error.log;

        root           /usr/share/nginx/webdav;

    }

    # WebDAV server
    server {
        listen 80;
        charset        utf-8;
        server_tokens  off;
        server_name    webdav.example.com;

        access_log     /var/log/nginx/webdav_access.log;
        error_log      /var/log/nginx/webdav_error.log;

        root           /usr/share/nginx/webdav;

        client_max_body_size    10m;
        client_body_temp_path   /tmp;
        create_full_put_path    on;
        autoindex               on;

        dav_methods             PUT DELETE MKCOL COPY MOVE;
        dav_access              user:rw   group:r   all:r;

        satisfy                 any;

        allow                   127.0.0.1/32;
        deny                    all;

        auth_basic              'My WebDAV area';
        auth_basic_user_file    /usr/share/nginx/.htpasswd;
    }

