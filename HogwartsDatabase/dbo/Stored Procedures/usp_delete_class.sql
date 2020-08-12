CREATE PROCEDURE [dbo].[usp_delete_class]
	@ClassID varchar(255)

AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	DELETE FROM 
		dbo.Classes 
	WHERE
		ClassID = @ClassID

END
