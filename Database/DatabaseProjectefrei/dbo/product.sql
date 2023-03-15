CREATE TABLE [dbo].[product] (
    [id]                 INT            IDENTITY (1, 1) NOT NULL,
    [ingredientslist_id] INT            NULL,
    [api_id]             INT            NOT NULL,
    [product_name]       VARCHAR (1000) NOT NULL,
    [product_brand]      VARCHAR (1000) NOT NULL,
    [product_price]      VARCHAR (100)  NOT NULL,
    [product_link]       VARCHAR (2000) NOT NULL,
    [product_image]      VARCHAR (2000) NOT NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_product_ingredientslist] FOREIGN KEY ([ingredientslist_id]) REFERENCES [dbo].[ingredientslist] ([id])
);


GO

