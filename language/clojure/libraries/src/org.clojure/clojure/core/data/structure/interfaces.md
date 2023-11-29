# Interfaces

- **IPersistentList**
  - Extends: `Sequential`, `IPersistentStack`
- **Sequential**
- **IPersistentStack**
  - Extends: `IPersistentCollection`
  - Methods
    - _peek_
    - _pop_
- **IPersistentCollection**
  - Extends: `Seqable`
  - Methods
    - _count_
    - _cons_
    - _empty_
    - _equiv_
- **Seqable**
  - Methods:
    - _seq_
