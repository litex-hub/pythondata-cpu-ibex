import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2608"
version_tuple = (0, 0, 2608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2466"
data_version_tuple = (0, 0, 2466)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2466")
except ImportError:
    pass
data_git_hash = "28935490c28923f486314e61696820bf45e23aae"
data_git_describe = "v0.0-2466-g28935490"
data_git_msg = """\
commit 28935490c28923f486314e61696820bf45e23aae
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Oct 21 17:23:08 2022 +0200

    [rtl] Protect core_busy_o with a multi-bit encoding
    
    This commit protects the core_busy_o signal using a multi-bit encoding
    to reduce the chances of an adversary for glitching this signal to low,
    thereby putting the core to sleep and e.g. not handling an alert.
    
    Without this commit, the glitch would only be detected once both the
    main core and the shadow core wake up again and the comparison of the
    core_busy_o signals continues.
    
    This resolves lowRISC/Ibex#1827.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
