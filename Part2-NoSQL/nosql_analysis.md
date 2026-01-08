# NoSQL Database Analysis for FlexiMart

## Section A: Limitations of RDBMS 
Relational databases like MySQL are designed with a fixed schema, which makes them less suitable for handling highly diverse product catalogs. In FlexiMart’s case, different product categories have different attributes. For example, electronic products require specifications such as RAM, processor, and storage, while footwear products require size, color, and material. Representing these varying attributes in a relational database would require many nullable columns or multiple related tables, leading to complexity and inefficiency.

Frequent schema changes are another limitation. Whenever a new product type with new attributes is introduced, the database schema must be altered. This process is time-consuming, risky for existing data, and can cause downtime.

Additionally, storing customer reviews as nested data is difficult in relational databases. Reviews must be stored in separate tables and joined with products, making queries more complex and reducing performance for read-heavy operations.

---

## Section B: Benefits of MongoDB 

MongoDB is well suited for FlexiMart’s expanding product catalog due to its flexible schema design. Each product is stored as a document, allowing different products to have different fields without requiring schema changes. This makes it easy to add new product categories with unique attributes.

MongoDB supports embedded documents, which allows customer reviews to be stored directly within the product document. This improves read performance and simplifies queries, as product and review data can be retrieved together without joins.

Horizontal scalability is another key advantage. MongoDB can easily scale across multiple servers using sharding, making it suitable for handling large volumes of product data and high user traffic. These features make MongoDB a strong choice for managing diverse, evolving product catalogs efficiently.

---

## Section C: Trade-offs of Using MongoDB 

One disadvantage of MongoDB is the lack of strong relational integrity. Unlike MySQL, MongoDB does not enforce foreign key constraints, which can lead to data inconsistency if not handled carefully at the application level.

Another drawback is that complex transactional operations are harder to manage. While MongoDB supports transactions, they are generally more complex and less efficient compared to relational databases. This makes MongoDB less suitable for scenarios requiring strict ACID compliance, such as financial transactions or order processing systems.
