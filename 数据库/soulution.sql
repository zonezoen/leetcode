-- 176. 第二高的薪水
-- https://leetcode-cn.com/problems/second-highest-salary/
SELECT IFNULL((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1,1),null) as SecondHigherstSalary;

-- 180. 连续出现的数字
-- https://leetcode-cn.com/problems/consecutive-numbers/
SELECT DISTINCT l1.Num as ConsecutiveNums FROM Logs l1, Logs l2, Logs l3 WHERE l1.id = l2.id -1 AND l2.id = l3.id - 1 AND l1.Num = l2.Num AND l2.Num = l3.Num

-- 177. 第N高的薪水
-- https://leetcode-cn.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1;
RETURN(SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET N);
END


-- 181. 超过经理收入的员工
-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/
SELECT e1.name as Employee FROM Employee e1, Employee e2 WHERE e1.Salary > e2.Salary AND e1.ManagerId = e2.Id;

-- 182. 查找重复的电子邮箱
-- https://leetcode-cn.com/problems/duplicate-emails/
SELECT DISTINCT p1.Email FROM Person p1,Person p2 WHERE p1.Email = p2.Email AND p1.Id != p2.Id

-- 183. 从不订购的客户
-- https://leetcode-cn.com/problems/customers-who-never-order/
SELECT DISTINCT c.name as Customers FROM Customers c JOIN Orders o WHERE c.Id != o.CustomerId
SELECT c.name as Customers FROM Customers c,Orders o WHERE c.Id != o.CustomerId
SELECT a.Name AS Customers FROM Customersa WHERE a.Id NOT IN (SELECT CustomerId FROM Orders)


-- 184. 部门工资最高的员工
-- https://leetcode-cn.com/problems/department-highest-salary/
-- SELECT d.name as Department,e.name as Employee,e.Salary as Salary FROM Employee e LEFT JOIN Department d ON e.DepartmentId = d.Id ORDER BY e.Salary GROUP BY d.name
select d.name as Department, e.name as Employee, salary
from employee e
join department d
on e.departmentid = d.id
where (e.departmentid, e.salary) in
(
    select e.departmentid, max(salary)
    from employee e
    group by e.departmentid
);


-- 185. 部门工资前三高的员工
-- https://leetcode-cn.com/problems/department-top-three-salaries/
select B.Name as Department, A.Name as Employee, A.Salary
from Employee A, Department B
where A.DepartmentId = B.Id
and 3>(select count(distinct Salary) from Employee
                    where DepartmentId=B.Id and Salary>A.Salary)
order by B.Name asc, A.Salary desc


-- 196. 删除重复的电子邮箱
-- https://leetcode-cn.com/problems/delete-duplicate-emails/
DELETE p2 FROM Person p1 JOIN Person p2 ON p1.Email = p2.Email WHERE p2.Id > p1.Id

-- 197. 上升的温度
-- https://leetcode-cn.com/problems/rising-temperature/
SELECT w2.Id FROM Weather w1,Weather w2 WHERE w2.Temperature>w1.Temperature AND datediff(w1.RecordDate,w2.RecordDate)=1


-- 596. 超过5名学生的课
-- https://leetcode-cn.com/problems/classes-more-than-5-students/
SELECT DISTINCT c.class FROM courses c
WHERE 5>(SELECT COUNT(class) FROM courses WHERE student=c.student)

SELECT class from courses group by class having count(DISTINCT student) >= 5;

























