import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2350"
version_tuple = (0, 0, 2350)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2350")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2224"
data_version_tuple = (0, 0, 2224)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2224")
except ImportError:
    pass
data_git_hash = "f49f452f2a4d7c7120726af901ece08be1e63e3d"
data_git_describe = "v0.0-2224-gf49f452f"
data_git_msg = """\
commit f49f452f2a4d7c7120726af901ece08be1e63e3d
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Fri Apr 8 18:03:41 2022 +0100

    Improve docs explaining Makefile variable dependencies

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
