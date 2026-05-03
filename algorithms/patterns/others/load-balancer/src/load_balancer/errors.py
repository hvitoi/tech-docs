"""Errors raised by the load balancer."""


class NoServersAvailableError(RuntimeError):
    """Raised when `get()` is called on an empty pool."""
