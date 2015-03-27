import os
import sys

import django
import django.conf


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'django_permanent',
        'django_permanent.tests.test_app',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    },
    MIDDLEWARE_CLASSES=[]
)


def runtests(*test_args):
    if not django.conf.settings.configured:
        django.conf.settings.configure(**DEFAULT_SETTINGS)
    if hasattr(django, 'setup'):
        django.setup()
    if not test_args:
        test_args = ['django_permanent']

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)
    from django.test.simple import DjangoTestSuiteRunner
    failures = DjangoTestSuiteRunner(verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
