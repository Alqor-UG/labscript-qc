"""
In this file, we will define all the settings for the maintainer. Any instance of labscript-qc has to change this file
to suit their needs. The maintainer will be responsible for updating the backends on the storage provider.
"""

from mot.config import spooler_object as mot_spooler

# valid storage types are: "local", "mongodb" and "dropbox"
storage_type = "local"

# configure the backends
backends = {
    "mot": mot_spooler,
}
