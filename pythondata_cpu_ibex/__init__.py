import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2084"
version_tuple = (0, 0, 2084)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2084")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1989"
data_version_tuple = (0, 0, 1989)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1989")
except ImportError:
    pass
data_git_hash = "d78e0d9a068b4b37b79d205a1f3de1fea907e07d"
data_git_describe = "v0.0-1989-gd78e0d9a"
data_git_msg = """\
commit d78e0d9a068b4b37b79d205a1f3de1fea907e07d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 12 17:47:31 2021 +0000

    [rtl] Hard wire dcsr.stepie to 0
    
    This indicates interrupts do not occur in single step mode.
    
    Fixes #1279

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
