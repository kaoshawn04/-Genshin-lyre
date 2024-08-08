import configparser


config = configparser.ConfigParser()
config.read("config/config.ini", encoding = "utf-8")

def get_config(*args):
    return [config["settings"][arg] for arg in args]