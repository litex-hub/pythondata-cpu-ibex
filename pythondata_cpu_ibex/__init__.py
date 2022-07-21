import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2475"
version_tuple = (0, 0, 2475)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2475")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2333"
data_version_tuple = (0, 0, 2333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2333")
except ImportError:
    pass
data_git_hash = "50d183fc1b5080dc0aecb14f54b008e9c65c2d0f"
data_git_describe = "v0.0-2333-g50d183fc"
data_git_msg = """\
commit 50d183fc1b5080dc0aecb14f54b008e9c65c2d0f
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jul 19 18:35:10 2022 +0100

    [ci] Add pmp_smoke_test cosim run to CI

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
