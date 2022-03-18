import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2309"
version_tuple = (0, 0, 2309)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2309")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2183"
data_version_tuple = (0, 0, 2183)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2183")
except ImportError:
    pass
data_git_hash = "96d8aa6c1522eae45b4ec0d03424c9c753544fe7"
data_git_describe = "v0.0-2183-g96d8aa6c"
data_git_msg = """\
commit 96d8aa6c1522eae45b4ec0d03424c9c753544fe7
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 17 22:10:06 2022 +0000

    Update spike_cosim.cc to be able to build against newer Spikes
    
    This should work with versions ibex-cosim-v0.1 and ibex-cosim-v0.2.

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
