-- Create a new table called 'searchstring' 
-- Drop the table if it already exists
IF OBJECT_ID('searchstring', 'U') IS NOT NULL
DROP TABLE searchstring
GO

-- Create the table
CREATE TABLE searchstring
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    search_string VARCHAR(1000) NOT NULL,
    search_date datetime default CURRENT_TIMESTAMP NOT NULL,
    website_name VARCHAR(100)

);