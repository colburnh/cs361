CREATE PROCEDURE [dbo].[usp_insert_professor]
	@LastName varchar(255),
	@FirstName varchar(255),
	@Active int
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	INSERT INTO 
		dbo.Professors (LastName, FirstName, Active)
	VALUES
		(@FirstName, @LastName, @Active)

END
