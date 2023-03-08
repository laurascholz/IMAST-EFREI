-- Create a new table called 'badingredients' 
-- Drop the table if it already exists
IF OBJECT_ID('badingredients', 'U') IS NOT NULL
DROP TABLE badingredients
GO

-- Create the table 
CREATE TABLE badingredients
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    chemical_name VARCHAR(8000) NOT NULL,
    ingredient_name VARCHAR(8000),
    product_type VARCHAR(1000),
    explanation VARCHAR(100),
    source VARCHAR(100)
    
);