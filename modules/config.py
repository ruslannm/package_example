import os
import configparser
from pathlib import Path

def get_data(section='server'):
    parent_dir = Path(__file__).parent.parent
    config_path  = os.path.join(parent_dir, 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)
    return {k : v for k, v in config[section].items()}


if __name__ == '__main__':
    print(get_data())