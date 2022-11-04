import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2656"
version_tuple = (0, 0, 2656)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2656")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2514"
data_version_tuple = (0, 0, 2514)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2514")
except ImportError:
    pass
data_git_hash = "ef43917dec825e9c86aa8e086734465f7c1a3bf2"
data_git_describe = "v0.0-2514-gef43917d"
data_git_msg = """\
commit ef43917dec825e9c86aa8e086734465f7c1a3bf2
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Nov 2 11:06:27 2022 +0000

    [dv] Fix random data on uninit accesses
    
    Previously the memory model writes didn't work correctly leaving an
    incoherent view of memory.

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
