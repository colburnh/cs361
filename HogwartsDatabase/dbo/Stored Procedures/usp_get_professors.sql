CREATE PROCEDURE [dbo].[usp_get_professors]
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	SELECT 
		*
	FROM
		Professors

END
