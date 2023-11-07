"""
This file is executed by labscript before the connection table is saved to the
hdf5 file. It is used to define the experiment shot, and to add any
device-specific information to the connection table.
"""
from labscript import start, stop, add_time_marker, AnalogOut, DigitalOut
from labscript_devices.DummyPseudoclock.labscript_devices import DummyPseudoclock
from labscript_devices.DummyIntermediateDevice import DummyIntermediateDevice
from labscript_devices.FunctionRunner.labscript_devices import FunctionRunner


# Use a virtual, or 'dummy', device for the psuedoclock
DummyPseudoclock(name="pseudoclock")

# An output of this DummyPseudoclock is its 'clockline' attribute, which we use
# to trigger children devices
DummyIntermediateDevice(name="intermediate_device", parent_device=pseudoclock.clockline)

# Create an AnalogOut child of the DummyIntermediateDevice
AnalogOut(name="analog_out", parent_device=intermediate_device, connection="ao0")

# Create a DigitalOut child of the DummyIntermediateDevice
DigitalOut(
    name="digital_out", parent_device=intermediate_device, connection="port0/line0"
)

# create a FunctionRunner child of the DummyIntermediateDevice
FunctionRunner(name="function_runner")

# The following is standard boilerplate necessary for the file to compile
if __name__ == '__main__':

   start()

   stop(1)