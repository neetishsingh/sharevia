
from typing import Union

from fastapi import FastAPI, Request

from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

import os


app = FastAPI()
authkey=''
def allotauthkey(val=''):
    if (val==''):
        import random
        number = random.randint(1000,9999)
        return str(number)
    else:
        return val    
authkey=allotauthkey()        
    #print(number)
allowedfileextensions=["aac"," adt"," adts","accdb","accde","accdr","accdt","aif"," aifc"," aiff","aspx","avi","bat","bin","bmp","cab","cda","csv","dif","dll","doc","docm","docx","dot","dotx","eml","eps","exe","flv","gif","htm","html","ini","iso","jar","jpg","jpeg","m4a","mdb","mid"," midi","mov","mp3","mp4","mpeg","mpg","msi","mui","pdf","png","pot","potm","potx","ppam","pps","ppsm","ppsx","ppt","pptm","pptx","psd","pst","pub","rar","rtf","sldm","sldx","swf","sys","tif"," tiff","tmp","txt","vob","vsd","vsdm","vsdx","vss","vssm","vst","vstm","vstx","wav","wbk","wks","wma","wmd","wmv","wmz"," wms","wpd"," wp5","xla","xlam","xll","xlm","xls","xlsm","xlsx","xlt","xltm","xltx","xps","zip"]

def downloadlinkgenerator(add,name):
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    add=add.replace('C:\\','')
    # String which represents the QR code
    s = '../download/?file_adress='+add+'&q='+name
    return s    
def getfilefromcurrentpath(filename):
    import pathlib
    paths=str(pathlib.Path(__file__).parent.resolve())
    # Create and save the png file naming "myqr.png"
    link=paths+'/'+filename
    link='../download/?file_adress='+link.replace('C:\\','')
    return link

def generateQR():
    import pyqrcode
    import png
    from pyqrcode import QRCode
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    # String which represents the QR code
    s = str(IPAddr)+":8000"+'/a/?authk='+authkey
    
    # Generate QR code
    url = pyqrcode.create(s)
    url.png('myqr.png', scale = 6)
    
    # Create and save the svg file naming "myqr.svg"
    #url.svg("myqr.svg", scale = 8)
    
    import pathlib
    paths=str(pathlib.Path(__file__).parent.resolve())
    # Create and save the png file naming "myqr.png"
    link=paths+'/myqr.png'
    link='../download/?file_adress='+link.replace('C:\\','')
    return link

