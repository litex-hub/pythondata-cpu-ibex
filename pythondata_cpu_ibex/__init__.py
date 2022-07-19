import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2470"
version_tuple = (0, 0, 2470)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2470")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2328"
data_version_tuple = (0, 0, 2328)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2328")
except ImportError:
    pass
data_git_hash = "51f114133514bb6205411ff1f9eed5791c73879e"
data_git_describe = "v0.0-2328-g51f11413"
data_git_msg = """\
commit 51f114133514bb6205411ff1f9eed5791c73879e
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Fri Jul 15 11:33:47 2022 +0100

    [lint] Point to correct Verible rules for lint workflow
    
    Signed-off-by: Marno van der Maas <mvdmaas+git@lowrisc.org>

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
