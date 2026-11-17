# SEPA Direct Debit (SDD) - SDD Collections

- **Features**
  - The transaction is initiated by the creditor (not debtor)
  - The creditor pulls de money, and the `amount can vary over time`

## Outgoing vs. Incoming SDD

- **SDD Outgoing**: client is the debtor (paying)
- **SDD Incoming**: client is the creditor (receiving)

## Mandates

- The `Creditor` (merchant) sends a mandate to `Debtor` (buyer)
- A mandate can be a `one off` or `recurrent`
- Each mandate has a unique identifier (**UMR**)

## Refunds

### Type A

- Up to `8 weeks` after the charge the debtor can contest undue charge (no questions asked)
- Refunding the debtor
  - Must happen at D+1

### Type B

- From `8 weeks` to to `13 months` in case of fraud
- Refunding the debtor
  - Must happen at D+1
- Charging back the creditor
  - First we need to request the a copy of the `mandate` and wait 30 days before charging the creditor

## SDD Schemes

- SEPA Direct Debit **Core**
- SEPA Direct Debit **B2B** (Business-to-Business)

## Glossary

- Creditor
- Debtor
- Creditor/debtor bank
- Mandate
- UMR
- CID (creditor identifier)
- Pre-notification
- Due date
- Settlement
- R-transaction

## R-transactions (Reversal Transactions)

- For stopping or undoing a collection

- `Creditor-initiated`
  - Cancellation (before settlement)
  - Reversal (up to 5 TARGET2 days after due date)

- `Initiated by a bank or the debtor`
  - Reject (before settlement)
  - Return (up to 5 TARGET2 days after settlement)
  - Refund (up to 8 weeks)
  - Refund (up to 13 months)

## Settlement

- `D (settlement date)`
- `D+5` (Guarding release)
- `<= D+5` (return window)
- `D+8 wk` (refund A)
- `D+13 mo` (refund B)
