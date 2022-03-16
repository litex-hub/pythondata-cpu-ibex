import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2303"
version_tuple = (0, 0, 2303)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2303")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2177"
data_version_tuple = (0, 0, 2177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2177")
except ImportError:
    pass
data_git_hash = "f7724adcc76bea0bd909c2ac28cf11226d5cbefe"
data_git_describe = "v0.0-2177-gf7724adc"
data_git_msg = """\
commit f7724adcc76bea0bd909c2ac28cf11226d5cbefe
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 11 17:10:02 2022 +0000

    [rtl] Move memory ECC checks and generation into core
    
    Previously integrity checks for incoming memory reads and integrity
    generation for outgoing memory writes were handled within ibex_lockstep
    and weren't duplicated.
    
    This moves the integrity checks and generation into the core so they are
    replicated and checked as part of the lockstep mechanism.
    
    Additionally it generates a bus error on any memory integrity check
    failure. This will result in Ibex taking an exception if any data read
    or instruction fetch has bad integrity.

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
