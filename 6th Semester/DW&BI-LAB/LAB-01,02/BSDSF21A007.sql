
/*
.##.....##.........######...#######..########.....###....##....##.......###....##....##.......##.##.....##.##.....##
.###...###........##....##.##.....##.##.....##...##.##...###...##......##.##...###...##.......##.##.....##.###...###
.####.####........##.......##.....##.##.....##..##...##..####..##.....##...##..####..##.......##.##.....##.####.####
.##.###.##.........######..##.....##.########..##.....##.##.##.##....##.....##.##.##.##.......##.##.....##.##.###.##
.##.....##..............##.##.....##.##.....##.#########.##..####....#########.##..####.##....##.##.....##.##.....##
.##.....##.###....##....##.##.....##.##.....##.##.....##.##...###....##.....##.##...###.##....##.##.....##.##.....##
.##.....##.###.....######...#######..########..##.....##.##....##....##.....##.##....##..######...#######..##.....##
*/




/*
.########....###.....######..##....##.....#######.
....##......##.##...##....##.##...##.....##.....##
....##.....##...##..##.......##..##.............##
....##....##.....##..######..#####........#######.
....##....#########.......##.##..##.............##
....##....##.....##.##....##.##...##.....##.....##
....##....##.....##..######..##....##.....#######.
*/

--1:	Select the names of employees who are working in Region A.

select concat(Employees.FirstName,' ',Employees.LastName) as Employee_Name
from Employees
where Employees.Region like '%A';


--2:	Count the number of employees working in Territory A.

select count (Employees.EmployeeID) as Count_of_Employees
from Employees
join EmployeeTerritories on employees.EmployeeID = EmployeeTerritories.EmployeeID
join Territories on EmployeeTerritories.TerritoryID = Territories.TerritoryID
where territories.TerritoryDescription like ('%A%');


--3:	Find the names of employees who were hired before the age of 21 years.

select concat(Employees.FirstName,' ',Employees.LastName) as Employee_Name
from Employees
where Employees.HireDate-Employees.BirthDate<21;

--4:	Show the distribution of products in each category.

select c.CategoryName,count(p.ProductName) as Product_Count
from Products as p
join Categories as c on p.CategoryID = c.CategoryID
group by C.CategoryName


--5:	Compute the number of orders which included suppliers from Lahore and where shipped to Islamabad. 

select count(*) as Order_Count
from Orders as ORD
join [Order Details] as od on ord.orderID = od.OrderID
join products as p on p.productID = od.ProductID
join suppliers as s on s.supplierID = p.supplierID
where s.City='Lahore'
and ord.ShipCity='Islamabad';

/*
.########....###.....######..##....##....##.......
....##......##.##...##....##.##...##.....##....##.
....##.....##...##..##.......##..##......##....##.
....##....##.....##..######..#####.......##....##.
....##....#########.......##.##..##......#########
....##....##.....##.##....##.##...##...........##.
....##....##.....##..######..##....##..........##.
*/

--1:	What is the total amount of discount offered during the last month and compare it with the discount in June last year? 

SELECT SUM(od.Discount) AS TotalDiscountLastMonth
FROM [Order Details] as od
JOIN Orders o 
ON od.OrderID = o.OrderID
WHERE o.OrderDate >= DATEADD(MONTH, DATEDIFF(MONTH, 0, (select max(orderdate) from orders)) - 1, 0)
AND o.OrderDate < DATEADD(MONTH, DATEDIFF(MONTH, 0, (select max(orderdate) from orders)), 0);


SELECT UM(od.Discount) AS Total_Discount_June_Last_Year
FROM [Order Details] as od
JOIN Orders o 
ON od.OrderID = o.OrderID
WHERE o.OrderDate >= (select max(orderdate) from orders where month(OrderDate)=6)

--2:	Give a report of the products that were sold the most in the last year

SELECT 
TOP 1 p.ProductName, SUM(od.Quantity) AS Total_Quantity_Sold
FROM [Order Details] od
JOIN Orders o 
ON o.OrderId = od.OrderId
JOIN Products p 
ON p.ProductId = od.ProductId
GROUP BY p.ProductName
ORDER BY Total_Quantity_Sold DESC;


--3:	How many products of supplier 2 were shipped by shipper 3 to customers in Faisalabad? And compare it with that of Karachi

SELECT
    (SELECT COUNT(*) 
    FROM [Order Details] od
    JOIN Orders o 
    ON o.OrderId = od.OrderId
    JOIN Products p 
    ON p.ProductId = od.ProductId
    JOIN Suppliers s 
    ON s.SupplierId = p.SupplierId
    JOIN Shippers sh 
    ON sh.ShipperId = o.OrderId
    JOIN Customers c 
    ON c.CustomerId = o.CustomerId
    WHERE s.SupplierId = 2
    AND sh.ShipperId = 3
    AND c.City = 'Faisalabad') AS Products_to_Faisalabad,

    (SELECT COUNT(*) 
    FROM [Order Details] as od
    JOIN Orders o 
    ON o.OrderId = od.OrderId
    JOIN Products p 
    ON p.ProductId = od.ProductId
    JOIN Suppliers s 
    ON s.SupplierId = p.SupplierId
    JOIN Shippers sh 
    ON sh.ShipperId = o.OrderId
    JOIN Customers c 
    ON c.CustomerId = o.CustomerId
    WHERE s.SupplierId = 2
    AND sh.ShipperId = 3
    AND c.City = 'Karachi') AS Products_to_Karachi;


