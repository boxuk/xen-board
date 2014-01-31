# ===============================================
#
# XenBoard Web app
#
# ===============================================

from flask import Flask, jsonify, render_template
from vms import Session
import os

app = Flask(__name__)

HOST = os.environ['XEN_HOST']
USER = os.environ['XEN_USER']
PWD  = os.environ['XEN_PWD']

session = Session(HOST, USER, PWD)

@app.route("/")
def home():
	vms = session.vm_list()
	return render_template("index.html", vms=vms)

@app.route("/api/vms")
def active_vms():
	vms = session.vm_list()
	return jsonify(vms=vms)

if __name__ == "__main__":
	print(HOST)
	print(USER)
	print(PWD)
	app.run(debug=True,
		port=5001)
