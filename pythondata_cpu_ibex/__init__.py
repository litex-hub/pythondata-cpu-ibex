import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2288"
version_tuple = (0, 0, 2288)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2288")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2162"
data_version_tuple = (0, 0, 2162)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2162")
except ImportError:
    pass
data_git_hash = "d3bd063662ed278cacdb9680baacddf5688955aa"
data_git_describe = "v0.0-2162-gd3bd0636"
data_git_msg = """\
commit d3bd063662ed278cacdb9680baacddf5688955aa
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Feb 21 17:54:19 2022 +0000

    [rtl] Add prim_buf for security critical signals
    
    A sufficiently agressive optimiser may optimise these away as under
    normal functioning they effectively don't do anything. They are purely
    to detect the presence of induced faults.

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
