# A dashboard for internal VMs

import XenAPI

class Session(object):

    def __init__(self, user, password):
        self.session = XenAPI.Session("http://myhost")
        self.user = user
        self.password = password
        self.login()

    def login():
        self.session.xenapi.login_with_password(self.user, self.password)

    def vm_list():
        """ Fetch a list of all internal VMs """
        all = self.session.xenapi.VM.get_all_records()
        for _, vm in all.items():
            print vm["name_label"]
