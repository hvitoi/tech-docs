"""In-memory thread-safe load balancer with pluggable selection strategies."""

from load_balancer.balancer import LoadBalancer, NoServersAvailableError, PoolFullError
from load_balancer.strategies import RoundRobin, Strategy, random_choice

__all__ = [
    "LoadBalancer",
    "NoServersAvailableError",
    "PoolFullError",
    "RoundRobin",
    "Strategy",
    "random_choice",
]


def main():
    lb = LoadBalancer()


if __name__ == "__main__":
    main()
