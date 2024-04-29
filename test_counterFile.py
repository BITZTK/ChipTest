import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, Event, Lock
from cocotb.types import LogicArray, Logic, Range
from cocotb.binary import BinaryValue


async def dut_reset(dut, cycles):
    posedge = RisingEdge(dut.clock)
    dut.reset.value = 1
    for _ in range(0, cycles):
        await posedge
    dut.reset.value = 0
    print(f"cycles = {dut.cycles.value.integer}")
    await posedge
    print(f"cycles = {dut.cycles.value.integer}")
    print("Start reset")


async def dut_posedge(dut, cycles):
    posedge = RisingEdge(dut.clock)
    for _ in range(0, cycles):
        await posedge


@cocotb.test()
async def testCounterFile(dut):
    # Create a 1ns period clock on dut's port clock
    clock = Clock(dut.clock, 1, units="ns")
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await dut_reset(dut, 5)

    print(f"cycles = {dut.cycles.value.integer}")

    print("Start main")

    posedge = RisingEdge(dut.clock)
    # await posedge
    for i in range(0, 5):
        print(f"i = {i}, out1 = {dut.io_out1.value.integer}, out2 = {dut.io_out2.value.integer}, cycles = {dut.cycles.value.integer}")
        await posedge
    print(f"cycles = {dut.cycles.value.integer}")
    await posedge
    print(f"cycles = {dut.cycles.value.integer}")
    print("Completed!!!")
