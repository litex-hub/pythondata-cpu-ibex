import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2220"
version_tuple = (0, 0, 2220)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2220")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2108"
data_version_tuple = (0, 0, 2108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2108")
except ImportError:
    pass
data_git_hash = "169785d0711335c94561a93146e069766eec138c"
data_git_describe = "v0.0-2108-g169785d0"
data_git_msg = """\
commit 169785d0711335c94561a93146e069766eec138c
Author: Michael Schaffner <msf@google.com>
Date:   Wed Dec 1 18:19:15 2021 -0800

    [secded] Switch to inverted ECC codes
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
