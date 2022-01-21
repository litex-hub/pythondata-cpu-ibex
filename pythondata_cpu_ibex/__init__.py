import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2264"
version_tuple = (0, 0, 2264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2142"
data_version_tuple = (0, 0, 2142)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2142")
except ImportError:
    pass
data_git_hash = "7c7e0e6d700cde858e740537fccbe9bc3d1144ee"
data_git_describe = "v0.0-2142-g7c7e0e6d"
data_git_msg = """\
commit 7c7e0e6d700cde858e740537fccbe9bc3d1144ee
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Jan 19 09:26:28 2022 -0800

    [ibex_tracer] Void cast function calls
    
    ...whose return value is ignored. This cleans up a compile time warning.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
