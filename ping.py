import subprocess
import platform
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
print(cred)
host = ['156.67.73.136','156.67.73.136','156.67.73.136',"163.45.3.2"]
siteResult = []
def ping():
     param = '-n' if platform.system().lower() == 'windows' else '-c'
     result = ''
     for x in host:
        command = ['ping', param, '1', x]
        y = subprocess.call(command)
        if (y==0):
            result = 'online'
        else: 
            result = 'offline'    
        siteResult.append((x,result))
     print(siteResult)    

