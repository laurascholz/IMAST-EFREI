CREATE TABLE ingredientslist
(
    id INT NOT NULL PRIMARY KEY IDENTITY(1,1), -- primary key column
    ingredientslist_name VARCHAR(100) NOT NULL,
    ingredientslist_string VARCHAR(2000) NOT NULL,
    ingredientslist_score VARCHAR(100)

);