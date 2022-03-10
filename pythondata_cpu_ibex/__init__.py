import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2300"
version_tuple = (0, 0, 2300)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2300")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2174"
data_version_tuple = (0, 0, 2174)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2174")
except ImportError:
    pass
data_git_hash = "0a8b4a4f61caface4a64f059a669e9478555a424"
data_git_describe = "v0.0-2174-g0a8b4a4f"
data_git_msg = """\
commit 0a8b4a4f61caface4a64f059a669e9478555a424
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Mar 8 16:20:28 2022 +0000

    [icache, dv] Made changes required to make TB compatible with Xcelium

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
