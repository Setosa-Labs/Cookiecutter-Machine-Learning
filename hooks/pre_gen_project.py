import re
import sys


def script_main():
    if not re.match(r'^[_a-z][_a-z0-9]*$', '{{ cookiecutter.package_name }}'):
        print('Packages may only start with a lowercase letter or underscore',
              'and may only consist of lowercase letters, numbers and', 
              'underscores')
        sys.exit(1)


if __name__ == '__main__':
    script_main()
