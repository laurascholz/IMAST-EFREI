-- Create a new table called 'product' 
-- Drop the table if it already exists
IF OBJECT_ID('product', 'U') IS NOT NULL
DROP TABLE product
GO

-- Create the table
CREATE TABLE product
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    ingredientslist_id INT,
    api_id INT NOT NULL,
    product_name VARCHAR(500) NOT NULL,
    product_brand VARCHAR(500) NOT NULL,
    product_price VARCHAR(100) NOT NULL,
    product_link VARCHAR(1000) NOT NULL,
    product_image VARCHAR(1000) NOT NULL,
    CONSTRAINT FK_product_ingredientslist FOREIGN KEY (ingredientslist_id) REFERENCES ingredientslist(id)
);