VCS_FLAGS += -full64 +v2k -timescale=1ns/1ns -sverilog +lint=TFIPC-L -debug_all
VCS_FGP_THREAD ?= 4


# randomize all undefined signals (instead of using X)
VCS_FLAGS += +vcs+initreg+random
# VCS_FLAGS += +define+RANDOMIZE_GARBAGE_ASSIGN
# VCS_FLAGS += +define+RANDOMIZE_INVALID_ASSIGN
# VCS_FLAGS += +define+RANDOMIZE_MEM_INIT
# VCS_FLAGS += +define+RANDOMIZE_REG_INIT
# manually set RANDOMIZE_DELAY to avoid VCS from incorrect random initialize
# NOTE: RANDOMIZE_DELAY must NOT be rounded to 0
# VCS_FLAGS += +define+RANDOMIZE_DELAY=1
VCS_FLAGS += +define+PRINTF_COND=1
VCS_FLAGS += +define+SIM_TOP_MODULE_NAME=tb_top

VCS_FLAGS += +define+PRINTF_COND_=1
VCS_FLAGS += +define+ASSERT_VERBOSE_COND_=1
VCS_FLAGS += +define+STOP_COND_=1

# Threads
VCS_FLAGS += -j ${THREADS}
# Fine-Grained Parallelism
VCS_FLAGS += -fgp
# top module to simlulate
VCS_FLAGS += -top ${TOPLEVEL}
# Enable fsdb dump for vcs compiler
VCS_FLAGS += -debug_access+all

ifeq ($(dump_enable), true)
	PLUSARGS += +dump_enable=1
	PLUSARGS += +dump_start_cycle=$(dump_start_cycyle)
endif

