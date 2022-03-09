import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2298"
version_tuple = (0, 0, 2298)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2298")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2172"
data_version_tuple = (0, 0, 2172)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2172")
except ImportError:
    pass
data_git_hash = "e6eb4fb11d8e1626e01ca76052352696f476586e"
data_git_describe = "v0.0-2172-ge6eb4fb1"
data_git_msg = """\
commit e6eb4fb11d8e1626e01ca76052352696f476586e
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Mar 1 10:15:17 2022 +0000

    [ibex, dv] Added a sequence to toggle fetch_enable_i pin
    
    Ibex has a top-level `fetch_enable_i` input. When set to on (noting it's a multi-bit signal for
    security hardening though only the bottom bit is looked at for non secure ibex) Ibex executes
    normally. When set to off Ibex will stop executing. Randomly toggling it should have no functional
    effect on Ibex's behaviour.
    The fetch enable sequence will randomly toggle the value of `fetch_enable_i` with a configurable
    bias between the 'On' value and all other values.

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
