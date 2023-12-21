""" config file for repo structure """
# base
import yaml
import os


def load_config():
    """
    load the config from the file 'config.yaml'.

    Returns:
        a dict with the app config
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_dir, "config.yaml")) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)