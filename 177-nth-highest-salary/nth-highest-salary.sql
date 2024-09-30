-- -CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- -BEGIN
-- -  RETURN (
-- -      # Write your MySQL query statement below.
-- -
-- -  );
-- -END
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
    RETURN (
        SELECT 
            distinct salary
        from Employee 
        order by salary desc
        limit 1 offset N
    );
END