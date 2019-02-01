CREATE DATABASE IF NOT EXISTS sales_series;
USE sales_series;
CREATE TABLE datasales 
(
    model VARCHAR(20) NOT NULL,
    sales_date DATE NOT NULL,
    sales INT,
    date_year CHAR(4) NOT NULL,
    date_month VARCHAR(2) NOT NULL
    );
