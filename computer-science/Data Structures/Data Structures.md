# Data Structure

- <https://en.wikipedia.org/wiki/List_of_data_structures>
- <https://www.bigocheatsheet.com/>

## Operations

- `Access` (Lookup): get an element in the structure by its identifier
- `Search`: find the location of an element in the structure
- `Insertion`: add a new element to the structure
- `Deletion`: delete an existing element from the structure

- `Traverse`: cycle over each element in the structure
- `Sorting`: organize the data in the structure in some way

## Language Support

|        | Array    | Dynamic Array | Linked List | Stack         | Queue                       | Priority Queue | Deque | Associative Array | Set | Graph |
| -      | -        | -             | -           | -             | -                           | -              | -     | -                 | -   | -     |
| Java   | Built-in | ArrayList     | LinkedList  | Stack         | LinkedList                  | PriorityQueue        | LinkedList | HashTable, TreeMap & others | HashSet, TreeSet | N/A |
| Python | Built-in | list          | N/A         | list as stack | queue, deque, list as queue | PriorityQueue, heapq | deque      | dict | set, fronzenset | N/A |

## Traversal

- A way to loop thorough all the elements in a given data structure
- `Example`: in a Linked List, the traversal stops when the next element points to null
- Traversals are usually implemented with a `while`/`for` and a defined `stop rule` according to each data structure

- **Iteration**
  - A special kind of traversal that is done over a `linear data structure` (e.g., arrays)
  - Sometimes term is also used interchangeably
