import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2481"
version_tuple = (0, 0, 2481)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2481")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2339"
data_version_tuple = (0, 0, 2339)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2339")
except ImportError:
    pass
data_git_hash = "83ac7a94d25f002c99a1d494f1dc32c81b7588ef"
data_git_describe = "v0.0-2339-g83ac7a94"
data_git_msg = """\
commit 83ac7a94d25f002c99a1d494f1dc32c81b7588ef
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Sat Jul 23 19:23:41 2022 +0100

    Don't check MCAUSE[31] in debug_mode to identify sync/async trap
    
    Interrupts are disabled in Debug Mode (Sdext 4.1.2), and simultaneously
    registers, including MCAUSE, are not updated by exceptions (Sdext 4.1.3),
    so reading MCAUSE[31] after an exception (eg. invalid instruction) in
    debug_mode may still report the previous cause (which could be an interrupt).

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
