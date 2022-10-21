import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2604"
version_tuple = (0, 0, 2604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2462"
data_version_tuple = (0, 0, 2462)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2462")
except ImportError:
    pass
data_git_hash = "e38f534ac249128ce2c2949ba779c82504d5fe4c"
data_git_describe = "v0.0-2462-ge38f534a"
data_git_msg = """\
commit e38f534ac249128ce2c2949ba779c82504d5fe4c
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Wed Oct 19 18:24:37 2022 +0100

    Add wall-clock timeout within rtl simulation to gracefully end
    
    Use a DPI call to unix 'date' to implement a wall-clock timeout entirely within
    a simulation. This allows the UVM environment to gracefully end when the
    threshold is reached, and for things like logs and coverage databases to be
    generated correctly.
    Previously, a process-level timeout was used, which gave the running simulation
    no time to commit any logs/databases to disk before ending. Hence we would not
    gather any coverage from timed-out tests.
    
    A plusarg 'test_timeout_s' can be specified to each test to set the timeout. The
    default timeout is 1800s.

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
