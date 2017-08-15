from .base import *
import os

DEBUG = False

ADMINS = (
	('Jay Tegge', 'jtegge095@gmail.com'),
)

ALLOWED_HOSTS = ['ourblog.com', 'www.ourblog.com']

DATABASES = {
	'default': {
	}
}

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '_6b$6+s569(txootxitm_p)=-!g=+spvc)5=ls9f6ld2j!mva^')

