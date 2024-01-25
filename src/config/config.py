""" config file for repo structure """
# base
import yaml
import os
import logging


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


class YamlLoader:
    """
    load the config yaml files

    Returns:
        a dict with the file configs
    """
    def __init__(self, version: str = None):
        self.version = version

    def prompts(self):
        """
        :returns the full prompt for the version given
        """
        root_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(root_dir, "prompts.yaml")) as stream:
            try:
                prompts = yaml.safe_load(stream)
                for prompt in prompts['general']['versions']:
                    if prompt["version_id"] == self.version:
                        prompt_config = prompt
                if prompt_config is not None:
                    return prompt_config
                else:
                    logging.info(f"The prompt version {self.version} do not exits!!")
            except yaml.YAMLError as exc:
                print(exc)
                logging.error(f"Error generating LLM response: {exc}")
