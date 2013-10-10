#!/usr/bin/env python
import os
import sys

# Edit this if necessary or override the variable in your environment.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solitude.settings')

try:
    # For local development in a virtualenv:
    from funfactory import manage
except ImportError:
    # Production:
    # Add a temporary path so that we can import the funfactory
    tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'vendor', 'src', 'funfactory')
    sys.path.append(tmp_path)

    from funfactory import manage

    # Let the path magic happen in setup_environ() !
    sys.path.remove(tmp_path)


manage.setup_environ(__file__, more_pythonic=True)

# This constant moved in Django 1.5 but it is used by Tastypie. When that
# gets updated we can remove this.
from django.db.models.sql import constants
try:
    from django.db.models.constants import LOOKUP_SEP
    constants.LOOKUP_SEP = LOOKUP_SEP
except ImportError:
    pass

# Tastypie pulls in simplejson from Django if it can. But simplejson is now
# incompatible with the std lib json. So its removed from our requirements.
# However Jenkins has simplejson installed globally, meaning it gets pulled in
# and fails.
import json
try:
    from django import utils
    utils.simplejson = json
except ImportError:
    pass

# Get all the funfactory logging goodness.
from funfactory import log_settings  # NOQA

if __name__ == "__main__":
    manage.main()
