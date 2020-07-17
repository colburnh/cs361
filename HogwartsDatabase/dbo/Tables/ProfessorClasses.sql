CREATE TABLE [dbo].[ProfessorClasses] (
    [ProfessorClassID] INT IDENTITY (1, 1) NOT NULL,
    [ProfessorID]      INT NOT NULL,
    [ClassID]          INT NOT NULL,
    PRIMARY KEY CLUSTERED ([ProfessorClassID] ASC),
    FOREIGN KEY ([ClassID]) REFERENCES [dbo].[Classes] ([ClassId]),
    FOREIGN KEY ([ProfessorID]) REFERENCES [dbo].[Professors] ([ProfessorID])
);

