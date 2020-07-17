CREATE TABLE [dbo].[Students] (
    [StudentID]     INT           IDENTITY (1, 1) NOT NULL,
    [LastName]      VARCHAR (255) NOT NULL,
    [FirstName]     VARCHAR (255) NOT NULL,
    [HouseID]       INT           NOT NULL,
    [Year]          INT           NOT NULL,
    [ElectiveOneID] INT           NULL,
    [ElectiveTwoID] INT           NULL,
    PRIMARY KEY CLUSTERED ([StudentID] ASC),
    FOREIGN KEY ([ElectiveOneID]) REFERENCES [dbo].[Classes] ([ClassId]),
    FOREIGN KEY ([ElectiveTwoID]) REFERENCES [dbo].[Classes] ([ClassId]),
    FOREIGN KEY ([HouseID]) REFERENCES [dbo].[Houses] ([HouseID])
);

