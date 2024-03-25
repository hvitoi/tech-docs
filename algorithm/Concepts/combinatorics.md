# Analytic combinatorics

## Fundamental Principle of Counting

- The `total number of possibilities` is the `product of the possibilities in each step`
- E.g., a code in the format $0A, \cdots, 9Z$ has $10*26$ possibilities

## Arrangement

- The `number of possibilities` to form an `ordered subgroup`
- Arrangement is `ordered`
- Arrangement has `no repetitions`

- $n$: available number of elements
- $p$: total elements in the subgroup

$$A_{n,p} = \frac{n!}{(n-p)!}$$

## Permutation

- Permutation is a kind of arrangement where all the elements are used $n=p$

- **Permutation Simple**

  - An arrangement where $n=p$

  $$P_n = n!$$

- **Permutation with repetition**

  - $n$: available number of elements
  - $a,b,c$: number of times each component repeats
  - Use cases: anagrams of words with repeating letters

  $$A^{a,b}_{n} = \frac{n!}{a!*b!*c!}$$

- **Permutation Circular**
  $$P^{circular}_n = (n-1)!$$

## Combination

- The `number of possibilities` to form an `unordered subgroup`

- $n$: available number of elements
- $p$: total elements in the subgroup

$$\binom{n}{p} = \frac{n!}{(n-p)!*p!}$$
$$\binom{n}{p} = \frac{A_{n,p}}{p!}$$
