import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2463"
version_tuple = (0, 0, 2463)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2463")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2321"
data_version_tuple = (0, 0, 2321)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2321")
except ImportError:
    pass
data_git_hash = "5c49fad9a236351a884f55d44248e4f9a0f7c7e5"
data_git_describe = "v0.0-2321-g5c49fad9"
data_git_msg = """\
commit 5c49fad9a236351a884f55d44248e4f9a0f7c7e5
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon May 30 14:52:34 2022 +0100

    [fcov] Adding debug related functional coverage
    
    Includes coverpoints for:
    
    - Hardware trigger point matches
    - Debug simple step entrance in controller
    - Seeing different insns while single stepping
    
    Also updates on coverage plan to fill up missing mentions of
    coverpoints/crosses
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
