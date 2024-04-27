class MagicMock:
    def __init__(self, return_value=None):
        self.return_value = return_value
        self.called = False
        self.call_count = 0
        self.call_args = None
        self.call_args_list = []
        self.method_calls = {}

    def __call__(self, *args, **kwargs):
        self.called = True
        self.call_count += 1
        self.call_args = (args, kwargs)
        self.call_args_list.append((args, kwargs))
        return self.return_value

    def __getattr__(self, name):
        if name not in self.method_calls:
            self.method_calls[name] = MagicMock()
        return self.method_calls[name]

    def assert_called(self):
        assert self.called, "Expected mock to have been called."

    def assert_called_once(self):
        assert self.call_count == 1, f"Expected mock to have been called once. Called {self.call_count} times."

    def assert_called_with(self, *args, **kwargs):
        assert self.call_args == (args, kwargs), f"Expected mock to have been called with {args}, {kwargs}. Called with {self.call_args}."

    def assert_has_calls(self, calls, any_order=False):
        if not any_order:
            assert self.call_args_list == calls, f"Expected mock to have been called with {calls}. Called with {self.call_args_list}."
        else:
            assert all(call in self.call_args_list for call in calls), f"Expected mock to have been called with {calls} in any order. Called with {self.call_args_list}."

    def reset_mock(self):
        self.called = False
        self.call_count = 0
        self.call_args = None
        self.call_args_list = []
        self.method_calls = {}