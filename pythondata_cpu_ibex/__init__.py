import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2067"
version_tuple = (0, 0, 2067)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2067")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1976"
data_version_tuple = (0, 0, 1976)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1976")
except ImportError:
    pass
data_git_hash = "82d0654c97e55a5b1ce70b2d14b4705dc266eb0d"
data_git_describe = "v0.0-1976-g82d0654c"
data_git_msg = """\
commit 82d0654c97e55a5b1ce70b2d14b4705dc266eb0d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 1 12:08:41 2021 +0000

    Don't automatically generate disassembly in the example Makefile
    
    Anyone who needs to disassemble their generated ELF can probably just
    call objdump directly and the precise set of flags have already
    confused at least one potential contributor[1].
    
    We're keeping the canned objdump command for "engineers that know
    where to look" because some have said they find it useful. Run it with
    e.g.
    
        make -C examples/sw/simple_system/hello_test disassemble
    
    [1] https://github.com/lowRISC/ibex/issues/1263

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
