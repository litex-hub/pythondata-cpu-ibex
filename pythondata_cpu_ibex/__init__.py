import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2302"
version_tuple = (0, 0, 2302)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2302")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2176"
data_version_tuple = (0, 0, 2176)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2176")
except ImportError:
    pass
data_git_hash = "2f1e188346decdef988ee7cfafc7d44e8d256e7c"
data_git_describe = "v0.0-2176-g2f1e1883"
data_git_msg = """\
commit 2f1e188346decdef988ee7cfafc7d44e8d256e7c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 10 12:45:53 2022 +0000

    Fix port list in top_artya7 example
    
    The "alert_major" port was split into "internal" and "bus" parts back
    in commit 9943f9a. Update the example to match.

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
