import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2633"
version_tuple = (0, 0, 2633)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2633")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2491"
data_version_tuple = (0, 0, 2491)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2491")
except ImportError:
    pass
data_git_hash = "e63bb13d0ab2dad4ee608323617a7467cf8f5816"
data_git_describe = "v0.0-2491-ge63bb13d"
data_git_msg = """\
commit e63bb13d0ab2dad4ee608323617a7467cf8f5816
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Oct 31 16:19:42 2022 +0000

    [ci] Bump cosim version to latest
    
    This integrates in the ebreak behaviour changes in spike

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
