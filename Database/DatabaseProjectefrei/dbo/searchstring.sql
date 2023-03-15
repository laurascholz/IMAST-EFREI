CREATE TABLE [dbo].[searchstring] (
    [id]            INT            IDENTITY (1, 1) NOT NULL,
    [search_string] VARCHAR (2000) NOT NULL,
    [search_date]   DATETIME       DEFAULT (getdate()) NOT NULL,
    [website_name]  VARCHAR (100)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

