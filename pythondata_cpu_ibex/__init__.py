import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2573"
version_tuple = (0, 0, 2573)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2573")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2431"
data_version_tuple = (0, 0, 2431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2431")
except ImportError:
    pass
data_git_hash = "3c11ef10b98a73c06345bd0f2fcb8d94226b4f31"
data_git_describe = "v0.0-2431-g3c11ef10"
data_git_msg = """\
commit 3c11ef10b98a73c06345bd0f2fcb8d94226b4f31
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Thu Sep 29 17:42:47 2022 +0100

    single_step test : only drive debug_req_i after stepping finishes
    
    This addresses a current testbench issue where asserting debug_req_i close to
    when single_stepping over an instruction causes an incorrect 'cause' to be
    recorded within DCSR.

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
