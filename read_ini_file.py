import configparser
import sys,os
class FileRead:
    #get all login info from the login file
    def __init__(self):
        self.file_handle = configparser.RawConfigParser()
        self.root_path = os.path.dirname(os.path.dirname(__file__))
        self.root_path+="/"
        path = os.path.join(self.root_path,"conf/")
        self.file_handle.read(path+"login.ini")

    def get_toke_url(self,datacenter):
        ardc = ["sap","eu20","us20","eu10"]
        if datacenter in ardc and datacenter in ["sap","eu10"]:
            token_url = self.file_handle["token_url"]["getTokenURL"]
            self.token_url = token_url.format(datacenter)
        elif datacenter in ardc and datacenter in ["eu20","us20"]:
            token_url = self.file_handle["token_url"]["getTokenAzureURL"]
            self.token_url = token_url.format(datacenter)
        return self.token_url

    #get auth for getting all tenant
    def get_login_info_for_get_tenant(self,datacenter,space):
        user = self.file_handle["tenant_users"]["user_tenant_login_"+datacenter+"_"+space]
        pwd = self.file_handle["tenant_password"]["password_tenant_login_"+datacenter+"_"+space]
        return user,pwd

    # for kafka auth
    def get_login_info_for_kafka(self,datacenter,space):
        #user password secret by the
        login_user = self.file_handle["kafka_users"]["user_"+datacenter+"_"+space]
        login_password = self.file_handle["kafka_password"]["password_"+datacenter+"_"+space]
        print(login_user,login_password)
        return login_user,login_password

    def get_space_tenant_id_for_kafka(self, datacenter, space):
        tenant_id = self.file_handle["tenant_id"][datacenter+"_"+space+"_tenant_id"]
        return tenant_id



    def get_patch_url(self):
        base_patch_url = self.file_handle["patch_url"]["base_url"]
        return base_patch_url
    # get_login_info("int")
# if __name__ == '__main__':
#     count = 1
#     for i in range(8):
#         count += 1
#     print(count)
