import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2098"
version_tuple = (0, 0, 2098)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2098")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2003"
data_version_tuple = (0, 0, 2003)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2003")
except ImportError:
    pass
data_git_hash = "8d37af2751a25cffd50d09d91845cf2c111f39b3"
data_git_describe = "v0.0-2003-g8d37af27"
data_git_msg = """\
commit 8d37af2751a25cffd50d09d91845cf2c111f39b3
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 5 15:49:41 2021 +0100

    Update google_riscv-dv to google/riscv-dv@59dcd8c
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision 59dcd8c813484eb6dcca67e7e36089fe772b9cc8
    
    * Update scripts for Metrics CI regression:  bug fixes, change ISS to
      spike in CI regression (Aimee Sutton)
    * Add illegal and load store instruction (aneels3)
    * Avoid generating hint instruction when RV32C is turned off
      (google/riscv-dv#787) (taoliug)
    * Fix illegal opcode issue in the cov_test (google/riscv-dv#786)
      (taoliug)
    * [questa] Remove -access=rwc from vlog command line arguments (Rupert
      Swarbrick)
    * [ci] temporarily disable CI flow (Udi Jonnalagadda)
    * fix issue with rcs for num_of_harts (aneels3)
    * fix multi-hart label issue (aneels3)
    * add multi_hart test (ishita71)
    * Fix minor issues (aneels3)
    * Add riscv_signature_pkg (aneels3)
    * add gen_signature_handshake (ishita71)
    * Add gen_interrupt_vector_table (aneels3)
    * Remove the unnecessary lines (Anil Sharma)
    * fix issue with riscv_rand_instr_test (aneels3)
    * Add multiprocessing code block (aneels3)
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
