# Entity Relationship Diagram

- More generic than classDiagram
- Expresses entities that are related in some way

```mermaid
erDiagram
  %% CUSTOMER has 0 or more ORDER
  %% ORDER has exactly one CUSTOMER
  CUSTOMER ||--o{ ORDER : places

  %% ORDER has 1 or more LINE-ITEM
  ORDER ||--|{ LINE-ITEM : contains

  %%
  CUSTOMER }|..|{ DELIVERY-ADDRESS : uses



  % Details
  CUSTOMER {
    String id
    String name
  }
  ORDER {
    String id
    OrderStatus status
  }
  LINE-ITEM {
    String code
    String description
    int qunatity
    int price
  }
```
