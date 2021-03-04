import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2070"
version_tuple = (0, 0, 2070)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2070")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1979"
data_version_tuple = (0, 0, 1979)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1979")
except ImportError:
    pass
data_git_hash = "5ef18f0b789b9e09f76863b42db20e22a3779e7e"
data_git_describe = "v0.0-1979-g5ef18f0b"
data_git_msg = """\
commit 5ef18f0b789b9e09f76863b42db20e22a3779e7e
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Wed Mar 3 10:48:44 2021 +0000

    Update lowrisc_ip to lowRISC/opentitan@6cc5c164b
    
    NOTE this commit includes various changes to align the Ibex repo with
    changes upstream in OT!
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    6cc5c164ba96d339f06cbcede0d17d2c96ce3c05
    
    * [dv] Add SV_FCOV_SVA back (Srikrishna Iyer)
    * [DV][FCOV] Minor updates to lowRISC/opentitan#5414 (Srikrishna Iyer)
    * [dvsim] Fix --cov + --build|run-only bugs (Srikrishna Iyer)
    * [lint] Waivers for rv_core_ibex lint (Greg Chadwick)
    * [lint] Allow one branch in unique case (Greg Chadwick)
    * [dv/macros] Add fcov macros from Ibex (Tom Roberts)
    * [dvsim/verilator] Fix pre-build cmd failure when hw/foundry is
      absent (Michael Schaffner)
    * [verilator/otp] Enable OTP preloading in verilator (Michael
      Schaffner)
    * [dvsim] Use builtins wherever possible (Srikrishna Iyer)
    * [prim] Avoid an apparent combinatorial loop in prim_secded_*_dec.sv
      (Rupert Swarbrick)
    * [dv/shadow_reg] Fix aes shadow reg error (Cindy Chen)
    * [lint] Remove comportable waivers from non-comportable IPs (Michael
      Schaffner)
    * [dv] Fix VPD dumping (Srikrishna Iyer)
    * [prim] Waive Verilator lint warning in prim_lfsr.sv (Pirmin Vogel)
    * [dv] Hard code various dv connections until full hook-up (Timothy
      Chen)
    * [tlul] Add payload checker and generator on device side only.
      (Timothy Chen)
    * [prim_packer] Silence verilator width warnings (Rupert Swarbrick)
    * [dvsim] lint fixes to FlowCfg (Srikrishna Iyer)
    * [dvsim] Minor improvement to FlowCfg (Srikrishna Iyer)
    * [dvsim] lint fixes to Scheduler (Srikrishna Iyer)
    * [dvsim] Very small update to Timer. (Srikrishna Iyer)
    * [lint] Update Verible lint parser to detect Verible syntax errors
      (Michael Schaffner)
    * [lint] Spot errors in the lint flow that we weren't expecting
      (Rupert Swarbrick)
    * [lint] Remove Fusesoc-related message waivers (Michael Schaffner)
    * [top / rst] Adjust the way rst_ni is used in design (Timothy Chen)
    * [dvsim/syn] Update parsing script and area reporting (Michael
      Schaffner)
    * [dv/regwen] update REGWEN conventions (Cindy Chen)
    * [dv/tools] Bug fix to common.tcl tb_top section. (Eitan Shapira)
    * [dv] Fix stress_all with reset (Weicai Yang)
    * [prim] Add a new slow to fast clock synchronizer (Tom Roberts)
    * [prim] Minor lint fix (Tom Roberts)
    * [tlul] Add instruction type to tlul (Timothy Chen)
    * [top] Ast updates (Timothy Chen)
    * [lint] Increase threshold for max number of bits in an array
      (Michael Schaffner)
    * [dv] add dv_base_reg_pkg to env_pkg template (Udi Jonnalagadda)
    * [dv/verilator] Ignore foundry dir (Srikrishna Iyer)
    * [dv] Provide license diagnostic info for VCS (Srikrishna Iyer)
    * [prim/otp_ctrl] Fix ECC correctable bug in generic OTP wrapper
      (Michael Schaffner)
    * [prim_ram_1p_scr] Make parity and diffusion layer settings more
      flexible (Michael Schaffner)
    * [prim] fix flash sram adapter use for configuration space (Timothy
      Chen)
    * [dv] Make CSR fields randomizable by default. (Srikrishna Iyer)
    * [dv/prim] minor updates (Udi Jonnalagadda)
    * [top] Minor lint fixes (Timothy Chen)
    * [prim_flash] Flash port alignments (Michael Schaffner)
    * [prim_util_pkg] Fix DC warning in _clog2() (Philipp Wagner)
    * Add missing full_o output signal of prim_fifo_sync (Philipp Wagner)
    * [dv] Gracefully kill simulation (Srikrishna Iyer)
    * [dv] Minor updates to prim tbs (Srikrishna Iyer)
    * [flash / top] Minor edits based on reviews (Timothy Chen)
    * [flash_ctrl / top] Various functional updates to flash (Timothy
      Chen)
    * [dv/otp_ctrl] regwen sequence (Cindy Chen)
    * [prim] Wire up full_o sync fifo output port in prim_sram_arbiter
      (Rupert Swarbrick)
    * [dvsim] Generate FUSESOC_IGNORE at top of scratch root (Rupert
      Swarbrick)
    * Revert "[lint] Remove Fusesoc-related message waivers" (Michael
      Schaffner)
    * Revert "[lint] Rename tool warnings to flow warnings and reduce
      their severity" (Michael Schaffner)
    * Revert "[lint] Provision syntax error filter for Verible lint"
      (Michael Schaffner)
    * [prim] Update fifo behavior during reset (Timothy Chen)
    * [dv] Move cip related macros to cip_macros (Weicai Yang)
    * [dv/dvsim] Fix when next_item does not have dependency (Cindy Chen)
    * [prim_packer_fifo/rtl] reset to disable output controls (Mark
      Branstad)
    * [lint] Provision syntax error filter for Verible lint (Michael
      Schaffner)
    * [lint] Rename tool warnings to flow warnings and reduce their
      severity (Michael Schaffner)
    * [lint] Remove Fusesoc-related message waivers (Michael Schaffner)
    * [dv/dvsim] collect coverage in scheduler (Cindy Chen)
    * [dvsim] Fix Syn class (Michael Schaffner)
    * [dv/shadow_reg] move get_shadow_regs function to dv_base_ral_block
      (Cindy Chen)
    * [lc_ctrl] Switch ECC to standard Hamming code (Michael Schaffner)
    * [prim_ram_*p_adv/prim_otp] Add option to use standard Hamming ECC
      (Michael Schaffner)
    * [secded_gen] Fix template bug that results in lint error (Michael
      Schaffner)
    * [prim/fifo_async] Disallow non-power-of-two depths (Tom Roberts)
    * [dv/alert] update shadow_reg alert naming in DV (Cindy Chen)
    * [dv] Align csr::reset_asserted to actual reset pin (Weicai Yang)
    * [prim_secded*_fpv] Generate FPV testbenches (Michael Schaffner)
    * [prim_secded*] Regenerate all SECDED primitives (Michael Schaffner)
    * [secded_gen] Add ability to generate FPV TB's and correct Hamming
      code (Michael Schaffner)
    * [dvsim] Run cov_merge / cov_report as part of the main set of jobs
      (Rupert Swarbrick)
    * [dvsim] Get rid of Deploy's static dispatch_counter (Rupert
      Swarbrick)
    * [dvsim] Make the scheduling logic per-target (Rupert Swarbrick)
    * [dvsim] Remove "status" from Deploy items (Rupert Swarbrick)
    * [dvsim] Create jobs with dependencies instead of sub-jobs (Rupert
      Swarbrick)
    * [dvsim] Simplify SimCfg._gen_results (Rupert Swarbrick)
    * [dvsim] Factor deploy method out of Deploy object (Rupert Swarbrick)
    * [dvsim] Move time tracking into its own class in Deploy.py (Rupert
      Swarbrick)
    * [dvsim] Fix printing of Deploy objects (Rupert Swarbrick)
    * [dv] make dv_macros.svh more UVM_agnostic (Srikrishna Iyer)
    * [dv/prim] reduce smoke test iterations (Udi Jonnalagadda)
    * [dv/hmac] reduce runtime for sha_vector test in smoke regression
      (Cindy Chen)
    * [DV] Enable cov comp creation iff cov is enabled (Srikrishna Iyer)
    * [prim_alert] Fix xcelium compile error (Cindy Chen)
    * [alert_rxtx/fpv] Update alert sender FPV testbenches (Michael
      Schaffner)
    * [alert_rxtx] Add option to latch fatal alert in alert sender
      (Michael Schaffner)
    * [kmac/dv] KMAC smoke test (Udi Jonnalagadda)
    * [dv/str_utils_pkg] add byte_to_str function (Udi Jonnalagadda)
    * [prim] - Add new prim_lc_dec (Jacob Levy)
    * [util] Move design-related helper scripts to util/design (Michael
      Schaffner)
    * [prim-flash] Add missing deps (Srikrishna Iyer)
    * [dv] Define SIMULATION during DV sims (Michael Schaffner)
    * [dv] Fix a typo in tb.sv.tpl (Weicai Yang)
    * Cleanup: Remove executable bits from source files (Philipp Wagner)
    * [dv] Use separate clock for EDN (Weicai Yang)
    * [dv] Add macro DV_EDN_IF_CONNECT to simplify EDN connect in TB
      (Weicai Yang)
    * [dv] Fix typo in clk_rst_if (Weicai Yang)
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
