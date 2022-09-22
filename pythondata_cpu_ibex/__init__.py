import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2555"
version_tuple = (0, 0, 2555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2413"
data_version_tuple = (0, 0, 2413)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2413")
except ImportError:
    pass
data_git_hash = "70186c57aeff46ff47b80e8f3d6e2c3d849f2e5b"
data_git_describe = "v0.0-2413-g70186c57"
data_git_msg = """\
commit 70186c57aeff46ff47b80e8f3d6e2c3d849f2e5b
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Sep 9 11:06:36 2022 +0100

    [rtl] Add ic_scr_key_valid field to CPUCTRL (renamed CPUCTRLSTS)
    
    The ic_scr_key_valid field indicates whether the ICache scrambling key
    is valid.
    
    CPUCTRL is also renamed CPUCTRLSTS as it contains both control and
    status bits.

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
