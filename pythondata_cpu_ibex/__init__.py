import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2430"
version_tuple = (0, 0, 2430)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2430")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2302"
data_version_tuple = (0, 0, 2302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2302")
except ImportError:
    pass
data_git_hash = "223f7cd25b4da7a1d6044e66eea6b37b2940f7a0"
data_git_describe = "v0.0-2302-g223f7cd2"
data_git_msg = """\
commit 223f7cd25b4da7a1d6044e66eea6b37b2940f7a0
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue May 24 15:28:29 2022 +0200

    Update google_riscv-dv to google/riscv-dv@cc4b870
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision cc4b87057cb38c91cb0c2ecb065e38281df7aa97
    
    * Fix google/riscv-dv#857 (aneels3)
    * [euvm] Fixed a typo in the README file (Puneet Goel)
    * [euvm] updated the README file (Puneet Goel)
    * [euvm] Moved euvm specific README to euvm folder (Puneet Goel)
    * [euvm] ported some SV updates (Puneet Goel)
    * [euvm] Fixed generated ASM code indentation (Puneet Goel)
    * Add support for RV64IMC instr coverage (aneels3)
    * Add register definitions for privilege spec 1.12 and debug spec
      1.0.0 (Henrik Fegran)
    * Updated README note for EUVM (Puneet Goel)
    * Use current date in output folder name (Puneet Goel)
    * Try to create output file folder if it does not exist (Puneet Goel)
    * Added a readme for EUVM port (Puneet Goel)
    * Allow providing a randomization seed from command line (Puneet Goel)
    * Make merging of directed instruction streams scalable (Puneet Goel)
    * Create and use new class riscv_prog_instr_stream (Puneet Goel)
    * Added and used append and prepend functions for instr_list (Puneet
      Goel)
    * Added new targets and tests (Puneet Goel)
    * Expose riscv instruction classes in the riscv gen package (Puneet
      Goel)
    * Use mixin templates to create RISCV instruction classes (Puneet
      Goel)
    * Fix a bug in asm section tag generation (Puneet Goel)
    * EUVM upgrade for bitmanip (Puneet Goel)
    * Use new clog2 implemented in esdl.data.bvec module (Puneet Goel)
    * Add debug and clean targets to Makefile (Puneet Goel)
    * Use Queue functions in place of array concatenation (Puneet Goel)
    * Misc fixes after review (Puneet Goel)
    * Fix broken run.py script (Puneet Goel)
    * Use more verbose naming in main function in the test (Puneet Goel)
    * Removed some redundant code comments (Puneet Goel)
    * Allow verbosity and instr count specification from make run command
      (Puneet Goel)
    * Handle riscv_loop_instr confliting constraint in post_randomize
      (Puneet Goel)
    * Use variable names that do not conflict with outers (Puneet Goel)
    * Use constraint in place of Constraint (Puneet Goel)
    * Fixed a typo where '-' was getting printed in place of ' ' (Puneet
      Goel)
    * Pick urandom from new location -- esdl.base.rand (Puneet Goel)
    * Fixed an issue where newline character was not getting added to some
      instructions (Puneet Goel)
    * Fixed an issue with sup program generation (Puneet Goel)
    * Added EUVM riscv_instr_base_test (Puneet Goel)
    * Added EUVM riscv_instr_register module (Puneet Goel)
    * Moved EUVM files to euvm folder (Puneet Goel)
    * Add makefile command to to run a test (Puneet Goel)
    * Cast return value from ceil to integer (Puneet Goel)
    * Miscelleneous fixes (Puneet Goel)
    * Fixed some issues in riscv_loop_instr (Puneet Goel)
    * Use variable for setting rand_mode (Puneet Goel)
    * Use false in place of '0' for bools (Puneet Goel)
    * Added build makefile (Puneet Goel)
    * misc fixes (Puneet Goel)
    * Added riscv instruction definitions (Puneet Goel)
    * Added euvm module riscv_instr_registry (Puneet Goel)
    * Added euvm module riscv_data_page_gen (Puneet Goel)
    * Added euvm module riscv_privileged_common_seq (Puneet Goel)
    * Added euvm module riscv_debug_rom_gen (Puneet Goel)
    * Use urandom!bool in place of inappropriately named function toss
      (Puneet Goel)
    * Added euvm module riscv_illegal_instr (Puneet Goel)
    * Added euvm module riscv_asm_program_gen (Puneet Goel)
    * Use esdl.rand: toss instead os uniform(0, 2) (Puneet Goel)
    * Fixed randomization of avail_regs in euvm module riscv_instr_stream
      (Puneet Goel)
    * Use esdl.rand: shuffle instead of randomShuffle (Puneet Goel)
    * Added euvm module riscv_directed_instr_lib (Puneet Goel)
    * added euvm module riscv_load_store_instr_lib (Puneet Goel)
    * urandom has moved to package esdl.rand (Puneet Goel)
    * Added euvm module riscv_instr_sequence (Puneet Goel)
    * Added euvm module riscv_amo_instr_lib (Puneet Goel)
    * Added euvm module riscv_instr_stream (Puneet Goel)
    * A small fix in riscv_pmp_cfg module (Puneet Goel)
    * Added euvm module riscv_loop_instr (Puneet Goel)
    * Added euvm module riscv_pseudo_instr (Puneet Goel)
    * Added euvm module riscv_vector_instr (Puneet Goel)
    * Added euvm module riscv_floating_point_instr (Puneet Goel)
    * Added euvm module riscv_b_instr (Puneet Goel)
    * Added euvm module isa/riscv_compressed_instr (Puneet Goel)
    * Added euvm module isa/riscv_amo_instr (Puneet Goel)
    * Added euvm module isa/riscv_instr (Puneet Goel)
    * Added euvm module riscv_callstack_gen (Puneet Goel)
    * Added euvm module riscv_page_table_list (Puneet Goel)
    * Used ranged switch case statements where required (Puneet Goel)
    * Added euvm module riscv_privil_reg (Puneet Goel)
    * Add @UVM_DEFAULT uda on the class members where required (Puneet
      Goel)
    * Added euvm module riscv_reg (Puneet Goel)
    * Added euvm module riscv_pmp_cfg (Puneet Goel)
    * Added euvm module riscv_vector_cfg (Puneet Goel)
    * Added euvm module riscv_page_table_exception_cfg (Puneet Goel)
    * Added euvm module riscv_page_table_entry (Puneet Goel)
    * Added euvm module riscv_page_table (Puneet Goel)
    * Added riscv_core_setting module (Puneet Goel)
    * Added new file riscv_instr_gen_config (Puneet Goel)
    * Fixed some module imports (Puneet Goel)
    * Added new file riscv_signature_pkg (Puneet Goel)
    * Added D port of riscv_instr_pkg (Puneet Goel)
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
