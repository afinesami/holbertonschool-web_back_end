-- SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
AND (students.last_meeting IS NULL OR students.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));
