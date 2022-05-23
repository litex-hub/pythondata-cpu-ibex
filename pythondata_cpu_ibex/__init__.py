import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2429"
version_tuple = (0, 0, 2429)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2429")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2301"
data_version_tuple = (0, 0, 2301)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2301")
except ImportError:
    pass
data_git_hash = "c5567e8f66b68b2603023f85cbe724f598134ca2"
data_git_describe = "v0.0-2301-gc5567e8f"
data_git_msg = """\
commit c5567e8f66b68b2603023f85cbe724f598134ca2
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Thu May 19 12:03:12 2022 +0100

    Change makefile default simulator for core_ibex dv to xcelium

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
