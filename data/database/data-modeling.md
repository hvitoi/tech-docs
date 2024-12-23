# Data modeling

- Table for `Actors`
- E.g., store, customer, seller

- Table for `Actions` of actors
- E.g., customers make orders, complains, returns

- Table for `properties of actors` that don’t fit to 2D diagram
- E.g., possible payment methods for customer

- Table for `properties of actions` that don’t fit to 2D diagram
- E.g., possible reasons for return

## Normalization

- It's a Optimization technique in relational databases

- _Normalization_: separate tables for redundancy reduction
  - E.g., doc, doctor, med doc
  - Cons: You know less from only one table. Have to read more than one table
- _Denormalization_: application of JOINS to integrate tables

### Normalized data

- `Minimizes storage` spaces
- Requires `two queries` to get data from different sources (tables, collections)
- Easy to perform updates! Need to change only one source of data
- Good approach when the data storage is expensive! And the performance is not important
  - Doubles the traffic with double queries (two transactions)! Increseases latency

### Denormalized data

- Data is duplicated in order for a source to container all the information needed!
- Only requires one transaction to fetch the complete data
- Improves the performance!
- Downside is that in order to update data, many sources must be updated
