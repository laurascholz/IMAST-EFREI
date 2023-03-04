-- Create a new table called 'ingredientslist' 
-- Drop the table if it already exists
IF OBJECT_ID('ingredientslist', 'U') IS NOT NULL
DROP TABLE ingredientslist
GO

-- Create the table
CREATE TABLE ingredientslist
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    ingredientslist_name VARCHAR(100) NOT NULL,
    ingredientslist_string VARCHAR(8000) NOT NULL,
    ingredientslist_score VARCHAR(100)

);