import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2340"
version_tuple = (0, 0, 2340)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2340")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2214"
data_version_tuple = (0, 0, 2214)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2214")
except ImportError:
    pass
data_git_hash = "0a9f5ed1daa4a7fcf46f2e21cbb02d87e569ea1a"
data_git_describe = "v0.0-2214-g0a9f5ed1"
data_git_msg = """\
commit 0a9f5ed1daa4a7fcf46f2e21cbb02d87e569ea1a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 21 16:15:08 2022 +0000

    [rtl] Remove "mispredict" ports from icache
    
    These are no longer needed: a previous commit has moved the logic that
    handles misprediction into the IF stage and branch_mispredict_i was
    dead zero.

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
