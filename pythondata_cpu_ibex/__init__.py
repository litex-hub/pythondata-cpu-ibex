import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2061"
version_tuple = (0, 0, 2061)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2061")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1970"
data_version_tuple = (0, 0, 1970)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1970")
except ImportError:
    pass
data_git_hash = "99b8f612234adc76e70cfc53f00a451b3ad4662a"
data_git_describe = "v0.0-1970-g99b8f612"
data_git_msg = """\
commit 99b8f612234adc76e70cfc53f00a451b3ad4662a
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Feb 10 16:25:51 2021 +0000

    [rtl] Debug mode controller changes
    
    * `if` in `DBG_TAKEN_IF` is needless as the conditions it checks will be
      true if controller enters `DBG_TAKEN_IF` state
    
    * flop `enter_debug_mode` so `FLUSH` state looks at what
      `enter_debug_mode` was when it was seen in `DECODE` state rather than
      what it has become. In particular the controller could enter `FLUSH`
      on the basis of performing a WFI then divert down the debug control
      path due to a new debug request being raised. In this instance it is
      preferable for the WFI to complete entering `SLEEP` before the debug
      request wakes the core back up.

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
