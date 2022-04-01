import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2329"
version_tuple = (0, 0, 2329)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2329")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2203"
data_version_tuple = (0, 0, 2203)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2203")
except ImportError:
    pass
data_git_hash = "fe3e029108d07aa6f032ad4a6c972c9609907d9e"
data_git_describe = "v0.0-2203-gfe3e0291"
data_git_msg = """\
commit fe3e029108d07aa6f032ad4a6c972c9609907d9e
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Apr 1 15:34:53 2022 +0200

    Update google_riscv-dv to google/riscv-dv@cb4295f
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision cb4295f9ce5da2881d7746015a6105adb8f09071
    
    * Update list search (Matthew Ballance)
    * Trap and report exceptions encountered in sub-processes and
      propagate error back (Matthew Ballance)
    * Workaround fix for loop test colon issue (aneels3)
    * Fix typo (aneels3)
    * Add support for RV64AFD (aneels3)
    * Fix typo (aneels3)
    * Update README.md (aneels3)
    * Add support for sub_programs (aneels3)
    * fix issue with imm value for 64 bit instr (aneels3)
    * Allow for underscores and capital letters in ISA for ISS (Pirmin
      Vogel)
    * implement rv64i (shrujal20)
    * Add support for RV32FD coverage (aneels3)
    * Integrate random seed for pyflow (aneels3)
    * Add riscv_loop_test (ShraddhaDevaiya)
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
