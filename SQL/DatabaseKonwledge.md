# Data base knowledge

## Data pipeline

Data pipeline is to describe any set of process that move data from on system to another. Transforming may or may not be included. ETL Pipelines usually run in realtime.

## ETL pipeline

Interchangeable with data pipeline but usually more specific extract data from source, transforming and loading into output destination. ETL Pipelines usually run in batches.

## Data model

An abstract model that organizes elements of data and standardizes how they relate to one another and to the properties of real-world entities

There are three stages or types of data model (called schemas):

1. Conceptual: Pointing out organization’s informational needs rather than the structure of a database. WHAT the system containts.
2. Logical: Conveys the logical constraints that apply to the stored data. It may define integrity constraints, views, and tables. HOW the system should be implemented regardless of actual DBMS.
3. Physical: Show how data is stored physically on a storage system in terms of files and indices. HOW the system will be implemented using a speific DBMS system.

## Database Schema

Database schema design is a strategy for constructing a framework for data management. Database schema organize data into seperate entities as well as the relationships and constraints. The process of creating a database schema is called data modeling. [See more](https://www.guru99.com/star-snowflake-data-warehousing.html)

1. Star Schema
    - One fact table at the center and others are dimension tables
    - redundacny
    - one join at most
    - dimension table is not normalized
2. Snowflake Schema
    - One fact table and dimension table. The dimensional table has its additional dimension table
    - save space
    - lower performance
    - complex structure
    - normalized data structure
3. Galaxy Schema
    - two facts table, others are the same
4. Star Cluster Schema
    - between star schema and snowflake schema

## ER Diagram

Refers to entity relationship diagram, which reporesent the relationship between each entity sets in a database.

- How to build (Entities, Attributes & Relationships)
  - specify entities
  - relationship
  - Cardinality Identification (one to one one to many etc...)
  - identity attributes
