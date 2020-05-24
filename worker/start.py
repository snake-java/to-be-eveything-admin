import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from publick.load import LoadYaml

if __name__ == "__main__":
    config = LoadYaml(os.path.dirname(__file__),'worker.yaml')
    