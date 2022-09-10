import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2553"
version_tuple = (0, 0, 2553)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2553")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2411"
data_version_tuple = (0, 0, 2411)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2411")
except ImportError:
    pass
data_git_hash = "02ccf9e5d066fbb8132ba712314558da974c3601"
data_git_describe = "v0.0-2411-g02ccf9e5"
data_git_msg = """\
commit 02ccf9e5d066fbb8132ba712314558da974c3601
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Sep 7 13:01:43 2022 +0100

    [ci] Bump cosim version for privilege spec updates

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
