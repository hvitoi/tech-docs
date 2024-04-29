# NP Completeness

- Everything in `NP` (currently not solvable in a fast manner) will eventually become `P` as we find new approaches to the problems?
  - This is the **P vs. NP problem**
- Does being able to quickly recognize correct answers (`NP`) means there's also a quick way to find them? (`P`)

> "If P=NP, then the world would be a profoundly different place than we usually assume it to be. There would be no special value in 'creative leaps', no fundamental gap between solving a problem and recognizing the solution once it's found. Everyone who could appreciate a symphony would be Mozart; everyone who could follow a step-by-step argument would be Gauss."

## P (Polynomial time)

- Problems `solvable` in `polynomial time`
- It's a class of problems that can be solved reasonably fast

- Examples
  - Multiplication
  - Sorting

## NP (Non-deterministic Polynomial time)

- Problems `verifiable` in `polynomial time`
- If given a correct solution, you can prove it in a reasonable amount of time

- Examples
  - Vehicle routing (TSP)
  - Job scheduling
  - Finding primes (which was later proven to be P)
  - Sudoku (easy to verify a solution)

- `NP Complete` is a subset of NP problems

## NP Hard

- Problems `not verifiable` in `polynomial time`

- Examples
  - Check if a movement in chess is the best one
