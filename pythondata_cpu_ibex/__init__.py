import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2323"
version_tuple = (0, 0, 2323)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2323")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2197"
data_version_tuple = (0, 0, 2197)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2197")
except ImportError:
    pass
data_git_hash = "2317bb7fc0e331e5c3939c148ed0ada109211330"
data_git_describe = "v0.0-2197-g2317bb7f"
data_git_msg = """\
commit 2317bb7fc0e331e5c3939c148ed0ada109211330
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri Mar 18 14:56:07 2022 +0000

    [icache, dv] Added ram interface and enables ecc error injection.
    
    This commit adds ibex_icache_ram_if to connect between DUT and tag /
    data RAMs.
    
    This interface injects 1 or 2 bit error on rdata if enable_ecc_errors
    bit is set. It also checks that ecc_err_o pin is asserted by DUT
    whenever an ecc error is injected.
    
    ibex_icache_ecc_vseq and ibex_icache_base_vseq have been modified to
    inject ecc errors through the ram interface.

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
