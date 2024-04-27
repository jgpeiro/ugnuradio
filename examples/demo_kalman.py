from top_block import TopBlock
from sig_source import SigSource
from throttle import Throttle
from multiply import Multiply
from add import Add
from kalman_filter import KalmanFilter
from probe import Probe

class KalmanFilterDemo(TopBlock):
    def __init__(self):
        super().__init__()

        # Create blocks
        self.signal_source = SigSource(1, "GR_SIN_WAVE", 1000, 1, 0)
        self.noise_source = SigSource(1, "GR_GAUSSIAN", 1000, 0.1, 0)
        self.throttle = Throttle(1, 10000)  # Adjust the throttle rate as needed
        self.adder = Add(1)
        self.kalman_filter = KalmanFilter(1, 0.1, 0.1, 0.1)  # Adjust the Kalman filter parameters as needed
        self.signal_probe = Probe(1, self.print_signal)
        self.filtered_probe = Probe(1, self.print_filtered)

        # Connect blocks
        self.connect(self.signal_source, (self.adder, 0))
        self.connect(self.noise_source, (self.adder, 1))
        self.connect(self.adder, self.throttle)
        self.connect(self.throttle, (self.kalman_filter, 0))
        self.connect(self.throttle, self.signal_probe)
        self.connect(self.kalman_filter, self.filtered_probe)

        # Add blocks to the graph
        self.add_block(self.signal_source)
        self.add_block(self.noise_source)
        self.add_block(self.throttle)
        self.add_block(self.adder)
        self.add_block(self.kalman_filter)
        self.add_block(self.signal_probe)
        self.add_block(self.filtered_probe)

    def print_signal(self, sample):
        print(f"Signal: {sample}")

    def print_filtered(self, sample):
        print(f"Filtered: {sample}")

# Create and run the Kalman filter demo
demo = KalmanFilterDemo()
demo.start()

# Run the demo for a specific duration
import time
time.sleep(5)

demo.stop()
demo.wait()