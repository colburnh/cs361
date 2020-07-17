CREATE TABLE [dbo].[ScheduledClassesStudent] (
    [ScheduledClassesStudentID] INT IDENTITY (1, 1) NOT NULL,
    [ScheduledClassID]          INT NOT NULL,
    [StudentID]                 INT NOT NULL,
    PRIMARY KEY CLUSTERED ([ScheduledClassesStudentID] ASC),
    FOREIGN KEY ([ScheduledClassID]) REFERENCES [dbo].[ScheduledClasses] ([ScheduledClassID]),
    FOREIGN KEY ([StudentID]) REFERENCES [dbo].[Students] ([StudentID])
);

