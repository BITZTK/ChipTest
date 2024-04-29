# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
SIM ?= vcs
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/dut/Passthrough.v
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = Passthrough

# MODULE is the basename of the Python test file
MODULE = test_First

THREADS ?= 64

PLUSARGS += +dump_enable=1
PLUSARGS += +dump_start_cycle=0
PLUSARGS += +dump_fsdb


# Enable fsdb dump for vcs compiler
VCS_FLAGS += -debug_access+all
COMPILE_ARGS += ${VCS_FLAGS}


# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

# verdi -ssf <wavefile>