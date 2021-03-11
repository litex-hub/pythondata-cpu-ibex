import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2078"
version_tuple = (0, 0, 2078)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2078")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1983"
data_version_tuple = (0, 0, 1983)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1983")
except ImportError:
    pass
data_git_hash = "50f09b71a96f87d46bbedead0cce5218c981d680"
data_git_describe = "v0.0-1983-g50f09b71"
data_git_msg = """\
commit 50f09b71a96f87d46bbedead0cce5218c981d680
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Mar 10 16:34:57 2021 +0000

    [rtl] Fix lint issues

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
