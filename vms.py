#!/usr/bin/env python

# ===============================================
#
# A dashboard for internal VMs
#
# ===============================================

import XenAPI, os

class Session(object):

    def __init__(self, host, user, password):
        self.session = XenAPI.Session(host)
        self.user = user
        self.password = password
        self.login()

    def __repr__(self): pass

    def login(self):
        self.session.xenapi.login_with_password(self.user, self.password)

    def read_ip_address(self, vm_uuid):
        """ Fetch the ip address for a VM """
        return self.session.xenapi.VM.get_by_uuid(vm_uuid)

    def vm_info(self, vm):
        """ Returns useful information about a VM
            - name The name of the VM
            - state Whether or not the VM is actually running
            - uuid The unique UUID for a VM
        """
        return { 'name' : vm['name_label'],
                 'state' : vm['power_state'],
                 'uuid' : vm['uuid'] }

    def vm_list(self, *args, **kwargs):
        """ List all running VMs """
        all = self.session.xenapi.VM.get_all()
        vms = []
        for vm in all:
            record = self.session.xenapi.VM.get_record(vm)
            if not(record["is_a_template"]):
                vms.append(record)

        return [self.vm_info(vm) for vm in vms]

    def running_vms(self):
        """ Returns only the VMs that are active """
        return [vm for vm in self.vm_list() if vm['state'] == "Running"]
