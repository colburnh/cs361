CREATE PROCEDURE [dbo].[usp_delete_student]
	@StudentID varchar(255)

AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	DELETE FROM 
		dbo.Students
	WHERE
		StudentID = @StudentID

END
