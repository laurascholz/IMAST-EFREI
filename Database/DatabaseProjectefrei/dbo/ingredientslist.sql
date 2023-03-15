CREATE TABLE [dbo].[ingredientslist] (
    [id]                       INT             IDENTITY (1, 1) NOT NULL,
    [ingredientslist_name]     VARCHAR (1000)  NOT NULL,
    [ingredientslist_string]   NVARCHAR (4000) NOT NULL,
    [ingredientslist_harmfull] INT             NULL,
    [ingredientslist_harmless] INT             NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

