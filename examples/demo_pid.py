from top_block import TopBlock
from sig_source import SigSource
from throttle import Throttle
from interpolating_fir_filter import InterpolatingFIRFilter
from multiply import Multiply
from divide import Divide
from probe import Probe
from device_sink import DeviceSink

class PIDDemoGraph(TopBlock):
    def __init__(self):
        super().__init__()

        # Create blocks
        self.sig_source = SigSource(1, "GR_SIN_WAVE", 1000, 1, 0)
        self.throttle = Throttle(1, 10000)
        self.pid_filter = InterpolatingFIRFilter(1, 1, [0.1, 0.2, 0.3, 0.2, 0.1], 0)
        self.proportional_gain = Multiply(1, 1.5)
        self.integral_gain = Multiply(1, 0.01)
        self.derivative_gain = Multiply(1, 0.1)
        self.output_scale = Divide(1, 10)
        self.probe = Probe(1, self.print_output)
        self.device_sink = DeviceSink(1, "PWM", {"pin": 12, "freq": 1000, "duty": 0})

        # Connect blocks
        self.connect(self.sig_source, self.throttle)
        self.connect(self.throttle, self.pid_filter)
        self.connect(self.pid_filter, self.proportional_gain)
        self.connect(self.pid_filter, self.integral_gain)
        self.connect(self.pid_filter, self.derivative_gain)
        self.connect(self.proportional_gain, self.output_scale)
        self.connect(self.integral_gain, self.output_scale)
        self.connect(self.derivative_gain, self.output_scale)
        self.connect(self.output_scale, self.probe)
        self.connect(self.output_scale, self.device_sink)

        # Add blocks to the graph
        self.add_block(self.sig_source)
        self.add_block(self.throttle)
        self.add_block(self.pid_filter)
        self.add_block(self.proportional_gain)
        self.add_block(self.integral_gain)
        self.add_block(self.derivative_gain)
        self.add_block(self.output_scale)
        self.add_block(self.probe)
        self.add_block(self.device_sink)

    def print_output(self, sample):
        print(f"PID Output: {sample}")

# Create and run the PID demo graph
pid_demo = PIDDemoGraph()
pid_demo.start()

# Run the graph for a specific duration
import time
time.sleep(10)

# Stop the graph
pid_demo.stop()
pid_demo.wait()