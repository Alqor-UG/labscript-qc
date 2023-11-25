"""
In this file, we will define all the settings for the maintainer. Any instance of labscript-qc has to change this file
to suit their needs. The maintainer will be responsible for updating the backends on the storage provider.
"""

import sys
from decouple import config

# Get the value of the EXP_SCRIPT_FOLDER variable
exp_script_folder = config("LAB_SCRIPT_FOLDER")
print(exp_script_folder)
# Add EXP_SCRIPT_FOLDER to the system path
sys.path.append(exp_script_folder)

from mot import config

# valid storage types are: "local", "mongodb" and "dropbox"
storage_type = "local"

# configure the backends
backends = {
    "mot": config.spooler_object,
}
