import subprocess

#filename = 'subpr.py'
#p = subprocess.run(['ls', '-la', 'grep', filename], capture_output=True, text=True)

folder='C:/'
import pathlib
paths=str(pathlib.Path(__file__).parent.resolve())
#print(paths)
p = subprocess.run(['dir'], capture_output=True, shell=True,text=True,cwd=paths)
ab=str(p)
ab=ab.split('\\n')
for i in ab:
    if('<DIR>' in i and (not '..' in i or not ' . ' in i)):
        #directory h
        print(i,"Directory h")
    elif('File(s)' in i or 'Dir(s)' in i):
        #subtotal
        print(i,'subtotal h')
    else:
        #file
        print(i,'files h')        

