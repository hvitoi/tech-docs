# Restoration

- On every insertion/removal, the heap has to be restored in order to "restore" its datastructure properties (max/min order)

- `Restoration on insertion`
  - _Bubble the item upwards_, by comparing it with the parent nodes

- `Restoration on removal`
  - The last item in the complete tree takes place in the removed items
  - _Bubble the item downwards_, by comparing it with the child nodes
