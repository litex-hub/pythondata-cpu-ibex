import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2461"
version_tuple = (0, 0, 2461)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2461")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2319"
data_version_tuple = (0, 0, 2319)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2319")
except ImportError:
    pass
data_git_hash = "81590d86c2d5d136a36c673511e0bb29973a5d13"
data_git_describe = "v0.0-2319-g81590d86"
data_git_msg = """\
commit 81590d86c2d5d136a36c673511e0bb29973a5d13
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Tue Jun 7 11:53:56 2022 +0100

    Fix multi-line string formatting in $sformatf for uvm_fatal macro
    
    Before the change the indentation of the second line would be printed as spaces
    in the fatal message.

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
