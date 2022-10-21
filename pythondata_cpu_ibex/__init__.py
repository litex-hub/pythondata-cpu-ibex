import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2600"
version_tuple = (0, 0, 2600)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2600")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2458"
data_version_tuple = (0, 0, 2458)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2458")
except ImportError:
    pass
data_git_hash = "a376f85f26df52cd4ae0767fbebfdaa0dd0d0e07"
data_git_describe = "v0.0-2458-ga376f85f"
data_git_msg = """\
commit a376f85f26df52cd4ae0767fbebfdaa0dd0d0e07
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Fri Oct 14 11:22:50 2022 +0100

    [lint] Shellcheck bash scripts in repo

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
