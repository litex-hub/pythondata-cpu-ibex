import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2632"
version_tuple = (0, 0, 2632)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2632")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2490"
data_version_tuple = (0, 0, 2490)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2490")
except ImportError:
    pass
data_git_hash = "980f73b047f961df470d6c26146f82447b606839"
data_git_describe = "v0.0-2490-g980f73b0"
data_git_msg = """\
commit 980f73b047f961df470d6c26146f82447b606839
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Oct 26 22:08:07 2022 +0100

    [cosim] Fixup ebreak behaviour
    
    When DCSR is set such that ebreak will enter debug mode we were getting
    cosim mismatches. This was because Ibex produces the ebreak on the RVFI
    interface and spike effectively skips right over it and executes the
    first instruction of the debug handler immediately. Traps have similar
    but not identical behaviour so we need a special case in the step
    function to handle this.

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
