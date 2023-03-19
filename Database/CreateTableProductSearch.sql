-- Create a new table called 'productsearch' 
-- Drop the table if it already exists
IF OBJECT_ID('productsearch', 'U') IS NOT NULL
DROP TABLE productsearch
GO

-- Create the table
CREATE TABLE productsearch
(
    product_id INT NOT NULL,
    searchstring_id INT NOT NULL,
    product_name VARCHAR(1000) NOT NULL, 
    CONSTRAINT FK_productsearch_product FOREIGN KEY (product_id) REFERENCES product(id),
    CONSTRAINT FK_productsearch_searchstring FOREIGN KEY (searchstring_id) REFERENCES searchstring(id)
);
