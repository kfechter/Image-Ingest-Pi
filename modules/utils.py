import os
import uuid
import getpass

PI_MODEL_PATH = "/sys/firmware/devicetree/base/model"

def on_pi():
    if os.name == "nt":
        return False
    if os.path.exists(PI_MODEL_PATH):
        pi_file = open(PI_MODEL_PATH, "r")
        pi_model = pi_file.read()
        pi_file.close()
        if("Raspberry Pi" in pi_model):
            return True
        else:
            return False
    else:
        return False
    
def get_logger_params(on_pi):
        #Setup Logging
    uuid_val =str(uuid.uuid1())
    if on_pi is True:
        # Extract serial from cpuinfo file
        user = "0000000000000000"
        try:
            f = open('/proc/cpuinfo','r')
            for line in f:
                if line[0:6]=='Serial':
                    cpuserial = line[10:26]
            f.close()
        except:
            user = "ERROR000000000"
    else:
        user = str(getpass.getuser())
    return uuid_val, user