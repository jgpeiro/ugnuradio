from top_block import TopBlock
from device_source import DeviceSource
from throttle import Throttle
from udp_sink import UDPSink

class ADCUDPDemo(TopBlock):
    def __init__(self, adc_pin, sample_rate, udp_host, udp_port):
        super().__init__()

        # Create blocks
        self.adc_source = DeviceSource(1, "ADC", {"pin": adc_pin})
        self.throttle = Throttle(1, sample_rate)
        self.udp_sink = UDPSink(1, udp_host, udp_port, 1024, True)

        # Connect blocks
        self.connect(self.adc_source, self.throttle)
        self.connect(self.throttle, self.udp_sink)

        # Add blocks to the graph
        self.add_block(self.adc_source)
        self.add_block(self.throttle)
        self.add_block(self.udp_sink)

# ADC and UDP configuration
adc_pin = 32  # Specify the ADC pin
sample_rate = 1000  # Specify the sample rate in Hz
udp_host = "192.168.0.100"  # Specify the UDP host IP address
udp_port = 5000  # Specify the UDP port

# Create and run the ADC UDP demo
demo = ADCUDPDemo(adc_pin, sample_rate, udp_host, udp_port)
demo.start()

# Run the demo indefinitely
import time
while True:
    time.sleep(1)