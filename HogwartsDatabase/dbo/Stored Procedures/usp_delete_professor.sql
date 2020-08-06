CREATE PROCEDURE [dbo].[usp_delete_professor]
	@ProfessorID varchar(255)

AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	DELETE FROM 
		dbo.Professors
	WHERE
		ProfessorID = @ProfessorID

END
