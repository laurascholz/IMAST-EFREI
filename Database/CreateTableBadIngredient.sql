-- Create a new table called 'badingredients' 
-- Drop the table if it already exists
IF OBJECT_ID('badingredients', 'U') IS NOT NULL
DROP TABLE badingredients
GO

-- Create the table 
CREATE TABLE badingredients
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    ingredient_name VARCHAR(100) NOT NULL,
    explanation_bad VARCHAR(100),
    source_bad VARCHAR(100)
    
);