# ===============================================
#
# XenBoard Web app
#
# ===============================================

from flask import Flask, jsonify, render_template

from vms import Session
import os

app = Flask(__name__)
HOST = ""
USER = ""
PWD  = ""

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
    app.run(debug=True,
            port=5001)
