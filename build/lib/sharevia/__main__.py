print('Hi ')

# Importing required module
import subprocess
 
# Using system() method to
# execute shell commands
import pathlib
paths=str(pathlib.Path(__file__).parent.resolve())
#commands=''''''
#subprocess.Popen('echo cd '+paths +'\n uvicorn main:app', shell=True)
subprocess.Popen('uvicorn main:app --host 0.0.0.0 --port 8000', shell=True,cwd=paths)