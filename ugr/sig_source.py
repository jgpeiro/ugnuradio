import math
from top_block import TopBlock

class SigSource(TopBlock):
    def __init__(self, sampling_freq, waveform, frequency, amplitude, offset):
        super().__init__()
        self.sampling_freq = sampling_freq
        self.waveform = waveform
        self.frequency = frequency
        self.amplitude = amplitude
        self.offset = offset
        self.next_block = None
        self.phase = 0.0

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        # Generate signal samples based on the waveform, frequency, amplitude, and offset
        num_samples = len(output_items)
        for i in range(num_samples):
            if self.waveform == "GR_COS_WAVE":
                # Generate cosine wave samples
                sample = self.amplitude * math.cos(2 * math.pi * self.frequency * self.phase / self.sampling_freq) + self.offset
            elif self.waveform == "GR_SIN_WAVE":
                # Generate sine wave samples
                sample = self.amplitude * math.sin(2 * math.pi * self.frequency * self.phase / self.sampling_freq) + self.offset
            elif self.waveform == "GR_CONST_WAVE":
                # Generate constant value samples
                sample = self.amplitude + self.offset
            else:
                # Unsupported waveform
                sample = 0.0

            output_items[i] = sample
            self.phase += 1

        if self.next_block is not None:
            self.next_block.work(output_items, [])

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass