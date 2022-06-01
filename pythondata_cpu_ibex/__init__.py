import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2458"
version_tuple = (0, 0, 2458)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2458")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2316"
data_version_tuple = (0, 0, 2316)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2316")
except ImportError:
    pass
data_git_hash = "9b68b5ef14aff5f49b6dd32878884158e6e2a5f8"
data_git_describe = "v0.0-2316-g9b68b5ef"
data_git_msg = """\
commit 9b68b5ef14aff5f49b6dd32878884158e6e2a5f8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue May 17 17:43:55 2022 +0100

    [dv,core_ibex] Allow instructions near the top of initialised IMEM
    
    If you call the read() function on the memory model with an
    uninitialised word, it generates a UVM error.
    
    This is reasonable for data memory (where we never want to read
    something without an architectural value) but is not reasonable for
    IMEM, where Ibex runs ahead. Squash the error in this case, but force
    bad integrity for the fetch to make sure we see something explode.

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
