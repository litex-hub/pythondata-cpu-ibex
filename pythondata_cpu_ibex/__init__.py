import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2581"
version_tuple = (0, 0, 2581)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2581")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2439"
data_version_tuple = (0, 0, 2439)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2439")
except ImportError:
    pass
data_git_hash = "4608df46060dc1fe916d71ac001ed23d2c23f490"
data_git_describe = "v0.0-2439-g4608df46"
data_git_msg = """\
commit 4608df46060dc1fe916d71ac001ed23d2c23f490
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Fri Oct 7 15:03:45 2022 +0100

    [dv] Shellcheck prettify script
    
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
