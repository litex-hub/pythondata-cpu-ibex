import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2575"
version_tuple = (0, 0, 2575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2433"
data_version_tuple = (0, 0, 2433)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2433")
except ImportError:
    pass
data_git_hash = "574d993dcde5d734e85e9698337aa8096152c58d"
data_git_describe = "v0.0-2433-g574d993d"
data_git_msg = """\
commit 574d993dcde5d734e85e9698337aa8096152c58d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Sep 28 17:53:49 2022 +0100

    [ci] Switch to downloading verilator from GCP bucket
    
    Previously it was sourced from the OpenSUSE build service. This has
    produced some reliability issues. Downloading pre-built binaries from a
    GCP bucket should improve things.

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
