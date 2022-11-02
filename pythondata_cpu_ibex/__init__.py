import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2644"
version_tuple = (0, 0, 2644)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2644")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2502"
data_version_tuple = (0, 0, 2502)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2502")
except ImportError:
    pass
data_git_hash = "63be01b6082d335f04d98056760f029faf60a424"
data_git_describe = "v0.0-2502-g63be01b6"
data_git_msg = """\
commit 63be01b6082d335f04d98056760f029faf60a424
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Wed Oct 26 10:40:39 2022 +0000

    [dv] Add test glitching PC
    
    This commit addresses #1755 by verifying that a glitch on the PC of Ibex
    raises an internal major alert in the core.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
