## Entity Relationship Description

### Customers
Stores customer information.
Primary Key: customer_id
Attributes: first_name, last_name, email, phone, city, registration_date
Relationship: One customer can place many orders (1:M).

### Products
Stores product catalog details.
Primary Key: product_id
Attributes: product_name, category, price, stock_quantity
Relationship: One product can appear in many order items (1:M).

### Orders
Stores order-level information.
Primary Key: order_id
Foreign Key: customer_id
Relationship: One order belongs to one customer.

### Order_Items
Stores line-item level order details.
Primary Key: order_item_id
Foreign Keys: order_id, product_id

## Normalization (3NF)
All tables are in Third Normal Form. Each non-key attribute depends only on the primary key. There are no transitive or partial dependencies, preventing insert, update, and delete anomalies.

## Sample Data
(Show 2 rows per table in markdown table format)
