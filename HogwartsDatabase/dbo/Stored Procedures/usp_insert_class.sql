CREATE PROCEDURE [dbo].[usp_insert_class]
	@Name varchar(255), 
	@Year1Type int, 
	@Year2Type int,
	@Year3Type int, 
	@Year4Type int, 
	@Year5Type int,
	@Year6Type int, 
	@Year7Type int, 
	@location VARCHAR(255),
	@MaxCapacity int, 
	@NumberOfHouses int

AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	INSERT INTO 
		dbo.Classes (Name, Year1Type, Year2Type, Year3Type, Year4Type, Year5Type, Year6Type, Year7Type, Location, MaxCapacity, NumberOfHouses)
	VALUES
		(@Name, @Year1Type, @Year2Type, @Year3Type, @Year4Type, @Year5Type, @Year6Type, @Year7Type, @Location, @MaxCapacity, @NumberOfHouses)

END
