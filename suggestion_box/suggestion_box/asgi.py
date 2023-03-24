"""
ASGI config for suggestion_box project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import pathlib
import dotenv

from django.core.asgi import get_asgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent 
ENV_FILE_PATH = BASE_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suggestion_box.settings')

application = get_asgi_application()
