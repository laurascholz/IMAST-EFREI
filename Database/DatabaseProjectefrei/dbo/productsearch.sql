CREATE TABLE [dbo].[productsearch] (
    [product_id]      INT NOT NULL,
    [searchstring_id] INT NOT NULL,
    CONSTRAINT [FK_productsearch_product] FOREIGN KEY ([product_id]) REFERENCES [dbo].[product] ([id]),
    CONSTRAINT [FK_productsearch_searchstring] FOREIGN KEY ([searchstring_id]) REFERENCES [dbo].[searchstring] ([id])
);


GO

