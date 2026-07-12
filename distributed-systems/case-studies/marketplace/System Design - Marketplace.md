# Marketplace - System design

## Functional Requirements

- **Merchants**
  - Operations
    - Upload products
    - Sell products
  - Digital or physical products?
    - Inventory?
    - Physical products with limited inventory
  - Merchant registration
    - What data?
    - Any physical person companies only?
  - Refunds and return policies? Out of scope for now?
  - What info the merchant needs to upload about the product?
    - Title
    - Description
    - Categories
    - Image
    - Videos
  - What info the platform needs to provide to the merchant about the sales?
    - Needs a product management system (webapp)
    - Sign up
    - Create new, update products
    - Analytics
      - Real-time page visitors
      - Historical trends
- **Buyers**
  - Browse products
  - Search products
  - Buy products
- **Products**
  - Product reviews?
  - Search capabilities
    - Seach by title, category, description
- **Platform**
  - Browser-based

## Non-functional Requirements

- Total customers
  - 200M
- Daily users
  - 50M /day
- Geographic distribution
  - Worldwide

## User Flow

1. Merchant signs up
2. Merchant logs in
3. Merchant creates an ad with description, picture, etc
4. Merchant manages the ad, edits, and looks
5. Merchant sees selling insights/analytics
6. Buyers logs in
7. Buyers sees the frontpage and sees the available products
8. Buyers searches an item by its title
9. Buyer adds the item to the cart
10. Buyers checkouts and sees the buying summary
11. Buyers confirms shipping & billing information
12. Buyers confirms
13. Platform will record the order and update inventory
14. Platform will bill the user
15. Platform sends a email confirmation to the user
