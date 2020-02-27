import re
import sys

if not re.match(r'^[_a-z][_a-z0-9]*$', '{{ cookiecutter.package_name }}'):
    print('Package names may only start with a lowercase letter or underscore '
          'and may only consist of lowercase letters, numbers and underscores')
    sys.exit(1)
