import os
import subprocess
import sys


__version__ = '0.0.1'
__author__ = 'Jeroen Seegers'
__license__ = 'MIT'


HOME_DIR = os.path.expanduser('~')
HISTORY_FILE = HOME_DIR + '/.git-history.log'


def ensure_history_file():
    """Ensure the history file exists"""
    if not os.path.isfile(HISTORY_FILE) and os.access(HOME_DIR, os.W_OK):
        open(HISTORY_FILE, 'a').close()
        return True
    elif os.path.isfile(HISTORY_FILE) and os.access(HOME_DIR, os.W_OK):
        return True
    elif os.path.isfile(HISTORY_FILE) and not os.access(HOME_DIR, os.W_OK):
        return False
    else:
        return False


def track_history():
    arguments = sys.argv[1:]
    arguments.insert(0, 'git')

    if arguments == ['git', 'history']:
        # Show the history so far
        with open(HISTORY_FILE, 'r') as f:
            print f.read()
            f.close()
    elif len(arguments) > 1:
        # Store command in history
        if ensure_history_file():
            with open(HISTORY_FILE, 'a') as f:
                f.write('{0}\n'.format(' '.join(sys.argv[1:])))
                f.close()

        # Execute given command
        subprocess.call(arguments)
    else:
        # Show default help text
        subprocess.call('git')


if __name__ == '__main__':
    track_history()
