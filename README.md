# THIS REPOSITORY IS NO LONGER MAINTAINED

# Xen Server Board

A Python application that lists all internal VMs

![](https://raw.github.com/boxuk/xen-board/master/static/preview.png)

## Requirements

+ Python 2.7
+ Pip

## Use

This application can be used to list all internal VMs to help developers and people working on support

It requires 3 env variables to be set for Xen server authentication.
Create a .env file in the project root with the following info.

```
export XEN_HOST=http://IPADDRESS
export XEN_USER=USER
export XEN_PWD=PASSEORD
```

Source it with

```
source .env
```

```
pip install requirements.txt
```

Run the server

```
python app.py
```
