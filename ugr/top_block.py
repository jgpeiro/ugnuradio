class _TopBlock:
    def __init__(self):
        self.blocks = []

    def connect(self, block1, block2):
        block1.set_next(block2)
        if( block1 not in self.blocks ):
            self.add_block( block1 )
        if( block2 not in self.blocks ):
            self.add_block( block2 )

    def start(self):
        for block in self.blocks:
            block.start()

    def stop(self):
        for block in self.blocks:
            block.stop()

    def wait(self):
        for block in self.blocks:
            block.wait()

    def add_block(self, block):
        self.blocks.append(block)

import time


class TopBlock:
    def __init__(self):
        self.blocks = []
        self.running = False

    def connect(self, block1, block2):
        block1.set_next(block2)

    def start(self):
        self.running = True
        for block in self.blocks:
            block.start()
        self.scheduler()

    def stop(self):
        self.running = False
        for block in self.blocks:
            block.stop()

    def wait(self):
        while self.running:
            time.sleep(0.1)

    def add_block(self, block):
        self.blocks.append(block)

    def scheduler(self):
        from sig_source import SigSource
        while self.running:
            for block in self.blocks:
                if isinstance(block, SigSource):
                    block.work([], [0.0] * 1024)
            time.sleep(0.1)