-- Create a new table called 'ingredientslist' 
-- Drop the table if it already exists
IF OBJECT_ID('ingredientslist', 'U') IS NOT NULL
DROP TABLE ingredientslist
GO

-- Create the table
CREATE TABLE ingredientslist
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    ingredientslist_name VARCHAR(500) NOT NULL,
    ingredientslist_string NVARCHAR(4000) NOT NULL,
    ingredientslist_harmfull INT,
    ingredientslist_harmless INT,

);