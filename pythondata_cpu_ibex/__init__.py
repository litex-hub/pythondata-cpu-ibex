import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2320"
version_tuple = (0, 0, 2320)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2320")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2194"
data_version_tuple = (0, 0, 2194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2194")
except ImportError:
    pass
data_git_hash = "72acfe2fcae98dd4af0deccdfd2c41e04b06d58d"
data_git_describe = "v0.0-2194-g72acfe2f"
data_git_msg = """\
commit 72acfe2fcae98dd4af0deccdfd2c41e04b06d58d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 25 09:02:58 2022 +0000

    [fcov, doc] Update coverage plan
    
    Added coverpoint and cross names to relevant plan entries so plan is up
    to date with implemented coverage. Also some minor changes to remove
    plan entries that are no longer required.

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
