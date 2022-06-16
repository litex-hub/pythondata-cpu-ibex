import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2462"
version_tuple = (0, 0, 2462)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2462")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2320"
data_version_tuple = (0, 0, 2320)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2320")
except ImportError:
    pass
data_git_hash = "31531f73255a75ca5d500dff5c08ec7ecab582c7"
data_git_describe = "v0.0-2320-g31531f73"
data_git_msg = """\
commit 31531f73255a75ca5d500dff5c08ec7ecab582c7
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 15 17:45:40 2022 -0700

    Update crash dump to contain mtval
    
    - mtval is a bit more useful for double fault situations
      as on the second exception we can still "remember" the
      data address and PC of the first exception.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