def sidebar():
    return '''<!-- Offcanvas Sidebar -->
<div class="offcanvas offcanvas-start" style="text-align:center;overflow: hidden; "id="demo">
  <div class="offcanvas-header" style="text-align:center">
    <h1 class="offcanvas-title" style="text-align:center"><img src="'''+getfilefromcurrentpath('logo.png')+'''" alt="Hanuman" style="width:100px;" class="rounded-pill"><span style="font-size:10px">v0.0.1</span></h1>
    <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
  </div>
  <div class="offcanvas-body">
  <p>Scan this QR and start sharing<p>
  <img src="'''+generateQR()+'''" alt="" width="auto" height="200">
    <div class="container mt-3">
  <h5>AuthCode:'''+authkey+'''</h5>
  <p>Important Details</p>
  <ul class="list-unstyled">
    <li>You can scan the same QR from multiple devices to share items paralelly.</li>
    <li>What next?
      <ul>
        <li>Limited File Sharing</li>
        <li>Streaming Videos without downloading</li>
        <li>Ultrafast Sharing</li>
        <li>Improved UI</li>
        
      </ul>
    </li>
    <li>Note: It is important to have python in atleast one of devices</li>
    <p>Developed by <span style="color:black;font-weight: bold;">Neetish Singh</span> with <span class="material-icons" style="color:red">
favorite
</span></p>
  </ul>
</div>
    <p></p>
    

    <p>Note:It is mandatory to have python installed in atleast 1 devices.</p>
    <button class="btn btn-secondary" type="button">Close<span class="material-icons">
close
</span></button>
  </div>
</div>'''
def navba():
    return '''<nav class="navbar navbar-expand-sm bg-light navbar-light fixed-top">
    <!-- Button to open the offcanvas sidebar -->

  <div class="container-fluid">
  
<a href="Javascript:history.go ( -1); Location.reload ()"  class="btn btn-primary">
  <span class="material-icons">
arrow_back
</span></a>
    <a class="navbar-brand" href="#">
      <img src="'''+getfilefromcurrentpath('logo.png')+'''" alt="Hanuman" style="width:100px;" class="rounded-pill"> 
      
    </a>
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#demo" style="margin:5px">
  <span class="material-icons">
menu
</span>
</button>
  </div>
</nav>'''
def newrequesthtml():
    return headofhtml()+navba()+'''<form action ="/a/">
  <div class="form-group" style="margin-top:100px;padding:50px">
    <label for="exampleInputEmail1">AuthCode</label>
    <input type="text" name="authk" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter AuthCode">
    <small id="emailHelp" class="form-text text-muted">You can ask the authcode from admin or Scan the QR to access files.</small>
  </div>
  
  <button type="submit" class="btn btn-primary" style='center;'>Verify</button>
</form></body></html>'''
def headofhtml():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>'''+navba()
@app.get("/")
def read_root():
    resh=readall('/')
    return resh

def htmltotal(head,mid,close):
    return head+mid+close

def HandleCode(ipad):
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(ipad,IPAddr)
    if(ipad==IPAddr or ('127.0.0.1'  in ipad)):
        #ask for pass
        return 0
    else:
        return 1
        #key dedo    

@app.get("/a/")
def read_item(file_adress: Union[str, None]='', request:Request=None,q: Union[str, None] = None,authk: Union[str, None] = '',response_class=HTMLResponse):
    print('------------------ye run kiya')
    client_host = request.client.host
    print(client_host,'<---------------',HandleCode(client_host))
    if(HandleCode(client_host)==0):
        authk=authkey
        return HTMLResponse(content= htmltotal(headofhtml()+sidebar(), readall('/'+file_adress,authk),'</body></html>'),status_code=200)
    else:
        if(authk!=authkey):
            return HTMLResponse(content=newrequesthtml())
        elif(authk==authkey):
            return HTMLResponse(content= htmltotal(headofhtml()+sidebar(), readall('/'+file_adress,authk),'</body></html>'),status_code=200)
        else: 
            return HTMLResponse(content=newrequesthtml())           


@app.get("/download/")
def read_item(file_adress: Union[str, None]=None, q: Union[str, None] = None):
    print('/'+file_adress)
    return downloadfile('/'+file_adress,q)

def readall(path,authk):
    #import os
    resh='''<div class="d-flex flex-wrap" style="margin-top:100px;background-color:grey;height:100%;border-radius: 25px;border: 2px solid #73AD21;">'''
    for file in os.listdir(path):
        if('$' in file):
            continue
        print('/-----------')
        ui=fetchFileIndividualdetail(path,file,authk)[-1]
        resh=resh+ui+""
    resh=resh+'</div>'
    return resh    
def fetchFileIndividualdetail(path,name,authk):
    #[filename,relativepath,isfile,isdir,size,extension]        
    filename=name
    if(path=='/'):
        xyz=path+filename
    else:    
        xyz=path+'/'+filename
    relativepath=os.path.abspath(xyz)
    isfile=os.path.isfile(xyz)
    isdir=os.path.isdir(xyz)
    size=os.path.getsize(xyz)
    extension=filename.split('.')[-1]

    ab=[filename,relativepath,isfile,isdir,size,extension]
    
    cy=createdesign(ab,authk)
    print(cy)
    if(ab[3] or ab[-1] in allowedfileextensions):
        ab.append(cy)
    else:
        ab.append('')    
    print(ab)
    return ab

import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def createdesign(data,authk):
    currentimgforfile='https://www.pngall.com/wp-content/uploads/2018/05/Files-High-Quality-PNG.png'
    currentimgfordir='https://cdn-icons-png.flaticon.com/512/3767/3767084.png'
    htsl='<div class="card" style="margin:10px;width:160px"><div class="card-body">'
    if(data[2] and data[5] in allowedfileextensions):
        #fileh
        htsl=htsl+'<img src="'+currentimgforfile+'" alt="'+data[0]+'" width="100" height="100">'
        htsl=htsl+'''<ul class="list-unstyled">
  <li>'''+data[0]+'''</li>
  <li class="test-muted">'''+str(convert_size(data[4]))+'''</li> 
  <hr>
  <ul class="list-inline">
  <li class="list-inline-item"><a href="'''+downloadlinkgenerator(data[1],data[0])+'''" class="btn btn-primary "><span class="material-icons">download</span></a></li>
  <li class="list-inline-item"><a href="?file_adress='+data[1]+data[0]+'" class="btn btn-primary disabled "><span class="material-icons">share</span></a></li>
  
</ul> 
</ul>'''
        
        #htsl=htsl+'<p>'+data[0]+'</p>'
        #htsl=htsl+'<small class="text-muted">Size:'+str(convert_size(data[4]))+'</small>'
        #htsl=htsl+'<a href="?file_adress='+data[1]+data[0]+'" class="btn btn-primary stretched-link">Go somewhere</a>'
    elif(data[3]):
        #directory h
        htsl=htsl+'<img src="'+currentimgfordir+'" alt="'+data[0]+'" width="100" height="100">'
        htsl=htsl+'''<ul class="list-unstyled">
  <li>'''+data[0]+'''</li>
  <li class="test-muted">     </li> 
  <hr>
  <ul class="list-inline">
  <li class="list-inline-item"><a href="?file_adress='+data[1]+data[0]+'" class="btn btn-primary disabled "><span class="material-icons">download</span></a></li>
  <li class="list-inline-item"><a href="?file_adress='''+data[1].replace('C:\\','')+'''&authk='''+authk+'''" class="btn btn-primary stretched-link"><span class="material-icons">open_in_new</span></a></li>
  
</ul> 
</ul>'''
       # htsl=htsl+'<a href="?file_adress='+data[1].replace('C:\\','')+'" class=" stretched-link"><span class="material-icons">folder_zip</span></a>'
    
    htsl=htsl+"</div></div>"    
    return htsl    


def downloadfile(file_path,filename):
    return FileResponse(path=file_path, filename=filename, media_type='image/png')