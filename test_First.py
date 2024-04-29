import cocotb
from cocotb.clock import Clock 
from cocotb.triggers import RisingEdge,Timer,Event,Lock
from cocotb.types import LogicArray,Logic,Range 
from cocotb.binary import BinaryValue

@cocotb.test()
async def First_test(dut):
    clock=Clock(dut.clock,10,units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    dut.io_in.value=0

    await RisingEdge(dut.clock)
    for i in range(0,7):
        dut.io_in.value=i
        if 'x' not in dut.io_out.value.binstr:
            print(dut.io_out.value.integer)
        else:
            print("dut.io_out contains 'x', value: {}".format(dut.io_out.value.binstr))

        # print(dut.io_out.value.integer)
        await RisingEdge(dut.clock)
        # if(i==5):
        #     break
    print(dut.io_out.value.integer)