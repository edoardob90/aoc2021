# timer.py
from dataclasses import dataclass, field
from typing import Callable, ClassVar, Dict, Optional
import time
import functools
from decimal import Decimal as D

_units = {'s': 1, 'ms': 1000, 'm': 1/D('60'), 'h': 1/D('3600')}

class TimerError(Exception):
    """Exception to report errors in using the Timer class"""

@dataclass
class Timer:
    """A simple but convenient Timer class"""
    timers: ClassVar[Dict[str, float]] = {}
    name: Optional[str] = None
    text: str = "Elapsed time: {:0.4f} {:s}"
    unit: str = 's'
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)


    def __post_init(self) -> None:
        """Add timer to dict of timers"""
        if self.name is not None:
            self.timers.setdefault(self.name, 0)

        if self.unit != 's' and not self.unit in _units:
            raise TimerError('Undefined Timer units. Must be "s", "h", "ms" or "m"')

    def __enter__(self):
        """Start a new timer as a ctx manager"""
        self.start()
        return self

    def __exit__(self, *exit_info):
        """Stop the ctx manager timer"""
        self.stop()

    def __call__(self, func):
        """Use Timer as a decorator"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper

    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Time is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        # print(self.unit, _units)
        elapsed_time *= _units[self.unit]
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time, self.unit))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time
