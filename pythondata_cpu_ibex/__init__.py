import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2615"
version_tuple = (0, 0, 2615)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2615")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2473"
data_version_tuple = (0, 0, 2473)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2473")
except ImportError:
    pass
data_git_hash = "5f5a70fca90917cc6152be4b1e4d9679d0357a3b"
data_git_describe = "v0.0-2473-g5f5a70fc"
data_git_msg = """\
commit 5f5a70fca90917cc6152be4b1e4d9679d0357a3b
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Tue Oct 11 11:42:21 2022 +0100

    Tweak regressions around PMP, allow for double_faults, uninit_accesses
    
    Add 180s timeout for pmp_full_random tests (this sees a reasonable pass-rate)
    
    Tweaked to latest api for double_fault detector
    
    Squashed changes from Marno's ongoing work:
    [pmp] Adjust full random PMP to use random memory addresses
    [pmp] Enable double fault detecter for MML read only test
    [dv,pmp] Add double fault pass flag
    [dv,pmp] Different parameters for pmp full random test

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
