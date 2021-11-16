import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2215"
version_tuple = (0, 0, 2215)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2215")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2103"
data_version_tuple = (0, 0, 2103)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2103")
except ImportError:
    pass
data_git_hash = "b66f199151b509eb975d2c3f19affdd7b80de7a8"
data_git_describe = "v0.0-2103-gb66f1991"
data_git_msg = """\
commit b66f199151b509eb975d2c3f19affdd7b80de7a8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 5 12:35:08 2021 +0100

    Update lowrisc_ip to lowRISC/opentitan@ad629e3e6
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    ad629e3e6e70c5eaa3c2dd68457b0a020448b35f
    
    * [dvsim] Introduce {self_dir} as variable (Philipp Wagner)
    * [dvsim] Small cleanups (Philipp Wagner)
    * [prim_lfsr] Minor lint fix (Michael Schaffner)
    * [dv] Update sec_cm testplan (Weicai Yang)
    * [prim/lint] Move waiver to correct waiver file (Michael Schaffner)
    * [prim_assert] Relocate waivers to dedicated prim_assert.waiver file
      (Michael Schaffner)
    * [alert_handler] Lint fixes and waiver updates (Michael Schaffner)
    * [prim_lc_receiver] Add parameter to select reset value (Michael
      Schaffner)
    * [lint] Add lint waiver for IP regfiles with shadow resets (Michael
      Schaffner)
    * [fpv] Fix Verible lint errors (Philipp Wagner)
    * [prim_lfsr] Minor lint fixes (Timothy Chen)
    * [clkmgr] Fix measurement control CDC (Timothy Chen)
    * [fpv/prim_counter] Pad one bit to include overflow case (Cindy Chen)
    * [fpv] Fix issue lowRISC#8371 (Zeeshan Rafique)
    * [flash_ctrl] Flash ctrl security hardening (Timothy Chen)
    * [dv] Fix CI error (Cindy Chen)
    * [prim_alert_*] Extend SVAs for FPV (Michael Schaffner)
    * [prim_alert_*] Update DV TB to respect initialization timing
      (Michael Schaffner)
    * [prim_alert_rxtx_fpv] Update FPV environment and fix SVAs (Michael
      Schaffner)
    * [prim_alert_sender] Update sender to support in-band reset mechanism
      (Michael Schaffner)
    * [prim_alert_sender] Simplify sender and clear ping req upon sigint
      (Michael Schaffner)
    * [prim_lc_sender] Add option to select reset value (Michael
      Schaffner)
    * [prim] Correct assertion valid term (Timothy Chen)
    * [prim_lc_combine] Align behavior of lc combine with mubi functions
      (Michael Schaffner)
    * [fpv/tool] Support GUI mode on dvsim (Cindy Chen)
    * [prim_lfsr] Further permutation refinements for SBox layer (Michael
      Schaffner)
    * [dv/shadow_reg] Shadow register write by field (Cindy Chen)
    * [prim] Fix the edge type (Eunchan Kim)
    * [checklist] Updates to checklist for D2 status (Tom Roberts)
    * [prim_mubi_pkg] Add a generic multibit type and associated functions
      (Michael Schaffner)
    * [prim] Minor fix and clarification to prim_count (Timothy Chen)
    * [keymgr/dv] Update testplan and covergroup plan (Weicai Yang)
    * [prim_lc_combine] Fix parameterization error (Michael Schaffner)
    * [fpv/prim_count] Small update on prim_count assertions (Cindy Chen)
    * [dv] Add ip_name in reg_block (Weicai Yang)
    * [keymgr] Finalize keymgr hardening (Timothy Chen)
    * [prim_lc_combine] Add a prim to compute logical AND/OR for LC
      signals (Michael Schaffner)
    * [dv] Remove common_cov_excl.el from unr.cfg (Weicai Yang)
    * [dv/top_level] Loop through the SW test multiple times (Cindy Chen)
    * [flash_ctrl] Various clean-up and updates (Timothy Chen)
    * [prim] Change prim_reg_cdc assertions (Timothy Chen)
    * [prim, keymgr] Migrate keymgr_cnt to prim_count (Timothy Chen)
    * [sw dv] Multi-site support for Verilator (Martin Lueker-Boden)
    * [dv/csr] Update write exclusion wdata value (Cindy Chen)
    * [dv/dv_base_reg] remove debug display (Cindy Chen)
    * [dv/shadow_reg] Fix alert shadow_reg regression error (Cindy Chen)
    * [top] Integrate ast into fpga (Timothy Chen)
    * [prim_lfsr] Improve statistics of non-linear output (Michael
      Schaffner)
    * [prim_esc_receiver] Fix response toggling corner case (Michael
      Schaffner)
    * option to use partner ast_pkg (Sharon Topaz)
    * [dv/prim_esc] Double the ping timeout cycles (Cindy Chen)
    * [dv] Use sed to add -elfile for each excl file (Weicai Yang)
    * [dv] Fix coverage report error (Weicai Yang)
    * [dv] Update common exclusion file (Weicai Yang)
    * [dv/prim_esc] Improve FSM coverage (Cindy Chen)
    * [reggen] Add a check to limit the swaccess type for shadow regs
      (Michael Schaffner)
    * [prim_subreg_shadow] Fix for W1S/W0C corner case (Michael Schaffner)
    * [prim_subreg_shadow] Disallow phase updates when storage err is
      present (Michael Schaffner)
    * [dvsim] Add passing count by milestone in reports (Srikrishna Iyer)
    * [dv/tool] Include toggle coverage for prim_alert_sender in
      cover_reg_top (Cindy Chen)
    * [clkmgr] Harden clock manager through frequency measurements
      (Timothy Chen)
    * [dv] Only enable VCS -kdb when dumping waves (Weicai Yang)
    * [dv] Fix shadow reg (Weicai Yang)
    * [dvsim] Allow non-integral values of --reseed-multiplier (Rupert
      Swarbrick)
    * [ast] Fixes for various ast issues (Timothy Chen)
    * [prim_esc_receiver] Assert escalation in case of sigint error
      (Michael Schaffner)
    * [prim_esc_receiver] Minor signal renaming for consistency (Michael
      Schaffner)
    * [dv/alert_handler] Support shadow register sequence (Cindy Chen)
    * [verilator] Use FileSz rather than MemSz when flattening ELF files
      (Michael Munday)
    * [prim_subreg_shadow] Only assert QE when committed_reg is written
      (Michael Schaffner)
    * [dv,verilator] Round up SV_MEM_WIDTH_BYTES to a multiple of 4
      (Rupert Swarbrick)
    * [prim] Add missing include (Pirmin Vogel)
    * [dv/cover_cfg] Exclude prim_alert/esc from xcelium (Cindy Chen)
    * [dv/cover_cfg] Exclude prim_alert/esc pairs (Cindy Chen)
    * [clkmgr] Use local BUFHCE clock gates on FPGA (Pirmin Vogel)
    * [prim_prince] Mark "leaf" functions in prince_ref.h as static inline
      (Rupert Swarbrick)
    * [dv/shadow_reg] Check status after shadow_reg write (Cindy Chen)
    * [dv/shadwo_reg] Shadow reg common sequence update (Cindy Chen)
    * [otp_ctrl/lc_ctrl] Add 32bit OTP vendor test ctrl/status regs to LC
      TAP (Michael Schaffner)
    * [otp_ctrl] Add VENDOR_TEST partition (Michael Schaffner)
    * [prim] Edge Detector (Eunchan Kim)
    * [prim_diff_decode] Fix asynchronous assertions (Michael Schaffner)
    * [spi_device] Instantiate Upload module (Eunchan Kim)
    * [dv] Add sv_flist_gen_flags HJson var for FuseSoc (Srikrishna Iyer)
    * [dv, xcelium] Properly pass excl files to IMC (Srikrishna Iyer)
    * [reg] Fix shadow reg update during storage error (Timothy Chen)
    * [regfile] Refactor cdc handling to the reg level (Timothy Chen)
    * [dv/prim_esc] Add a testplan and increase coverage (Cindy Chen)
    * [dv] Update TLUL and EDN frequency (Weicai Yang)
    * [rstmgr, top] Add support for shadow resets (Timothy Chen)
    * [dv] Update Xcelium cover ccf (Srikrishna Iyer)
    * [dv] reduce seeds for CSR tests (Weicai Yang)
    * [usb/top] Remove AND gates on non-AON domain and rename 3.3V signal
      (Michael Schaffner)
    * [dv/prim_alert] Improvement on prim_alert tb (Cindy Chen)
    * [prim] FIFO SRAM Adapter fix (Eunchan Kim)
    * [prim] Add Write Mask port (Eunchan Kim)
    * [dv] Fix timescale issue with Xcelium (Weicai Yang)
    * [dv/prim_esc] Fix prim_esc regression error (Cindy Chen)
    * [dv/dv_base_reg] change from uvm_low to uvm_high (Cindy Chen)
    * [sram_ctrl] Harden initialization counter (Michael Schaffner)
    * [tools/uvmdvgen] Fix path in testplan inclusion (Guillermo Maturana)
    * [dv] Change stress_all_with_rand_reset to V3 (Weicai Yang)
    * [dv] fix tl error coverage (Weicai Yang)
    * [dv] Add macro DV_GET_ENUM_PLUSARG (Weicai Yang)
    * [prim] SRAM Async FIFO (Eunchan Kim)
    * [dv, xcelium] Fix statement coverage extraction (Srikrishna Iyer)
    * [dvsim] Minor fixes to coverage extraction (Srikrishna Iyer)
    * [prim_lfsr] Do not shadow |state| variable (Philipp Wagner)
    * [prim] Add non-linear out option to prim_lfsr (Timothy Chen)
    * [dv] Constrain TLUL to 24Mhz or higher (Weicai Yang)
    * [primgen] Instantiate tech libs in stable order (Philipp Wagner)
    * [primgen] Actually find the Verible Python wrapper (Philipp Wagner)
    * [dv/prim_esc] fix regression error (Cindy Chen)
    * [dv] Fix shadow reg predict (Weicai Yang)
    * [dv/common] Exclude assertion coverage from IP level testbench
      (Cindy Chen)
    * [dv/prince] hit additional toggle coverpoints (Udi Jonnalagadda)
    * [sram_ctrl] Update docs (Michael Schaffner)
    * [sram_ctrl] Absorb prim_ram_1p_scr (Michael Schaffner)
    * [dv/prim_alert/esc] Improvements for prim_alert/esc_tb (Cindy Chen)
    * [dv/dvsim] Add "testfile" grading option (Guillermo Maturana)
    * [dv/prim_esc] Direct test for prim_rx/tx (Cindy Chen)
    * [dv/utils] added 6MHz to clk_freq_mhz_e (Dror Kabely)
    * [prim_xor2/lint] Add waiver for .* use in generated prim (Michael
      Schaffner)
    * [dv, doc] Replace all 'dv.plan' with testplan (Srikrishna Iyer)
    * Fix the testplan link in dvsim code (Srikrishna Iyer)
    * [dv/dsim] Add dsim workaround for issue 242 (Guillermo Maturana)
    * [util, reggen] Support standardized cdc handling for regfile
      (Timothy Chen)
    * [dv/shadow_reg] Align shadow_reg field update behavior (Cindy Chen)
    * [dvsim] Fix publish report summary typo (Cindy Chen)
    * [rtl/prim_alert_sender] Allow ping_req to stay high without error
      (Cindy Chen)
    * [dvsim] Separate publish report from dvsim flow [PART3] (Cindy Chen)
    * [dv/prim_alert] Add a testbench for prim_alert (Cindy Chen)
    * [otp_ctrl] Connect test-related GPIO signal (Michael Schaffner)
    * [prim_subreg_shadow] Make local parameter a localparam (Philipp
      Wagner)
    * [prim_subreg] Make software access type an enum (Philipp Wagner)
    * [rtl/prim_diff_decode] Add prim_flop_2sync dependency (Cindy Chen)
    * [otp_ctrl] Update AscentLint waiver file (Michael Schaffner)
    * [edn] Add MaxLatency assertion (Eunchan Kim)
    * [prim_subreg_shadow] Correct write data signal usage (Michael
      Schaffner)
    * [script/dvsim] Separate publish report from dvsim flow [PART2]
      (Cindy Chen)
    * [prim_lfsr] Fix assertion issue occuring right after reset (Michael
      Schaffner)
    * [dv/shadow_reg] Handle CSR automated sequence write abort (Cindy
      Chen)
    * [dv/dv_lib] Add post_apply_reset for extra delay (Guillermo
      Maturana)
    * [dv] Add function coverage plan for tl_errors, tl_intg_err (Weicai
      Yang)
    * [dv] Remove tl_intg_err in top-level and increase seeds for
      tl_intg_err (Weicai Yang)
    * [dv/shadow_reg] Fix alert shadow reg regression error (Cindy Chen)
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
