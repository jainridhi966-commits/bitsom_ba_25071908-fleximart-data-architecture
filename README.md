# FlexiMart Data Architecture Project

**Student Name:** RIDHI JAIN
**Student ID:** bitsom_ba_25071908
**Email:** jainridhi966@gmail.com
**Date:** 8th January,2026

## Project Overview

This project implements an end-to-end data architecture solution for FlexiMart. It includes relational database design with an ETL pipeline, NoSQL analysis using MongoDB for flexible product catalogs, and a data warehouse built using a star schema to support analytical business queries.

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.x, pandas, mysql-connector-python
- MySQL 8.0 / PostgreSQL 14
- MongoDB 6.0

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

This project improved my understanding of end-to-end data pipelines, including data cleaning, transformation, and loading into relational databases. I learned how NoSQL databases like MongoDB handle flexible schemas and nested data more efficiently. Additionally, designing a star schema and writing analytical SQL queries strengthened my knowledge of data warehousing concepts.

## Challenges Faced

1.Handling duplicate and inconsistent data during the ETL process, which was resolved through data validation and de-duplication logic.

2.Managing schema differences between relational and NoSQL databases, which was addressed by using document-based modeling in MongoDB.
