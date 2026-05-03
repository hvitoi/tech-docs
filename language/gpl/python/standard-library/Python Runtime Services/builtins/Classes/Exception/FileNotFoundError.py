# %%
# FileNotFoundError -- OSError -- Exception -- BaseException
#
# OSError corresponds to system-call errors. Since 3.3, the constructor
# auto-selects a subclass based on errno, so opening a missing file raises
# FileNotFoundError directly (not bare OSError).
#
# The whole OSError family:
#   OSError  (aliases: IOError, EnvironmentError -- kept for backward compat)
#    ├── FileNotFoundError       errno.ENOENT
#    ├── FileExistsError         errno.EEXIST
#    ├── PermissionError         errno.EACCES / EPERM
#    ├── IsADirectoryError       errno.EISDIR
#    ├── NotADirectoryError      errno.ENOTDIR
#    ├── InterruptedError        errno.EINTR
#    ├── TimeoutError            errno.ETIMEDOUT (also raised by signal.alarm, asyncio)
#    ├── BlockingIOError         EAGAIN/EWOULDBLOCK/EALREADY/EINPROGRESS
#    ├── ChildProcessError       errno.ECHILD
#    └── ConnectionError
#         ├── BrokenPipeError          errno.EPIPE / ESHUTDOWN
#         ├── ConnectionAbortedError   errno.ECONNABORTED
#         ├── ConnectionRefusedError   errno.ECONNREFUSED
#         └── ConnectionResetError     errno.ECONNRESET

open(
    "/no/such/file"
)  # FileNotFoundError: [Errno 2] No such file or directory: '/no/such/file'

# %%
# OSError attributes (set automatically when raised by the OS)
try:
    open("/no/such/file")
except OSError as e:
    e.errno  # 2
    e.strerror  # 'No such file or directory'
    e.filename  # '/no/such/file'
    e.filename2  # None (used by ops with two paths, e.g. rename)

# %%
# Catch the family
import os

try:
    os.remove("/etc/passwd")
except PermissionError:
    print("nope")
except FileNotFoundError:
    print("missing")
except OSError as e:  # catches all the rest
    print("other os error:", e)

# %%
# pathlib raises the same exceptions
from pathlib import Path
# Path("/no/such").read_text()   # FileNotFoundError

# %%
# Use exist_ok / missing_ok to avoid having to catch
Path("/tmp/maybe").mkdir(exist_ok=True)  # no FileExistsError if it already exists
Path("/tmp/maybe/file").unlink(missing_ok=True)  # no FileNotFoundError if absent
