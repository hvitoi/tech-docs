# %%
# Exception hierarchy (the most relevant subset)
#
# BaseException                <- root of EVERYTHING (don't catch directly)
#  ├── BaseExceptionGroup      <- 3.11+ groups (used with except*)
#  ├── SystemExit              <- raised by sys.exit()
#  ├── KeyboardInterrupt       <- Ctrl+C
#  ├── GeneratorExit           <- generator/coroutine close()
#  └── Exception               <- base for "normal" errors (catch this)
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError
#       │    ├── OverflowError
#       │    └── FloatingPointError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError                  (alias: IOError, EnvironmentError)
#       │    ├── FileNotFoundError
#       │    ├── FileExistsError
#       │    ├── PermissionError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── TimeoutError
#       │    └── ConnectionError
#       │         ├── BrokenPipeError
#       │         ├── ConnectionAbortedError
#       │         ├── ConnectionRefusedError
#       │         └── ConnectionResetError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    └── RecursionError
#       ├── StopIteration
#       ├── StopAsyncIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       ├── ExceptionGroup          # 3.11+, subclass of BaseExceptionGroup
#       └── Warning                 # base of UserWarning, DeprecationWarning, ...

# %%
# "Error" vs "Exception" — there is NO semantic difference in Python.
# - `Exception` is the class name of the recommended base for user-defined errors.
# - `Error` is just a naming convention for subclasses (ValueError, TypeError, ...).
# - In Java terms: there is no "checked vs unchecked" distinction; all are unchecked.
# - The split that matters: `BaseException` vs `Exception`. `except:` and
#   `except BaseException:` catch SystemExit/KeyboardInterrupt/GeneratorExit too,
#   which usually breaks shutdown semantics. Catch `Exception` instead.

# %%
# Raising

raise ValueError("bad input")  # with message
raise ValueError  # bare class is fine, args=()

# Re-raise the current exception (only valid inside except)
try:
    int("x")
except ValueError:
    raise  # preserves original traceback

# %%
# try / except / else / finally
try:
    x = int("42")
except ValueError as e:  # bind to a name
    print("bad:", e)
except (KeyError, IndexError):  # catch multiple
    print("missing")
else:  # runs only if no exception
    print("ok:", x)
finally:  # always runs
    print("cleanup")

# %%
# Exception chaining
#
#   raise X from Y   -> sets __cause__ (explicit cause shown as "The above ...")
#   raise X          -> inside except, sets __context__ (implicit, "During handling ...")
#   raise X from None -> suppress chain entirely

try:
    int("x")
except ValueError as e:
    raise RuntimeError("could not parse") from e

# %%
# Built-in attributes every exception has
e = ValueError("bad", 42)
e.args  # ('bad', 42)  -- the constructor args
str(e)  # "('bad', 42)"  -- repr of args when len != 1
e.__cause__  # explicit cause (raise ... from ...)
e.__context__  # implicit cause (active exception when this was raised)
e.__suppress_context__  # True if `from None` was used
e.__traceback__  # traceback object (or None)
e.with_traceback  # method, returns self with traceback attached

# 3.11+ additions
e.add_note("happened while parsing config")  # appended to traceback
e.__notes__  # ['happened while parsing config']


# %%
# User-defined exceptions: subclass Exception (NOT BaseException)
class ConfigError(Exception):
    """Raised when config is invalid."""


class MissingKey(ConfigError):
    def __init__(self, key):
        super().__init__(f"missing config key: {key}")
        self.key = key


raise MissingKey("database.url")

# %%
# Exception groups (3.11+) — collect multiple exceptions into one
# Use `except*` to match members of the group.
try:
    raise ExceptionGroup("boot", [ValueError("a"), TypeError("b")])
except* ValueError as eg:
    print("values:", eg.exceptions)
except* TypeError as eg:
    print("types:", eg.exceptions)
