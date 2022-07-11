import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2464"
version_tuple = (0, 0, 2464)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2464")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2322"
data_version_tuple = (0, 0, 2322)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2322")
except ImportError:
    pass
data_git_hash = "ab510f8acf2804efbe0a8d4cf93452b02acc05fe"
data_git_describe = "v0.0-2322-gab510f8a"
data_git_msg = """\
commit ab510f8acf2804efbe0a8d4cf93452b02acc05fe
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Jun 29 17:59:05 2022 +0100

    [dv/doc] Tweaks/fixes to functional coverage
    
    This fixes up some minor issues in the functional coverage plan and
    implemented cover points

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