--4:    Give a report of the month wise distribution of orders placed from Lahore

SELECT p.ProductName, SUM(od.Quantity) AS Total_Quantity_Sold
FROM [Order Details] as od
JOIN Orders o 
N o.OrderId = od.OrderId
JOIN Products p 
ON p.ProductId = od.ProductId
WHERE o.OrderDate >= DATEADD(year, -1, GETDATE())
GROUP BY p.ProductName
ORDER BY TotalQuantitySold DESC;


--5:    Which product was sold the most?

SELECT 
TOP 1 p.ProductName,SUM(od.Quantity) AS TotalQuantitySold
FROM [Order Details] od
JOIN Orders as o 
ON o.OrderId = od.OrderId
JOIN Products p 
ON p.ProductId = od.ProductId
GROUP BY p.ProductName
ORDER BY TotalQuantitySold DESC;


--6:	Compare the products that were sold the most in different regions

SELECT c.Region, p.ProductName, SUM(od.Quantity) AS TotalQuantitySold
FROM [Order Details] as od
JOIN Orders as o 
ON o.OrderId = od.OrderId
JOIN Products as p
ON p.ProductId = od.ProductId
JOIN Customers as c 
ON c.CustomerId = o.CustomerId
GROUP BY c.Region, p.ProductName
ORDER BY c.Region, TotalQuantitySold�DESC;


--7:	Compute the amount of the product delivered by shippers during the first quarter of the year 2024 in the region of Lahore and compared its performance with that of the last year.

select distinct(ShipRegion)
from orders

SELECT s.ShipperID, s.CompanyName, SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS TotalAmount2024
FROM Orders as o
JOIN [Order Details] as od 
ON o.OrderID = od.OrderID
JOIN Shippers s ON o.ShipVia = s.ShipperID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.ShipRegion = 'Lahore'
AND o.ShippedDate BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY s.ShipperID, s.CompanyName;

SELECT s.ShipperID, s.CompanyName, SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS TotalAmount2023
FROM Orders as o
JOIN [Order Details] od ON o.OrderID = od.OrderID
JOIN Shippers s ON o.ShipVia = s.ShipperID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.ShipRegion = 'Lahore'
AND o.ShippedDate BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY s.ShipperID, s.CompanyName;

--8:	Identify the products that are sold the most in cold and hot weathers.

SELECT 
Top 1 p.ProductID, p.ProductName, SUM(od.Quantity) AS Total_Quantity_Sold_in_Cold
FROM Orders as o
JOIN [Order Details] as od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE MONTH(o.OrderDate) IN (12, 1, 2)
GROUP BY p.ProductID, p.ProductName
ORDER BY Total_Quantity_Sold_in_Cold DESC


SELECT 
Top 1 p.ProductID, p.ProductName, SUM(od.Quantity) AS Total_Quantity_Sold_in_Hot
FROM Orders as o
JOIN [Order Details] as od 
ON o.OrderID = od.OrderID
JOIN Products as p 
ON od.ProductID = p.ProductID
WHERE MONTH(o.OrderDate) IN (6, 7, 8)
GROUP BY p.ProductID, p.ProductName
ORDER BY Total_Quantity_Sold_in_Hot DESC;



--9:	Show the distribution of the discount offered on the suppliers from different cities during the year 2024.

SELECT s.City,SUM(od.Quantity * od.UnitPrice * od.Discount) AS Total_Discount
FROM Orders as o
JOIN [Order Details] as od ON o.OrderID = od.OrderID
JOIN Products as p ON od.ProductID = p.ProductID
JOIN Suppliers as s ON p.SupplierID = s.SupplierID
WHERE o.OrderDate BETWEEN '1997-01-01' AND '1998-12-31'
GROUP BY s.City
ORDER BY TotalDiscount DESC;




--10:	Select the products, the names of suppliers who bought the products that fall in the category of cosmetics and were shipped on 1 January 2024. Also, compare the performance of each month is same report.

SELECT p.ProductName, s.CompanyName AS SupplierName
FROM Products AS p
JOIN Suppliers as s ON p.SupplierID = s.SupplierID
JOIN Categories as c ON p.CategoryID = c.CategoryID
JOIN [Order Details] od ON p.ProductID = od.ProductID
JOIN Orders as o ON od.OrderID = o.OrderID
WHERE c.CategoryName = 'Cosmetics'
AND o.ShippedDate = '2024-01-01';


SELECT DATEPART(YEAR, OrderDate) AS OrderYear, DATEPART(MONTH, OrderDate) AS OrderMonth, SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS TotalSalesAmount
FROM Orders as o
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY DATEPART(YEAR, OrderDate), DATEPART(MONTH, OrderDate)
ORDER BY OrderYear, OrderMonth;
