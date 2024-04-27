from top_block import TopBlock

class _UDPSink(TopBlock):
    def __init__(self, item_size, host, port, payload_size, eof):
        super().__init__()
        self.item_size = item_size
        self.host = host
        self.port = port
        self.payload_size = payload_size
        self.eof = eof

    def work(self, input_items, output_items):
        # Send the input items over UDP
        # Implement the UDP sending logic here
        # ...

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass

import socket

class UDPSink(TopBlock):
    def __init__(self, item_size, host, port, payload_size, eof):
        super().__init__()
        self.item_size = item_size
        self.host = host
        self.port = port
        self.payload_size = payload_size
        self.eof = eof
        self.socket = None

    def work(self, input_items, output_items):
        # Convert input items to bytes
        data = bytearray(input_items)

        # Send data over UDP
        num_packets = len(data) // self.payload_size
        for i in range(num_packets):
            start = i * self.payload_size
            end = start + self.payload_size
            packet = data[start:end]
            self.socket.sendto(packet, (self.host, self.port))

        # Send remaining data if any
        remaining_data = data[num_packets * self.payload_size:]
        if remaining_data:
            self.socket.sendto(remaining_data, (self.host, self.port))

        # Send EOF packet if specified
        if self.eof:
            self.socket.sendto(b'', (self.host, self.port))

    def start(self):
        # Create a UDP socket if not already created
        if self.socket is None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def stop(self):
        # Close the UDP socket if it exists
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def wait(self):
        pass