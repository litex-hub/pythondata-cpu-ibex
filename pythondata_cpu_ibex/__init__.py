import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2199"
version_tuple = (0, 0, 2199)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2199")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2087"
data_version_tuple = (0, 0, 2087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2087")
except ImportError:
    pass
data_git_hash = "ff6797b26f545f6f306c4511fe87d1f838d69727"
data_git_describe = "v0.0-2087-gff6797b2"
data_git_msg = """\
commit ff6797b26f545f6f306c4511fe87d1f838d69727
Author: Udi <udij@google.com>
Date:   Fri Aug 14 17:27:28 2020 -0700

    [ibex/ml] add CSR/mem_error tests to ml_testlist
    
    Signed-off-by: Udi <udij@google.com>

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
