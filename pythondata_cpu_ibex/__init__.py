import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2062"
version_tuple = (0, 0, 2062)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2062")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1971"
data_version_tuple = (0, 0, 1971)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1971")
except ImportError:
    pass
data_git_hash = "6ebc6bcb9f4574ab2adff9ec1c27f052ee620b69"
data_git_describe = "v0.0-1971-g6ebc6bcb"
data_git_msg = """\
commit 6ebc6bcb9f4574ab2adff9ec1c27f052ee620b69
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 24 15:07:06 2021 +0000

    [simple_system] Fix type for mhpmcounter_get
    
    It's probably clearer if this 64-bit counter is treated as a uint64_t,
    not an int64_t (the code using it downstream expects non-negative
    values).

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
