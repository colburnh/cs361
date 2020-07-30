CREATE PROCEDURE [dbo].[usp_insert_student]
	@LastName varchar(255),
	@FirstName varchar(255),
	@HouseID int,
	@Year int,
	@ElectiveOneID int,
	@ElectiveTwoID int

AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	INSERT INTO 
		dbo.Students (LastName, FirstName, HouseID, Year, ElectiveOneID, ElectiveTwoID)
	VALUES
		(@LastName, @FirstName, @HouseID, @Year, @ElectiveOneID, @ElectiveTwoID)

END
