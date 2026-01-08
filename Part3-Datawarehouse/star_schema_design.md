# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

FACT TABLE: fact_sales  
Grain: One row per product per order line item  
Business Process: Sales transactions

Measures:
- quantity_sold: Number of units sold
- unit_price: Price per unit at time of sale
- discount_amount: Discount applied on sale
- total_amount: Final sale amount

Foreign Keys:
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

DIMENSION TABLE: dim_date  
Purpose: Enables time-based analysis  
Type: Conformed dimension  

Attributes:
- date_key (PK): Surrogate key (YYYYMMDD)
- full_date
- day_of_week
- day_of_month
- month
- month_name
- quarter
- year
- is_weekend

DIMENSION TABLE: dim_product  
Purpose: Stores product attributes  

Attributes:
- product_key (PK)
- product_id
- product_name
- category
- subcategory
- unit_price

DIMENSION TABLE: dim_customer  
Purpose: Stores customer attributes  

Attributes:
- customer_key (PK)
- customer_id
- customer_name
- city
- state
- customer_segment

---

## Section 2: Design Decisions (150 words)

The grain of the fact table is defined at the transaction line-item level to capture detailed sales activity. This allows flexible analysis such as product-wise, customer-wise, and time-based reporting. Surrogate keys are used instead of natural keys to improve performance, maintain historical accuracy, and handle changes in source system keys.

This star schema supports efficient OLAP operations such as drill-down and roll-up. Analysts can drill down from yearly sales to quarterly or monthly levels using the date dimension. Roll-up operations are also supported by aggregating measures across dimensions. The simple structure of a star schema reduces join complexity and improves query performance.

---

## Section 3: Sample Data Flow

Source Transaction:  
Order #101, Customer "John Doe", Product "Laptop", Qty: 2, Price: 50000

Data Warehouse Representation:

fact_sales:
- date_key: 20240115
- product_key: 5
- customer_key: 12
- quantity_sold: 2
- unit_price: 50000
- total_amount: 100000

dim_date: {20240115, 2024-01-15, January, Q1}  
dim_product: {Laptop, Electronics}  
dim_customer: {John Doe, Mumbai}
