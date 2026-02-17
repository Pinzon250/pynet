from pynet.cli import app
from pynet.core.templates import list_templates

if __name__ == "__main__":
    base = list_templates()
    
    print(base)
