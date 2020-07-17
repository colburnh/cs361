CREATE TABLE [dbo].[ScheduledClasses] (
    [ScheduledClassID] INT           IDENTITY (1, 1) NOT NULL,
    [ProfessorClassID] INT           NOT NULL,
    [HouseID]          INT           NOT NULL,
    [StartTime]        TIME (7)      NULL,
    [EndTime]          TIME (7)      NULL,
    [DaysoftheWeek]    VARCHAR (255) NULL,
    [Year]             VARCHAR (255) NULL,
    [MaxOccupancy]     INT           NULL,
    [Occupancy]        INT           NULL,
    [RemainingSpots]   INT           NULL,
    [Location]         VARCHAR (255) NULL,
    PRIMARY KEY CLUSTERED ([ScheduledClassID] ASC),
    FOREIGN KEY ([HouseID]) REFERENCES [dbo].[Houses] ([HouseID]),
    FOREIGN KEY ([ProfessorClassID]) REFERENCES [dbo].[ProfessorClasses] ([ProfessorClassID])
);

