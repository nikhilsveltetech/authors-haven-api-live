from .base import *
from .base import env

DEBUG=True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-ad)gp!u!xh8m^=0w+s0uk#hqx!@udpci**2!gvw1pzuh&)9007")

ALLOWED_HOSTS = ['localhost', '0.0.0.0','127.0.0.1']