/*
Post-Deployment Script Template							
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be appended to the build script.		
 Use SQLCMD syntax to include a file in the post-deployment script.			
 Example:      :r .\myfile.sql								
 Use SQLCMD syntax to reference a variable in the post-deployment script.		
 Example:      :setvar TableName MyTable							
               SELECT * FROM [$(TableName)]					
--------------------------------------------------------------------------------------
*/
:r .\dbo.ClassYearType.Table.sql
GO
:r .\dbo.Houses.Table.sql
GO
:r .\dbo.Professors.Table.sql
GO
:r .\dbo.Classes.Table.sql
GO
:r .\dbo.Students.Table.sql
GO
:r .\dbo.ProfessorClasses.Table.sql
GO
:r .\dbo.ScheduledClasses.Table.sql
GO
:r .\dbo.ScheduledClassesStudent.Table.sql
GO