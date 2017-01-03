
# coding: utf-8

# In[1]:

#%reload_ext autoreload
#%autoreload 2
from algae_app.models import *
from django.db.models import Q, Sum, Count
import pandas as pd
from django.utils import timezone
from django.core.files import File
import cv2
import uuid
import numpy as np
import os


# In[2]:

APP_NAME="algae_app"
ROOT_PATH=os.path.abspath(".")

##clear migrations and database
import fnmatch
cd=ROOT_PATH
print "cd %s"%cd
for f in os.listdir(cd):
    if fnmatch.fnmatch(f, '*.sqlite3'):
        print "removing %s"%(os.path.join(ROOT_PATH,f))
        os.remove(os.path.join(cd,f))

cd=os.path.join(ROOT_PATH,APP_NAME,"migrations")
print "cd %s"%cd
for f in os.listdir(cd):
    if fnmatch.fnmatch(f, '*.pyc'):
        print "removing %s"%(os.path.join(cd,f))
        os.remove(os.path.join(cd,f))
    elif fnmatch.fnmatch(f, '0*.py'):
        print "removing %s"%(os.path.join(cd,f))
        os.remove(os.path.join(cd,f))

import sys
import subprocess
manage = os.path.join(ROOT_PATH , "manage.py")
print subprocess.check_output([sys.executable, manage, "makemigrations","--noinput"])
print subprocess.check_output([sys.executable, manage, "migrate","--noinput"])


# In[3]:

from django.contrib.auth.models import User
if User.objects.filter(username='admin').exists():
    print "[admin] is already in User Table"
    admin=User.objects.get(username='admin')
else:
    print "creating [admin] in User Table"
    admin=User.objects.create_user('admin', password='qwer1234')
    admin.is_superuser=True
    admin.is_staff=True
    admin.save()


# In[ ]:



