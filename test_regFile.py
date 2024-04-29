import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, Event, Lock
from cocotb.types import LogicArray, Logic, Range
from cocotb.binary import BinaryValue


async def coroutine1():
    print("Coroutine 1 started")
    await cocotb.triggers.Timer(5, 'ns')
    print("Coroutine 1 completed")


async def coroutine2():
    print("Coroutine 2 started")
    await cocotb.triggers.Timer(3, 'ns')
    print("Coroutine 2 completed")


async def wait_10ns():
    cocotb.log.info("About to wait for 10 ns")
    await Timer(10, units='ns')
    cocotb.log.info("Simulation time has advanced by 10 ns")


async def coro_inner():
    cocotb.log.info("About to wait for 1 ns")
    await Timer(1, units='ns')
    cocotb.log.info("Simulation time has advanced by 1 ns")
    return "Hello World"


async def coro_event1(event: Event):
    cocotb.log.info("Coroutine 1 waiting for the event")
    await event.wait()
    cocotb.log.info("Coroutine 1 received the event")


async def coro_event2(event: Event):
    print("Coroutine 2 waiting for 2 seconds")
    await cocotb.triggers.Timer(2, units='ms')
    print("Coroutine 2 setting the event")
    event.set()


async def coroutine1_lock(lock):
    print("Coroutine 1 trying to acquire the lock")

    # 尝试获取锁
    await lock.acquire()

    try:
        print("Coroutine 1 acquired the lock")
        # 在这里可以执行受保护的操作
    finally:
        # 释放锁
        lock.release()
        print("Coroutine 1 released the lock")


async def coroutine2_lock(lock):
    print("Coroutine 2 trying to acquire the lock")

    # 尝试获取锁
    await lock.acquire()

    try:
        print("Coroutine 2 acquired the lock")
        # 在这里可以执行受保护的操作
    finally:
        # 释放锁
        lock.release()
        print("Coroutine 2 released the lock")


@cocotb.test()
async def regFile_simple_test(dut):
    # Assert initial output is unknown
    # assert LogicArray(dut.io_in_b.value) == LogicArray("X")

    # Set initial input value to prevent it from floating
    dut.io_in_a.value = 0
    dut.io_in_b.value = 0

    # Creat a 10us period clock on port clock
    clock = Clock(dut.clock, 10, units="us")
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    # Synchronize with the clock. This will regisiter the initial `io_in_a` `io_in_b` value
    # await RisingEdge(dut.clock)
    expected_val = 0  # Matches initial input value
    for i in range(10):
        print(f"i = {i}")
        dut.io_in_a.value = i
        dut.io_in_b.value = i
        await RisingEdge(dut.clock)
        print(dut.io_out.value.integer, type(dut.io_out.value))
        assert dut.io_out.value.integer == (2 * i) % 16

    await RisingEdge(dut.clock)

    # print("Main coroutine started")
    # await cocotb.start(coroutine1())
    # await cocotb.start(coroutine2())
    # print("Main coroutine completed")
    # await cocotb.triggers.Timer(6, 'ns')

    # print("Main coroutine started")
    # await cocotb.start_soon(coroutine1())
    # await cocotb.start_soon(coroutine2())
    # print("Main coroutine completed")
    # await cocotb.triggers.Timer(6, 'ns')

    # for i in range(10):
    #     print(f"wait start {i}")
    #     await wait_10ns()
    #     print(f"wait finish {i}")

    # task = cocotb.start_soon(coro_inner())
    # result = await cocotb.triggers.Join(task)
    # print(f"result = {result}")
    # assert result == "Hello World"

    # my_event = Event()
    # await cocotb.start(coro_event1(my_event))
    # await cocotb.start(coro_event2(my_event))
    # await cocotb.triggers.Timer(5, units='ms')
    # print("xmy")

    # my_lock = Lock()
    #
    # await cocotb.start(coroutine1_lock(my_lock))
    # await cocotb.start(coroutine2_lock(my_lock))
    #
    # await cocotb.triggers.Timer(5, units='ns')

    # vec = BinaryValue(n_bits=7, bigEndian=False)
    # vec.integer = 42
    # print(vec.binstr)
    # print(vec.value)
    # print(vec.n_bits)
    # print(vec.buff)

    # lg = Logic("X")
    # lg1 = Logic(0)
    # lg2 = Logic(1)
    # print(lg)
    # lg3 = lg1 ^ lg2
    # lg4 = lg1 & lg2
    # print(type(lg3), lg3)
    # print(type(lg4), lg4)

    # r = Range(1, 'to', 0)
    # print(r.left, r.right, r.direction, len(r))
    # print(r)
