import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2207"
version_tuple = (0, 0, 2207)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2207")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2095"
data_version_tuple = (0, 0, 2095)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2095")
except ImportError:
    pass
data_git_hash = "c35472abb9527a3c8e4d993f9d1f92447972e440"
data_git_describe = "v0.0-2095-gc35472ab"
data_git_msg = """\
commit c35472abb9527a3c8e4d993f9d1f92447972e440
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Wed May 12 14:12:34 2021 +0100

    [bitmanip][zba] Add support for Zba (address calculation) extension
    
    Add support for the Zba extension added in v0.93 of the bit manipulation
    specification (unchanged in v1.0.0). The new instructions added are:
    
      - sh1add: rd = (rs1 << 1) + rs2
      - sh2add: rd = (rs1 << 2) + rs2
      - sh3add: rd = (rs1 << 3) + rs2
    
    The instructions are single cycle and have been implemented using the
    adder in the ALU.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
