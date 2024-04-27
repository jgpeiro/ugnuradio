from top_block import TopBlock
from device_source import DeviceSource
from throttle import Throttle
from multiply import Multiply
from device_sink import DeviceSink

class AnalogDemo(TopBlock):
    def __init__(self, num_channels, input_pins, output_pins):
        super().__init__()

        self.num_channels = num_channels
        self.input_pins = input_pins
        self.output_pins = output_pins

        # Create blocks for each channel
        self.analog_sources = []
        self.throttles = []
        self.multipliers = []
        self.analog_sinks = []

        for i in range(num_channels):
            # Analog input source
            analog_source = DeviceSource(1, "ADC", {"pin": input_pins[i], "atten": 0})
            self.analog_sources.append(analog_source)

            # Throttle to limit the data rate
            throttle = Throttle(1, 1000)  # Adjust the throttle rate as needed
            self.throttles.append(throttle)

            # Multiplier for scaling the input value
            multiplier = Multiply(1, 0.1)  # Adjust the scaling factor as needed
            self.multipliers.append(multiplier)

            # Analog output sink
            analog_sink = DeviceSink(1, "DAC", {"pin": output_pins[i]})
            self.analog_sinks.append(analog_sink)

            # Connect blocks for each channel
            self.connect(analog_source, throttle)
            self.connect(throttle, multiplier)
            self.connect(multiplier, analog_sink)

            # Add blocks to the graph
            self.add_block(analog_source)
            self.add_block(throttle)
            self.add_block(multiplier)
            self.add_block(analog_sink)

# Single-channel analog demo
single_channel_input_pin = 32  # Specify the input pin for single-channel demo
single_channel_output_pin = 25  # Specify the output pin for single-channel demo

single_channel_demo = AnalogDemo(1, [single_channel_input_pin], [single_channel_output_pin])
single_channel_demo.start()

# Run the single-channel demo for a specific duration
import time
time.sleep(5)

single_channel_demo.stop()
single_channel_demo.wait()

# Multi-channel analog demo
multi_channel_input_pins = [32, 33, 34]  # Specify the input pins for multi-channel demo
multi_channel_output_pins = [25, 26, 27]  # Specify the output pins for multi-channel demo

multi_channel_demo = AnalogDemo(len(multi_channel_input_pins), multi_channel_input_pins, multi_channel_output_pins)
multi_channel_demo.start()

# Run the multi-channel demo for a specific duration
time.sleep(5)

multi_channel_demo.stop()
multi_channel_demo.wait()