CREATE TABLE [dbo].[ingredientscheck] (
    [ingredientslist_id] INT NOT NULL,
    [badingredients_id]  INT NOT NULL,
    CONSTRAINT [FK_ingredientscheck_badingredients] FOREIGN KEY ([badingredients_id]) REFERENCES [dbo].[badingredients] ([id]),
    CONSTRAINT [FK_ingredientscheck_ingredientslist] FOREIGN KEY ([ingredientslist_id]) REFERENCES [dbo].[ingredientslist] ([id])
);


GO

