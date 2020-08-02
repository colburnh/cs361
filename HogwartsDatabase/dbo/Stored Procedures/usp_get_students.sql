CREATE PROCEDURE [dbo].[usp_get_students]
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	SELECT 
		*
	FROM
		Students

END
