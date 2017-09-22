import yaml

def filetypesParser(ftpath):
    with open(ftpath, 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)