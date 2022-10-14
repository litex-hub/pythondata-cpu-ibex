import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2587"
version_tuple = (0, 0, 2587)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2587")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2445"
data_version_tuple = (0, 0, 2445)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2445")
except ImportError:
    pass
data_git_hash = "298c8789da80b08f6b67f789a087f383c9197789"
data_git_describe = "v0.0-2445-g298c8789"
data_git_msg = """\
commit 298c8789da80b08f6b67f789a087f383c9197789
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Oct 4 15:39:19 2022 +0100

    [rtl/dv] Bring back data integrity check on write responses
    
    Previously Ibex signalled a major alert on an integrity error (where
    incoming read data doesn't match its integrity bits) for both read and
    write responses. This was removed as the data part of a response to a
    write is ignored.
    
    This brings it back in a more measured way. This provides a little extra
    fault injection hardening as an attacker glitching the memory bus will
    generate an alert on both read and write responses.

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
