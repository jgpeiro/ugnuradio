class KalmanFilter(TopBlock):
    def __init__(self, item_size, process_noise, measurement_noise, initial_estimate):
        super().__init__()
        self.item_size = item_size
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        self.estimate = initial_estimate
        self.error_estimate = 1.0
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            measurement = input_items[i]

            # Predict step
            predicted_estimate = self.estimate
            predicted_error_estimate = self.error_estimate + self.process_noise

            # Update step
            kalman_gain = predicted_error_estimate / (predicted_error_estimate + self.measurement_noise)
            self.estimate = predicted_estimate + kalman_gain * (measurement - predicted_estimate)
            self.error_estimate = (1 - kalman_gain) * predicted_error_estimate

            output_items.append(self.estimate)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass