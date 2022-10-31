import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2639"
version_tuple = (0, 0, 2639)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2639")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2497"
data_version_tuple = (0, 0, 2497)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2497")
except ImportError:
    pass
data_git_hash = "b278e5b26747ef85cdda660ab7f48e0aadfe432c"
data_git_describe = "v0.0-2497-gb278e5b2"
data_git_msg = """\
commit b278e5b26747ef85cdda660ab7f48e0aadfe432c
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Sat Oct 29 10:48:35 2022 +0100

    [dv] Fix riscv_mem_error_test
    
    Memory errors trigger the same exception as PMP failures. For this test
    we simply need to return to the failing instructions rather than the
    more complex handling from the PMP exception handler.

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
