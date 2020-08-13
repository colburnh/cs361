CREATE PROCEDURE [dbo].[usp_get_scheduledclasses]
	@year int
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	SELECT 
		sc.ScheduledClassID,
		p.LastName AS 'Professor',
		c.Name AS 'Class',
		h.HouseName AS 'House',
		StartTime,
		EndTime,
		DaysoftheWeek,
		Year
	FROM 
		ScheduledClasses sc
		JOIN ProfessorClasses pc
			ON sc.ProfessorClassID = pc.ProfessorClassID
		JOIN Classes c
			ON pc.ClassID = c.ClassId
		JOIN Professors p
			ON pc.ProfessorID = p.ProfessorID
		JOIN Houses h
			ON sc.HouseID = h.HouseID
	WHERE
		Year = @year
	ORDER BY 
		StartTime

END
