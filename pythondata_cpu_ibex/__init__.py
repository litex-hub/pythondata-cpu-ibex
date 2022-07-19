import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2471"
version_tuple = (0, 0, 2471)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2471")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2329"
data_version_tuple = (0, 0, 2329)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2329")
except ImportError:
    pass
data_git_hash = "1ea89a423b314f53840510edadb4ef3487281f2d"
data_git_describe = "v0.0-2329-g1ea89a42"
data_git_msg = """\
commit 1ea89a423b314f53840510edadb4ef3487281f2d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jul 19 16:06:21 2022 +0100

    [dv] Fix traps in simple system cosim
    
    Previously any traps seen on RVFI were skipped over. This was old
    behaviour. With the latest cosim setup traps must be passed to the
    `step` function.

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
