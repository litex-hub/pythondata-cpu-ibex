import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2304"
version_tuple = (0, 0, 2304)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2304")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2178"
data_version_tuple = (0, 0, 2178)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2178")
except ImportError:
    pass
data_git_hash = "be5fffa656a3a153ae5bb8786f43540179632d77"
data_git_describe = "v0.0-2178-gbe5fffa6"
data_git_msg = """\
commit be5fffa656a3a153ae5bb8786f43540179632d77
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Mar 16 12:26:16 2022 +0000

    [icache, dv] Fixed regression failure in ibex_icache_back_line
    
    There was issue with rtespect to calculating number of instructions per
    word and this commit fixes that issue.
    
    Number of instructions per word = 1/4*1 + 3/4(1/4*3/2 + 3/4*2) = 53/32.
    Earlier th5s was calculated as 7/4.
    Ideal window length needed to calculate fetch ratio percentage is
    calculated as 53/32*C*2 = 848. Earlier it was calculated to be 300.

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
