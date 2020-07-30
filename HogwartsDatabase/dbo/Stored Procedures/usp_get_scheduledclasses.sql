CREATE PROCEDURE [dbo].[usp_get_scheduledclasses]
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	SELECT 
		*
	FROM
		ScheduledClasses

END
