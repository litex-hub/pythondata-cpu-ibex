import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2093"
version_tuple = (0, 0, 2093)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2093")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1998"
data_version_tuple = (0, 0, 1998)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1998")
except ImportError:
    pass
data_git_hash = "b04c1850b69eee3979f485eb21d4645d73c631ba"
data_git_describe = "v0.0-1998-gb04c1850"
data_git_msg = """\
commit b04c1850b69eee3979f485eb21d4645d73c631ba
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 5 12:39:09 2021 +0100

    Avoid encumbered name in ibex_icache_testplan.hjson
    
    With this change, we no longer use "sanity" in non-vendored code.

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
