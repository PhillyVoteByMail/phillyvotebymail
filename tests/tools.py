import os

CURR_FILE_DIR = os.path.dirname(os.path.realpath(__file__))

def fixture_path(*args):
    return os.path.join(CURR_FILE_DIR, 'fixtures', *args)
