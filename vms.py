#!/usr/bin/env python

# A dashboard for internal VMs

import XenAPI

import os

class Session(object):

    def __init__(self, host, user, password):
        self.session = XenAPI.Session(host)
        self.user = user
        self.password = password
        self.login()

    def login(self):
        self.session.xenapi.login_with_password(self.user, self.password)

    def read_ip_address(self, vm_uuid):
        return self.session.xenapi.VM.get_by_uuid(vm_uuid)

    def vm_info(self, vm):
        return { 'name' : vm['name_label'] }

    def vm_list(self):
        """ List all running VMs """
        all = self.session.xenapi.VM.get_all()
        vms = []
        for vm in all:
            record = self.session.xenapi.VM.get_record(vm)
            if not(record["is_a_template"]):
                vms.append(record)
        return [self.vm_info(vm) for vm in vms]

    def running_vms(self):
        return [vm for vm in self.vm_list() if vm["power_state"] == "Running"]
