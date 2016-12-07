# flask-https
Simple HTTPS site running on Flask

## Installation
Set up a virtualenv:
```
[root@flask flask-https]# virtualenv venv
New python executable in venv/bin/python
Installing Setuptools..............................................................................................................................................................................................................................done.
Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.

[root@flask flask-https]# source venv/bin/activate
```

Use yum and pip to get the following prerequisites:
```
(venv)[root@flask flask-https]# yum install gcc libffi-devel python-devel openssl-devel
(venv)[root@flask flask-https]# pip install flask pyOpenSSL six cffi cryptography
```

Create your key and cert:
```
[root@flask flask-https]# openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
Generating a 2048 bit RSA private key
.....................................................................+++
...................................+++
writing new private key to 'server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:US
State or Province Name (full name) []:VT
Locality Name (eg, city) [Default City]:Burlington
Organization Name (eg, company) [Default Company Ltd]:IPAs For Everyone
Organizational Unit Name (eg, section) []:
Common Name (eg, your name or your server's hostname) []:flask
Email Address []:
```

GO!
```
(venv)[root@flask flask-https]#  * Running on https://0.0.0.0:443/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 188-286-719
```
