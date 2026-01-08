USE fleximart_dw;

INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,0),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,0);

INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Laptop','Electronics','Computers',50000),
('P002','Headphones','Electronics','Audio',3000);

INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','John Doe','Mumbai','MH','Retail'),
('C002','Jane Smith','Delhi','DL','Retail');

INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240101,1,1,2,50000,0,100000),
(20240201,2,2,3,3000,0,9000);
