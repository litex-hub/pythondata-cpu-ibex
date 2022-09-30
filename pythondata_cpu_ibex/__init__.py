import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2562"
version_tuple = (0, 0, 2562)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2562")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2420"
data_version_tuple = (0, 0, 2420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2420")
except ImportError:
    pass
data_git_hash = "3943a4eca3917d0a00406abb36f4951304c0b394"
data_git_describe = "v0.0-2420-g3943a4ec"
data_git_msg = """\
commit 3943a4eca3917d0a00406abb36f4951304c0b394
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Tue Sep 27 11:36:50 2022 +0100

    [pmp] Remove off mode from pmp_*_mode_cross coverpoints

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
