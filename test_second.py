import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, Event, Lock
from cocotb.types import LogicArray, Logic, Range
from cocotb.binary import BinaryValue

@cocotb.test()
async def First_test(dut):
    # Create a 1ns period clock on dut's port clock
    clock = Clock(dut.clock, 10, units="ns")
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    dut.io_in.value = 0

    await RisingEdge(dut.clock)
    for i in range(0, 5):
        dut.io_in.value = i
        print(dut.io_out.value.integer)
        # assert dut.io_out.value.integer == i
        await RisingEdge(dut.clock)
    print(dut.io_out.value.integer)