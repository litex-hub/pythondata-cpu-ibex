import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2459"
version_tuple = (0, 0, 2459)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2459")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2317"
data_version_tuple = (0, 0, 2317)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2317")
except ImportError:
    pass
data_git_hash = "f71b23ddf8b93c63f0c42eb3cecf77aff177530d"
data_git_describe = "v0.0-2317-gf71b23dd"
data_git_msg = """\
commit f71b23ddf8b93c63f0c42eb3cecf77aff177530d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jun 3 09:22:04 2022 +0200

    Update google_riscv-dv to google/riscv-dv@0b2b3d6
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision 0b2b3d65ce8fdff4de8974d1f328a90d6c1db5dd
    
    * [epmp] Add support for mseccfg CSR (Pirmin Vogel)
    
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
