import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2589"
version_tuple = (0, 0, 2589)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2589")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2447"
data_version_tuple = (0, 0, 2447)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2447")
except ImportError:
    pass
data_git_hash = "75a93dbed0dbe340b637c82e2a8e3ba1b841ecc3"
data_git_describe = "v0.0-2447-g75a93dbe"
data_git_msg = """\
commit 75a93dbed0dbe340b637c82e2a8e3ba1b841ecc3
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Tue Oct 11 14:29:36 2022 +0100

    Fixup signal used when checking for ebreak cause

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
