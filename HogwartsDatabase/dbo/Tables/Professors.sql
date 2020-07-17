CREATE TABLE [dbo].[Professors] (
    [ProfessorID] INT           IDENTITY (1, 1) NOT NULL,
    [LastName]    VARCHAR (255) NOT NULL,
    [FirstName]   VARCHAR (255) NOT NULL,
    [Active]      INT           NOT NULL,
    PRIMARY KEY CLUSTERED ([ProfessorID] ASC)
);

