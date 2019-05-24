import sys
from configparser import ConfigParser
from pathlib import Path


def config() -> ConfigParser:
    """
    Get secrets, or fail if hte file doesn't exist.

    By default, ConfigParser fails silently if it cannot find the file. We don't
    want this behaviour as we only have one file for secrets, and so if it
    doesn't exist, there's not logical behaviour.
    """
    secrets_file = Path('secrets.ini')

    if not secrets_file.exists():
        print('ERROR: `secrets.ini` not defined\n'
              'Use `secrets.example.ini` as a reference to set up API keys')
        sys.exit(1)

    configuration = ConfigParser()
    configuration.read(secrets_file)

    return configuration
