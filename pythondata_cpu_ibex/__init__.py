import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2427"
version_tuple = (0, 0, 2427)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2427")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2299"
data_version_tuple = (0, 0, 2299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2299")
except ImportError:
    pass
data_git_hash = "6efb4b15973011b4cd5d09ca0f3bf7c07730b5d5"
data_git_describe = "v0.0-2299-g6efb4b15"
data_git_msg = """\
commit 6efb4b15973011b4cd5d09ca0f3bf7c07730b5d5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon May 16 15:42:31 2022 +0100

    Dump riscv-dv generation messages to a log file
    
    I was previously just dumping them to /dev/null because the
    code always worked but... predictably I was wrong! Write them
    somewhere more useful for debug.

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
