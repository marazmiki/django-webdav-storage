from multiprocessing import freeze_support
from django.core.management import BaseCommand, CommandError
from django.conf import settings


try:
    from wsgidav.server import run_server
except ImportError:
    run_server = None


class Command(BaseCommand):
    help = (
        'Starts a lightweight WebDAV server for development purposes'
    )

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?',
                            default=8080,
                            help='Optional port number, or ipaddr:port')

    def configure(self, opts):
        root = getattr(settings, 'WEBDAV_WSGIDAV_ROOT', None)
        port_config = getattr(settings, 'WEBDAV_WSGIDAV_PORT', 8080)
        port_args = opts['addrport']

        if not root:
            raise CommandError(
                'You should specify the WEBDAV_WSGIDAV_ROOT in your '
                'settings module'
            )

        config = run_server.DEFAULT_CONFIG.copy()
        config.update({
            'verbose': opts['verbosity'],
            'server': 'wsgiref',
            'provider_mapping': {
                '/': run_server.FilesystemProvider(root)
            },
        })

        if not port_args and not port_config:
            raise CommandError(
                'You should specify the WEBDAV_WSGIDAV_PORT in your '
                'settings module or pass the port or addr:port in the '
                'command line'
            )

        if port_args:
            if isinstance(port_args, int):
                config['port'] = port_args
            else:
                bits = port_args.rsplit(':', 1)
                if len(bits) == 1:
                    config['port'] = bits[0]
                else:
                    config['host'] = bits[0]
                    config['port'] = bits[1]

        config.setdefault('host', '127.0.0.1')

        return config

    def handle(self, *args, **options):
        if run_server is None:
            raise CommandError(
                'To use this command, you should install WsgiDAV first with'
                'typing\n\n  pip install wsgidav\n\n'
                'in your console.'
            )

        config = self.configure(options)
        app = run_server.WsgiDAVApp(config)
        server = config['server']
        freeze_support()
        run_server._runWsgiref(app, config, server)
