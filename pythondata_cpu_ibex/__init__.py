import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2058"
version_tuple = (0, 0, 2058)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2058")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1968"
data_version_tuple = (0, 0, 1968)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1968")
except ImportError:
    pass
data_git_hash = "7cee76bf05134c683154b26f4d18c2843cbfca64"
data_git_describe = "v0.0-1968-g7cee76bf"
data_git_msg = """\
commit 7cee76bf05134c683154b26f4d18c2843cbfca64
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Feb 10 16:36:26 2021 +0000

    [dv] Reorder checks in sim.py
    
    The UVM log should be checked for failures before attempting to process
    the core trace log. A simulation failure could mean the trace log
    doesn't exist and is is preferable to report the simulation error from
    the log rather than trace not found as a failure cause.

"""

# Tool version info
tool_version_str = "0.0.post90"
tool_version_tuple = (0, 0, 90)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post90")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
