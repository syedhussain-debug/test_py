import configparser
import os

class ConfigReader:
    def __init__(self, file_path="application.properties"):
        self.config = configparser.ConfigParser()
        
        # ConfigParser requires sections, so we fake one
        with open(file_path) as f:
            file_content = "[DEFAULT]\n" + f.read()
        
        self.config.read_string(file_content)
    
    def read_config():
              config = {}
              props = os.path.join(os.path.dirname(__file__), "application.properties")
              with open(props) as f:
                  for line in f:
                      line = line.strip()
                      if "=" in line and not line.startswith("#"):
                          k, v = line.split("=", 1)
                          config[k.strip()] = v.strip()
              return config

    def get(self, key, fallback=None):
        return self.config["DEFAULT"].get(key, fallback)
