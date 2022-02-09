import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2273"
version_tuple = (0, 0, 2273)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2273")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2149"
data_version_tuple = (0, 0, 2149)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2149")
except ImportError:
    pass
data_git_hash = "bbc48a0c34342935b5bd326bb8351168d6258ec7"
data_git_describe = "v0.0-2149-gbbc48a0c"
data_git_msg = """\
commit bbc48a0c34342935b5bd326bb8351168d6258ec7
Author: fabian <36959980+ftorres16@users.noreply.github.com>
Date:   Tue Feb 8 18:53:26 2022 -0500

    Add srecord as simple_system prerequisite

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
