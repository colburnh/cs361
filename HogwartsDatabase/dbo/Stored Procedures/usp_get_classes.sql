﻿CREATE PROCEDURE [dbo].[usp_get_classes]
AS
BEGIN

	SET XACT_ABORT ON;
	SET NOCOUNT ON;

	SELECT 
		*
	FROM
		Classes

END
