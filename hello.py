#!/usr/bin/env python3
import os
import json
import cgi
import cgitb
import templates

cgitb.enable()


print("Content-type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))


# print("Content-type: text/html")
# print()
# print(templates.login_page())

# form = cgi.FieldStorage()
# user = form.getfirst("username")
# print(user)
