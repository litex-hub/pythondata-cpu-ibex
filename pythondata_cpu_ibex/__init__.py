import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2652"
version_tuple = (0, 0, 2652)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2652")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2510"
data_version_tuple = (0, 0, 2510)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2510")
except ImportError:
    pass
data_git_hash = "31cc8e0b5a8ede3f9876e93dd0194e29aae93bf6"
data_git_describe = "v0.0-2510-g31cc8e0b"
data_git_msg = """\
commit 31cc8e0b5a8ede3f9876e93dd0194e29aae93bf6
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Tue Nov 1 09:46:02 2022 +0000

    Increase iterations for PMP tests to improve coverage

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
