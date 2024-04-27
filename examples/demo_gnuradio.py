import time
from top_block import TopBlock
from sig_source import SigSource
from throttle import Throttle
from file_sink import FileSink

class MyGraph(TopBlock):
    def __init__(self):
        super().__init__()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = 100

        ##################################################
        # Blocks
        ##################################################
        self.analog_sig_source_x_0 = SigSource(self.samp_rate, "GR_COS_WAVE", 10, 1000, 0)
        self.blocks_throttle_0 = Throttle(2, self.samp_rate)
        #self.blocks_udp_sink_0 = UDPSink(2, '192.168.1.103', 1234, 1024, True)
        self.blocks_file_sink_0 = FileSink(2, "output.txt")
        
        ##################################################
        # Add blocks (required on this port)
        ##################################################
        self.add_block(self.analog_sig_source_x_0)
        self.add_block(self.blocks_throttle_0)
        self.add_block(self.blocks_file_sink_0)
        
        ##################################################
        # Connections
        ##################################################
        self.connect(self.analog_sig_source_x_0, self.blocks_throttle_0)
        self.connect(self.blocks_throttle_0, self.blocks_file_sink_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.sampling_freq = self.samp_rate
        self.blocks_throttle_0.sample_rate = self.samp_rate


def main():
    tb = MyGraph()
    tb.start()
    time.sleep_ms(10000)
    tb.stop()
    tb.wait()

if __name__ == '__main__':
    main()