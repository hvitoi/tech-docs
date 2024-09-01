# AWS::Budgets::Budget

- Set custom budgets that alert you when you exceed your budgeted thresholds
- Alerts can be emitted when the limit to close

```yaml
Type: AWS::Budgets::Budget
Properties:
  Budget:
    BudgetData
  NotificationsWithSubscribers:
    - NotificationWithSubscribers
  ResourceTags:
    - ResourceTag
```

## BudgetData

- **BudgetType**
  - `Cost budget`: set value threshold in dollars
  - `Usage budget`
  - `Savings Plans budget`
  - `Reservation budget`
