# A simple `Timer` class

## Install

Run `pip install .` within this directory. The package can be imported with the usual `from timer import timer` or `from timer.timer import Timer` if you want to strip the module namespace.

## Usage

The timer can be used as a context manager

```python
with Timer(name='ctx timer'):
    # measure the time
```

or as a decorator:
```python
@Timer(name='decorator timer')
def my_func(a, b, *args, **kwargs):
    # function's body
    pass

my_func(40, 100, "a", "b", "c", text="Python")
```


The class `Timer` can be customized by passing the following arguments:

- `name`: to create multiple timers and give a name to each of them
- `text`: to print a custom string instead of "Elapsed time: XXX"
- `unit`: the unit used to print the time. A string among `s` (seconds, default), `ms` (milliseconds), `m` (minutes), or `h` (hours) 
- `logger`: a callable used to log the time spent. By default, is the built-in `print` function
