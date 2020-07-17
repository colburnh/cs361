CREATE TABLE [dbo].[Classes] (
    [ClassId]        INT           IDENTITY (1, 1) NOT NULL,
    [Name]           VARCHAR (255) NOT NULL,
    [Year1Type]      INT           NULL,
    [Year2Type]      INT           NULL,
    [Year3Type]      INT           NULL,
    [Year4Type]      INT           NULL,
    [Year5Type]      INT           NULL,
    [Year6Type]      INT           NULL,
    [Year7Type]      INT           NULL,
    [Location]       VARCHAR (255) NULL,
    [MaxCapacity]    INT           NULL,
    [NumberOfHouses] INT           NULL,
    PRIMARY KEY CLUSTERED ([ClassId] ASC),
    FOREIGN KEY ([Year1Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year2Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year3Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year4Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year5Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year6Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID]),
    FOREIGN KEY ([Year7Type]) REFERENCES [dbo].[ClassYearType] ([ClassYearTypeID])
);

