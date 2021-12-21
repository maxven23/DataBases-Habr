WITH CompaniesWithAdmins AS (
    SELECT company_id, u.user_id, u.login, u.status, u.registration_date
    FROM users_is_in_company
    JOIN users u on users_is_in_company.user_id = u.user_id
    WHERE u.status IN ('Administrator', 'Editor', 'Moderator')
), Counting AS (
    SELECT CWA.user_id, c.name, COUNT(CWA.status) AS adm_count, DATE_PART('day', NOW() - CWA.registration_date) AS Experience_in_days
    FROM CompaniesWithAdmins CWA
    JOIN company c on CWA.company_id=c.company_id
    WHERE CWA.registration_date < '01-01-2018'
    GROUP BY CWA.user_id, c.name, CWA.registration_date
)
SELECT *
FROM Counting
ORDER BY Experience_in_days DESC, user_id;