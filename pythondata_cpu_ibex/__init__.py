import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2056"
version_tuple = (0, 0, 2056)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2056")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1967"
data_version_tuple = (0, 0, 1967)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1967")
except ImportError:
    pass
data_git_hash = "0cb2afffa9893444dc2979bb290fa2c08ac384d7"
data_git_describe = "v0.0-1967-g0cb2afff"
data_git_msg = """\
commit 0cb2afffa9893444dc2979bb290fa2c08ac384d7
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Feb 1 18:40:28 2021 +0000

    Update google_riscv-dv to google/riscv-dv@0b62525
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision 0b625258549e733082c12e5dc749f05aefb07d5a
    
    * Add a knob to use rounding mode from the instruction (google/riscv-
      dv#767) (taoliug)
    * Add rounding mode support for floating point arithmetic instructions
      (google/riscv-dv#766) (taoliug)
    * Fix syntax issue (google/riscv-dv#765) (taoliug)
    * Add riscv_amo_instr (aneels3)
    * convert string to enum type (ishita71)
    * Remove unintended errors in the coverage flow (google/riscv-dv#757)
      (taoliug)
    * Fix c_test handling in the YAML testlist (google/riscv-dv#756)
      (taoliug)
    * Add support for new Spike trace format (google/riscv-dv#755) (Daniel
      Bates)
    * Fix google/riscv-dv#751 for floating point coverage (Weicai Yang)
    * Fix issues with implemented TODO's (aneels3)
    * fix randomize_gpr (aneels3)
    * Add file riscv_b_instr.py (ishita71)
    * add std_randomize todo (pvipsyash)
    * Add todo for floating_point test (ShraddhaDevaiya)
    * Add scripts to integrate with Metrics regression platform (Aimee
      Sutton)
    
    Includes a fix to dv/uvm/core_ibex/sim.py to use `asm_test` rather than
    `asm_tests` due to changes in RISCV-DV
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post89"
tool_version_tuple = (0, 0, 89)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post89")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
