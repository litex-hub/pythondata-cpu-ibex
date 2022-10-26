import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2613"
version_tuple = (0, 0, 2613)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2613")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2471"
data_version_tuple = (0, 0, 2471)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2471")
except ImportError:
    pass
data_git_hash = "1d4cf9b207467eb37cbcd7c20ffcdd55cc7077e1"
data_git_describe = "v0.0-2471-g1d4cf9b2"
data_git_msg = """\
commit 1d4cf9b207467eb37cbcd7c20ffcdd55cc7077e1
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Oct 25 17:36:31 2022 +0100

    [dv] Add single step over exception coverpoint

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
