from ._utils import *

@task
def test():
    settings = {
        'INSTALLED_APPS': (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'armstrong.core.arm_content',
            'armstrong.core.arm_content.tests.arm_content_support',
        ),
        'ROOT_URLCONF': 'armstrong.core.arm_content.tests.arm_content_support.urls',
        'AUTH_PROFILE_MODULE': 'arm_content_support.UserProfile',
    }
    run_tests(settings, 'arm_content_support', 'arm_content')

