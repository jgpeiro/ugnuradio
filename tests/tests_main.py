import unittest
from test_top_block import TestTopBlock
from test_sig_source import TestSigSource
from test_throttle import TestThrottle
from test_udp_sink import TestUDPSink
from test_udp_source import TestUDPSource
from test_interpolating_fir_filter import TestInterpolatingFIRFilter
from test_am_modulator import TestAMModulator
from test_fm_modulator import TestFMModulator
from test_constellation_modulator import TestConstellationModulator
from test_constellation_demodulator import TestConstellationDemodulator
from test_interpolation import TestInterpolation
from test_decimation import TestDecimation
from test_multiply import TestMultiply
from test_divide import TestDivide
from test_probe import TestProbe
from test_time_delay import TestTimeDelay
from test_threshold import TestThreshold
from test_selector import TestSelector
from test_gui_widgets import TestGUIWidgets
from test_device_source import TestDeviceSource
from test_device_sink import TestDeviceSink

def run_tests():
    # Create a test suite
    suite = unittest.TestSuite()

    # Add test cases to the suite
    suite.addTest(unittest.makeSuite(TestTopBlock))
    suite.addTest(unittest.makeSuite(TestSigSource))
    suite.addTest(unittest.makeSuite(TestThrottle))
    suite.addTest(unittest.makeSuite(TestUDPSink))
    suite.addTest(unittest.makeSuite(TestUDPSource))
    suite.addTest(unittest.makeSuite(TestInterpolatingFIRFilter))
    suite.addTest(unittest.makeSuite(TestAMModulator))
    suite.addTest(unittest.makeSuite(TestFMModulator))
    suite.addTest(unittest.makeSuite(TestConstellationModulator))
    suite.addTest(unittest.makeSuite(TestConstellationDemodulator))
    suite.addTest(unittest.makeSuite(TestInterpolation))
    suite.addTest(unittest.makeSuite(TestDecimation))
    suite.addTest(unittest.makeSuite(TestMultiply))
    suite.addTest(unittest.makeSuite(TestDivide))
    suite.addTest(unittest.makeSuite(TestProbe))
    suite.addTest(unittest.makeSuite(TestTimeDelay))
    suite.addTest(unittest.makeSuite(TestThreshold))
    suite.addTest(unittest.makeSuite(TestSelector))
    suite.addTest(unittest.makeSuite(TestGUIWidgets))
    suite.addTest(unittest.makeSuite(TestDeviceSource))
    suite.addTest(unittest.makeSuite(TestDeviceSink))

    # Create a test runner
    runner = unittest.TextTestRunner(verbosity=2)

    # Run the tests
    runner.run(suite)

if __name__ == "__main__":
    run_tests()