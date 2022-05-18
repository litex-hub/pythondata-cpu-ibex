import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2426"
version_tuple = (0, 0, 2426)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2426")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2298"
data_version_tuple = (0, 0, 2298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2298")
except ImportError:
    pass
data_git_hash = "efd289dc17f8f9574030d9aeccd7c93592c421e5"
data_git_describe = "v0.0-2298-gefd289dc"
data_git_msg = """\
commit efd289dc17f8f9574030d9aeccd7c93592c421e5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon May 16 16:55:29 2022 +0100

    [core_ibex] Disable waves by default
    
    This seems like something you'd want to enable explicitly, to avoid
    filling up a disk on a big run.

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
