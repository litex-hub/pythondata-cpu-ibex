import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2291"
version_tuple = (0, 0, 2291)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2291")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2165"
data_version_tuple = (0, 0, 2165)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2165")
except ImportError:
    pass
data_git_hash = "bdf2f2b44076c8e9a00fa6dcbee0a409026e5c3a"
data_git_describe = "v0.0-2165-gbdf2f2b4"
data_git_msg = """\
commit bdf2f2b44076c8e9a00fa6dcbee0a409026e5c3a
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Feb 23 16:09:57 2022 +0000

    [ibex, dv] Added agent configuration for ibex_mem_intf_response_agent
    
    Defining agent configuration for any agent is a standard UVM flow and is
    a cleaner flow for defining delay between driving sequence items,
    passing virtual interface etc.
    
    Agent configuration has been added to the existing agent to make delay
    configuration more flexible in the future.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
