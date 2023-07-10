from .settings import *

####################################################################################
# Allow Wing Pro to stop on exceptions and debug templates, when it is present

import os

try:
    from . import wing_debug_support

    del wing_debug_support
except ImportError:
    if "WINGDB_ACTIVE" in os.environ:
        print("Failed to import debugger support for Wing Pro")

if "WINGDB_ACTIVE" in os.environ:
    DEBUG = True
    try:
        TEMPLATES[0]["OPTIONS"]["debug"] = True
    except Exception:
        TEMPLATE_DEBUG = True

######################################################################################
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

#####################################################################################
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
