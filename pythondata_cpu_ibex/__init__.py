import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2468"
version_tuple = (0, 0, 2468)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2468")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2326"
data_version_tuple = (0, 0, 2326)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2326")
except ImportError:
    pass
data_git_hash = "5bba52713fc482309d2ca68420e5f405134dd56b"
data_git_describe = "v0.0-2326-g5bba5271"
data_git_msg = """\
commit 5bba52713fc482309d2ca68420e5f405134dd56b
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Thu Jul 14 16:44:25 2022 +0100

    Fix randomize bug, add assertion for cnt != 0

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
