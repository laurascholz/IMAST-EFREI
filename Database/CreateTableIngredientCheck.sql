-- Create a new table called 'ingredientscheck' 
-- Drop the table if it already exists
IF OBJECT_ID('ingredientscheck', 'U') IS NOT NULL
DROP TABLE ingredientscheck
GO

-- Create the table 
CREATE TABLE ingredientscheck
(
   ingredientslist_id INT NOT NULL,
   badingredients_id INT NOT NULL,
   CONSTRAINT FK_ingredientscheck_ingredientslist FOREIGN KEY (ingredientslist_id) REFERENCES ingredientslist(id),
   CONSTRAINT FK_ingredientscheck_badingredients FOREIGN KEY (badingredients_id) REFERENCES badingredients(id)
);

