import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2306"
version_tuple = (0, 0, 2306)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2306")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2180"
data_version_tuple = (0, 0, 2180)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2180")
except ImportError:
    pass
data_git_hash = "9ef123f2b1c673f61d3aa4b8f22d6760f3b079f7"
data_git_describe = "v0.0-2180-g9ef123f2"
data_git_msg = """\
commit 9ef123f2b1c673f61d3aa4b8f22d6760f3b079f7
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Mar 15 12:01:04 2022 +0000

    [icache, dv] Removed support for single clock cycle PMP error response
    
    Earlier the design supported single clock cycle error responses from PMP
    block whenever a read was done from blocked memory. Now there is at
    least one clock cycle delay after the request has been granted for the
    error to be asserted. Therefore, this commit removes the support for
    single clock cycle PMP error response.

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
