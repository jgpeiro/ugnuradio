import socket
from top_block import TopBlock

class UDPSource(TopBlock):
    def __init__(self, item_size, host, port, payload_size, eof):
        super().__init__()
        self.item_size = item_size
        self.host = host
        self.port = port
        self.payload_size = payload_size
        self.eof = eof
        self.socket = None
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        # Receive data over UDP
        data, address = self.socket.recvfrom(self.payload_size)

        # Check for EOF packet
        if self.eof and not data:
            self.stop()
            return

        # Convert received data to output items
        output_items[:] = list(data)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        # Create a UDP socket if not already created
        if self.socket is None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.host, self.port))

    def stop(self):
        # Close the UDP socket if it exists
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def wait(self):
        pass