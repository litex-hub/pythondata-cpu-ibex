import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2614"
version_tuple = (0, 0, 2614)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2614")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2472"
data_version_tuple = (0, 0, 2472)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2472")
except ImportError:
    pass
data_git_hash = "bbda68a0df2f896e920e820a2f759f6855b34148"
data_git_describe = "v0.0-2472-gbbda68a0"
data_git_msg = """\
commit bbda68a0df2f896e920e820a2f759f6855b34148
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Oct 25 19:29:33 2022 +0100

    [dv] Disable bad integrity on uninitialised memory for selected tests
    
    From an initial triage and test regression run these tests benefit from
    this.

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
