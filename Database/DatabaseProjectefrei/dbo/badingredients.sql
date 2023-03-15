CREATE TABLE [dbo].[badingredients] (
    [id]              INT            IDENTITY (1, 1) NOT NULL,
    [chemical_name]   VARCHAR (8000) NOT NULL,
    [ingredient_name] VARCHAR (8000) NOT NULL,
    [explanation]     VARCHAR (100)  NULL,
    [source]          VARCHAR (500)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

