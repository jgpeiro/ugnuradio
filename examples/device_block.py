import machine

class DeviceSource(TopBlock):
    def __init__(self, item_size, device_type, device_config):
        super().__init__()
        self.item_size = item_size
        self.device_type = device_type
        self.device_config = device_config
        self.device = None
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        if self.device_type == "SPI":
            data = self.device.read(self.item_size)
        elif self.device_type == "I2C":
            data = self.device.readfrom(self.device_config["address"], self.item_size)
        elif self.device_type == "ADC":
            data = [self.device.read() for _ in range(self.item_size)]
        elif self.device_type == "Pin":
            data = [self.device.value() for _ in range(self.item_size)]
        else:
            raise ValueError(f"Unsupported device type: {self.device_type}")

        output_items.extend(data)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        if self.device_type == "SPI":
            self.device = machine.SPI(**self.device_config)
        elif self.device_type == "I2C":
            self.device = machine.I2C(**self.device_config)
        elif self.device_type == "ADC":
            self.device = machine.ADC(**self.device_config)
        elif self.device_type == "Pin":
            self.device = machine.Pin(**self.device_config)
        else:
            raise ValueError(f"Unsupported device type: {self.device_type}")

    def stop(self):
        if self.device is not None:
            self.device.deinit()
            self.device = None

    def wait(self):
        pass


class DeviceSink(TopBlock):
    def __init__(self, item_size, device_type, device_config):
        super().__init__()
        self.item_size = item_size
        self.device_type = device_type
        self.device_config = device_config
        self.device = None
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        if self.device_type == "SPI":
            self.device.write(input_items)
        elif self.device_type == "I2C":
            self.device.writeto(self.device_config["address"], input_items)
        elif self.device_type == "PWM":
            for value in input_items:
                self.device.duty(value)
        elif self.device_type == "Pin":
            for value in input_items:
                self.device.value(value)
        else:
            raise ValueError(f"Unsupported device type: {self.device_type}")

        if self.next_block is not None:
            self.next_block.work(input_items, None)

    def start(self):
        if self.device_type == "SPI":
            self.device = machine.SPI(**self.device_config)
        elif self.device_type == "I2C":
            self.device = machine.I2C(**self.device_config)
        elif self.device_type == "PWM":
            self.device = machine.PWM(**self.device_config)
        elif self.device_type == "Pin":
            self.device = machine.Pin(**self.device_config)
        else:
            raise ValueError(f"Unsupported device type: {self.device_type}")

    def stop(self):
        if self.device is not None:
            self.device.deinit()
            self.device = None

    def wait(self):
        pass