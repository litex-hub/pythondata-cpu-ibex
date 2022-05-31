import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2455"
version_tuple = (0, 0, 2455)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2455")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2313"
data_version_tuple = (0, 0, 2313)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2313")
except ImportError:
    pass
data_git_hash = "e1f614887eef3ae089292d2ce8470c6eb80a1ae9"
data_git_describe = "v0.0-2313-ge1f61488"
data_git_msg = """\
commit e1f614887eef3ae089292d2ce8470c6eb80a1ae9
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon May 16 13:57:06 2022 +0200

    Update spike_cosim.cc to be able to build against newer Spike versions
    
    This works with versions ibex-cosim-v0.2 and ibex-cosim-v0.3. The latter
    version is required to support the mseccfg CSR added with ePMP.
    
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
