from top_block import TopBlock
from file_source import FileSource
from throttle import Throttle
from device_sink import DeviceSink
from device_source import DeviceSource
from file_sink import FileSink

class FileSPITransfer(TopBlock):
    def __init__(self, input_file, output_file, spi_config):
        super().__init__()

        # Create blocks
        self.file_source = FileSource(1, input_file)
        self.throttle = Throttle(1, 1000000)  # Adjust the throttle rate as needed
        self.spi_sink = DeviceSink(1, "SPI", spi_config)
        self.spi_source = DeviceSource(1, "SPI", spi_config)
        self.file_sink = FileSink(1, output_file)

        # Connect blocks
        self.connect(self.file_source, self.throttle)
        self.connect(self.throttle, self.spi_sink)
        self.connect(self.spi_source, self.file_sink)

        # Add blocks to the graph
        self.add_block(self.file_source)
        self.add_block(self.throttle)
        self.add_block(self.spi_sink)
        self.add_block(self.spi_source)
        self.add_block(self.file_sink)

# Configure SPI parameters
spi_config = {
    "baudrate": 1000000,
    "polarity": 0,
    "phase": 0,
    "bits": 8,
    "firstbit": 0,
    "sck": 14,
    "mosi": 13,
    "miso": 12,
    "cs": 15
}

# Specify input and output file paths
input_file = "input.txt"
output_file = "output.txt"

# Create and run the file-to-SPI-to-file transfer
transfer = FileSPITransfer(input_file, output_file, spi_config)
transfer.start()

# Wait for the transfer to complete
transfer.wait()

# Stop the transfer
transfer.stop()