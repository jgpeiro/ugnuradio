from top_block import TopBlock
from device_source import DeviceSource
from throttle import Throttle
from interpolating_fir_filter import InterpolatingFIRFilter
from am_demodulator import AMDemodulator
from multiply import Multiply
from divide import Divide
from probe import Probe
from device_sink import DeviceSink

class AMRadioReceiver(TopBlock):
    def __init__(self, rf_freq, sample_rate, audio_rate):
        super().__init__()

        # Create blocks
        self.sdr_source = DeviceSource(1, "SDR", {"freq": rf_freq, "sample_rate": sample_rate})
        self.throttle = Throttle(1, sample_rate)
        self.bandpass_filter = InterpolatingFIRFilter(1, 1, self.get_bandpass_coefficients(rf_freq, sample_rate), 0)
        self.am_demodulator = AMDemodulator(0.5)
        self.audio_filter = InterpolatingFIRFilter(1, 1, self.get_audio_coefficients(audio_rate), 0)
        self.audio_gain = Multiply(1, 10)
        self.audio_sink = DeviceSink(1, "I2S", {"bck_pin": 26, "ws_pin": 25, "sdout_pin": 22, "rate": audio_rate})

        # Connect blocks
        self.connect(self.sdr_source, self.throttle)
        self.connect(self.throttle, self.bandpass_filter)
        self.connect(self.bandpass_filter, self.am_demodulator)
        self.connect(self.am_demodulator, self.audio_filter)
        self.connect(self.audio_filter, self.audio_gain)
        self.connect(self.audio_gain, self.audio_sink)

        # Add blocks to the graph
        self.add_block(self.sdr_source)
        self.add_block(self.throttle)
        self.add_block(self.bandpass_filter)
        self.add_block(self.am_demodulator)
        self.add_block(self.audio_filter)
        self.add_block(self.audio_gain)
        self.add_block(self.audio_sink)

    def get_bandpass_coefficients(self, rf_freq, sample_rate):
        # Generate bandpass filter coefficients for the desired RF frequency
        # You can use tools like scipy.signal.firwin to design the filter
        # Return the filter coefficients as a list
        pass

    def get_audio_coefficients(self, audio_rate):
        # Generate audio filter coefficients for the desired audio rate
        # You can use tools like scipy.signal.firwin to design the filter
        # Return the filter coefficients as a list
        pass

# Create and run the AM radio receiver
rf_freq = 1000000  # RF frequency in Hz
sample_rate = 2000000  # SDR sample rate in Hz
audio_rate = 44100  # Audio sample rate in Hz

am_receiver = AMRadioReceiver(rf_freq, sample_rate, audio_rate)
am_receiver.start()

# Run the receiver indefinitely
import time
while True:
    time.sleep(1)