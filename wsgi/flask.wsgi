import os
import sys

##Virtualenv Settings
activate_this = '/usr/share/drinkmixer/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

##Replace the standard out
#sys.stdout = sys_stderr

##Add this file path to sys.path in order to import settings
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
sys.path.insert(0, '/usr/share/drinkmixer/wsgi/flask.wsgi')

##Add this file path to sys.path in order to import app
sys.path.append('/usr/share/drinkmixer/')

##Create application for the app 
from app import app as application
