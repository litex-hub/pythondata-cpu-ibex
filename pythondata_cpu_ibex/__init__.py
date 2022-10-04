import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2566"
version_tuple = (0, 0, 2566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2424"
data_version_tuple = (0, 0, 2424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2424")
except ImportError:
    pass
data_git_hash = "1cdd403564f4b2e4352919f591ee9182cebcfb67"
data_git_describe = "v0.0-2424-g1cdd4035"
data_git_msg = """\
commit 1cdd403564f4b2e4352919f591ee9182cebcfb67
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Tue Oct 4 10:20:13 2022 +0100

    [formal] Remove build infrastructure for instruction cache assertions

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
