from top_block import TopBlock
from device_source import DeviceSource
from throttle import Throttle
from add import Add
from device_sink import DeviceSink

class ADCPWMDemo(TopBlock):
    def __init__(self, adc_pin1, adc_pin2, sample_rate, pwm_pin, pwm_freq):
        super().__init__()

        # Create blocks
        self.adc_source1 = DeviceSource(1, "ADC", {"pin": adc_pin1})
        self.adc_source2 = DeviceSource(1, "ADC", {"pin": adc_pin2})
        self.throttle1 = Throttle(1, sample_rate)
        self.throttle2 = Throttle(1, sample_rate)
        self.adder = Add(1)
        self.pwm_sink = DeviceSink(1, "PWM", {"pin": pwm_pin, "freq": pwm_freq})

        # Connect blocks
        self.connect(self.adc_source1, self.throttle1)
        self.connect(self.adc_source2, self.throttle2)
        self.connect(self.throttle1, (self.adder, 0))
        self.connect(self.throttle2, (self.adder, 1))
        self.connect(self.adder, self.pwm_sink)

        # Add blocks to the graph
        self.add_block(self.adc_source1)
        self.add_block(self.adc_source2)
        self.add_block(self.throttle1)
        self.add_block(self.throttle2)
        self.add_block(self.adder)
        self.add_block(self.pwm_sink)

# ADC and PWM configuration
adc_pin1 = 32  # Specify the first ADC pin
adc_pin2 = 33  # Specify the second ADC pin
sample_rate = 1000  # Specify the sample rate in Hz
pwm_pin = 25  # Specify the PWM output pin
pwm_freq = 1000  # Specify the PWM frequency in Hz

# Create and run the ADC PWM demo
demo = ADCPWMDemo(adc_pin1, adc_pin2, sample_rate, pwm_pin, pwm_freq)
demo.start()

# Run the demo indefinitely
import time
while True:
    time.sleep(1)