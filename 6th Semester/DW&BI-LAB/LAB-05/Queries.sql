-- Select monthly sales by customer state compared to those of the previous year
WITH MonthlySales AS (
    SELECT 
        t.Year,
        t.MonthNumber,
        st.StateName,
        SUM(s.SalesAmount) AS MonthlySalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Customer c ON s.CustomerKey = c.CustomerKey
        INNER JOIN City ct ON c.CityKey = ct.CityKey
        INNER JOIN State st ON ct.StateKey = st.StateKey
    GROUP BY 
        t.Year, t.MonthNumber, st.StateName
),
PreviousYearSales AS (
    SELECT 
        t.Year + 1 AS Year,
        t.MonthNumber,
        st.StateName,
        SUM(s.SalesAmount) AS PreviousYearSalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Customer c ON s.CustomerKey = c.CustomerKey
        INNER JOIN City ct ON c.CityKey = ct.CityKey
        INNER JOIN State st ON ct.StateKey = st.StateKey
    GROUP BY 
        t.Year, t.MonthNumber, st.StateName
)
SELECT 
    ms.Year,
    ms.MonthNumber,
    ms.StateName,
    ms.MonthlySalesAmount,
    pys.PreviousYearSalesAmount,
    ms.MonthlySalesAmount - pys.PreviousYearSalesAmount AS Difference
FROM 
    MonthlySales ms
    LEFT JOIN PreviousYearSales pys 
        ON ms.StateName = pys.StateName 
        AND ms.MonthNumber = pys.MonthNumber 
        AND ms.Year = pys.Year
ORDER BY 
    ms.Year, ms.MonthNumber, ms.StateName;

-- Monthly sales growth per product, that is, total sales per product compared to those of the previous month

WITH MonthlyProductSales AS (
    SELECT
        P.ProductKey,
        P.ProductName,
        T.Year,
        T.MonthNumber,
        SUM(S.SalesAmount) AS MonthlySales
    FROM
        Sales S
    JOIN
        Product P ON S.ProductKey = P.ProductKey
    JOIN
        Time T ON S.TimeKey = T.TimeKey
    GROUP BY
        P.ProductKey, P.ProductName, T.Year, T.MonthNumber
),
SalesWithPreviousMonth AS (
    SELECT
        MPS.ProductKey,
        MPS.ProductName,
        MPS.Year,
        MPS.MonthNumber,
        MPS.MonthlySales,
        LAG(MPS.MonthlySales, 1) OVER (
            PARTITION BY MPS.ProductKey, MPS.Year
            ORDER BY MPS.MonthNumber
        ) AS PreviousMonthSales
    FROM
        MonthlyProductSales MPS
)
SELECT
    SPM.ProductKey,
    SPM.ProductName,
    SPM.Year,
    SPM.MonthNumber,
    SPM.MonthlySales,
    SPM.PreviousMonthSales,
    CASE 
        WHEN SPM.PreviousMonthSales IS NOT NULL 
        THEN (SPM.MonthlySales - SPM.PreviousMonthSales) / SPM.PreviousMonthSales * 100
        ELSE NULL
    END AS MonthlyGrowthPercentage
FROM
    SalesWithPreviousMonth SPM
ORDER BY
    SPM.ProductKey, SPM.Year, SPM.MonthNumber;


--List the top three best-selling employees

WITH EmployeeSales AS (
    SELECT 
        e.EmployeeKey,
        e.FirstName,
        e.LastName,
        SUM(s.SalesAmount) AS TotalSalesAmount
    FROM 
        Sales s
        INNER JOIN Employee e ON s.EmployeeKey = e.EmployeeKey
    GROUP BY 
        e.EmployeeKey, e.FirstName, e.LastName
),
RankedEmployeeSales AS (
    SELECT 
        es.EmployeeKey,
        es.FirstName,
        es.LastName,
        es.TotalSalesAmount,
        RANK() OVER (ORDER BY es.TotalSalesAmount DESC) AS SalesRank
    FROM 
        EmployeeSales es
)
SELECT 
    EmployeeKey,
    FirstName,
    LastName,
    TotalSalesAmount
FROM 
    RankedEmployeeSales
WHERE 
    SalesRank <= 3
ORDER BY 
    SalesRank;

--Best-selling employee per product and year

WITH ProductYearSales AS (
    SELECT 
        t.Year,
        p.ProductName,
        e.EmployeeKey,
        e.FirstName,
        e.LastName,
        SUM(s.SalesAmount) AS TotalSalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Product p ON s.ProductKey = p.ProductKey
        INNER JOIN Employee e ON s.EmployeeKey = e.EmployeeKey
    GROUP BY 
        t.Year, p.ProductName, e.EmployeeKey, e.FirstName, e.LastName
),
RankedProductYearSales AS (
    SELECT 
        pys.Year,
        pys.ProductName,
        pys.EmployeeKey,
        pys.FirstName,
        pys.LastName,
        pys.TotalSalesAmount,
        RANK() OVER (PARTITION BY pys.Year, pys.ProductName ORDER BY pys.TotalSalesAmount DESC) AS SalesRank
    FROM 
        ProductYearSales pys
)
SELECT 
    Year,
    ProductName,
    EmployeeKey,
    FirstName,
    LastName,
    TotalSalesAmount
FROM 
    RankedProductYearSales
WHERE 
    SalesRank = 1
ORDER BY 
    Year, ProductName;

--Countries that account for top 50% of sales amount

WITH CountrySales AS (
    SELECT 
        co.CountryName,
        SUM(s.SalesAmount) AS TotalSalesAmount
    FROM 
        Sales s
        INNER JOIN Customer c ON s.CustomerKey = c.CustomerKey
        INNER JOIN City ci ON c.CityKey = ci.CityKey
        INNER JOIN Country co ON ci.CountryKey = co.CountryKey
    GROUP BY 
        co.CountryName
),
TotalSales AS (
    SELECT 
        SUM(TotalSalesAmount) AS TotalSales
    FROM 
        CountrySales
),
CumulativeSales AS (
    SELECT 
        cs.CountryName,
        cs.TotalSalesAmount,
        SUM(cs.TotalSalesAmount) OVER (ORDER BY cs.TotalSalesAmount DESC) AS CumulativeSalesAmount,
        ts.TotalSales,
        (SUM(cs.TotalSalesAmount) OVER (ORDER BY cs.TotalSalesAmount DESC) / ts.TotalSales) AS CumulativeSalesPercentage
    FROM 
        CountrySales cs, TotalSales ts
)
SELECT 
    CountryName,
    TotalSalesAmount,
    CumulativeSalesPercentage
FROM 
    CumulativeSales
WHERE 
    CumulativeSalesPercentage <= 0.50
ORDER BY 
    CumulativeSalesPercentage DESC;

-- Total sales and average monthly sales by employee and year
WITH EmployeeYearSales AS (
    SELECT 
        e.EmployeeKey,
        e.FirstName,
        e.LastName,
        t.Year,
        SUM(s.SalesAmount) AS TotalSalesAmount,
        COUNT(DISTINCT t.MonthNumber) AS NumberOfMonths
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Employee e ON s.EmployeeKey = e.EmployeeKey
    GROUP BY 
        e.EmployeeKey, e.FirstName, e.LastName, t.Year
)
SELECT 
    eys.EmployeeKey,
    eys.FirstName,
    eys.LastName,
    eys.Year,
    eys.TotalSalesAmount,
    eys.TotalSalesAmount / eys.NumberOfMonths AS AverageMonthlySalesAmount
FROM 
    EmployeeYearSales eys
ORDER BY 
    eys.Year, eys.EmployeeKey;


--Total sales amount and total discount amount per product and month.

WITH ProductMonthSales AS (
    SELECT 
        p.ProductName,
        t.Year,
        t.MonthNumber,
        SUM(s.SalesAmount) AS TotalSalesAmount,
        SUM(s.Discount) AS TotalDiscountAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Product p ON s.ProductKey = p.ProductKey
    GROUP BY 
        p.ProductName, t.Year, t.MonthNumber
)
SELECT 
    ProductName,
    Year,
    MonthNumber,
    TotalSalesAmount,
    TotalDiscountAmount
FROM 
    ProductMonthSales
ORDER BY 
    Year, MonthNumber, ProductName;

--Monthly year-t-date sales for each product category

WITH MonthlyCategorySales AS (
    SELECT 
        t.Year,
        t.MonthNumber,
        c.CategoryName,
        SUM(s.SalesAmount) AS MonthlySalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Product p ON s.ProductKey = p.ProductKey
        INNER JOIN Category c ON p.CategoryKey = c.CategoryKey
    GROUP BY 
        t.Year, t.MonthNumber, c.CategoryName
),
CumulativeCategorySales AS (
    SELECT 
        mcs.Year,
        mcs.MonthNumber,
        mcs.CategoryName,
        mcs.MonthlySalesAmount,
        SUM(mcs.MonthlySalesAmount) OVER (PARTITION BY mcs.Year, mcs.CategoryName ORDER BY mcs.MonthNumber) AS YearToDateSalesAmount
    FROM 
        MonthlyCategorySales mcs
)
SELECT 
    Year,
    MonthNumber,
    CategoryName,
    MonthlySalesAmount,
    YearToDateSalesAmount
FROM 
    CumulativeCategorySales
ORDER BY 
    Year, MonthNumber, CategoryName;

--Moving average over the last 3 months of the sales amount by product category

WITH MonthlyCategorySales AS (
    SELECT 
        t.Year,
        t.MonthNumber,
        c.CategoryName,
        SUM(s.SalesAmount) AS MonthlySalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
        INNER JOIN Product p ON s.ProductKey = p.ProductKey
        INNER JOIN Category c ON p.CategoryKey = c.CategoryKey
    GROUP BY 
        t.Year, t.MonthNumber, c.CategoryName
),
MovingAverageSales AS (
    SELECT 
        mcs.Year,
        mcs.MonthNumber,
        mcs.CategoryName,
        mcs.MonthlySalesAmount,
        AVG(mcs.MonthlySalesAmount) OVER (
            PARTITION BY mcs.CategoryName
            ORDER BY mcs.Year, mcs.MonthNumber
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS MovingAverage3Months
    FROM 
        MonthlyCategorySales mcs
)
SELECT 
    Year,
    MonthNumber,
    CategoryName,
    MonthlySalesAmount,
    MovingAverage3Months
FROM 
    MovingAverageSales
ORDER BY 
    Year, MonthNumber, CategoryName;


--Personal sales amount made by an employee compared with the total sales amount made by herself and her subordinated during 1997
SELECT
    e1.FirstName,
    e1.LastName,
    SUM(s1.SalesAmount) AS PersonalSales,
    (
        SELECT SUM(s2.SalesAmount)
        FROM Sales s2
        JOIN Employee e2 ON s2.EmployeeKey = e2.EmployeeKey
        JOIN Time t2 ON s2.OrderDateKey = t2.TimeKey
        WHERE (e2.EmployeeKey = e1.EmployeeKey OR e2.SupervisorKey = e1.EmployeeKey) AND YEAR(t2.Date) = 1997
    ) AS TotalSalesWithSubordinates
FROM Sales s1
JOIN Employee e1 ON s1.EmployeeKey = e1.EmployeeKey
JOIN Time t1 ON s1.OrderDateKey = t1.TimeKey
WHERE YEAR(t1.Date) = 1997
GROUP BY e1.FirstName, e1.LastName, e1.EmployeeKey;
GO

--Total sales amount, number of products, and sum of the quantities sold for each order

SELECT 
    s.OrderNo,
    SUM(s.SalesAmount) AS TotalSalesAmount,
    COUNT(DISTINCT s.ProductKey) AS NumberOfProducts,
    SUM(s.Quantity) AS TotalQuantitySold
FROM 
    Sales s
GROUP BY 
    s.OrderNo
ORDER BY 
    s.OrderNo;

--For each month, total number of orders, total sales amount, and average sales amount by order

WITH MonthlyOrderSales AS (
    SELECT 
        t.Year,
        t.MonthNumber,
        s.OrderNo,
        SUM(s.SalesAmount) AS OrderSalesAmount
    FROM 
        Sales s
        INNER JOIN Time t ON s.TimeKey = t.TimeKey
    GROUP BY 
        t.Year, t.MonthNumber, s.OrderNo
),
MonthlyAggregates AS (
    SELECT 
        Year,
        MonthNumber,
        COUNT(OrderNo) AS TotalNumberOfOrders,
        SUM(OrderSalesAmount) AS TotalSalesAmount,
        AVG(OrderSalesAmount) AS AverageSalesAmountPerOrder
    FROM 
        MonthlyOrderSales
    GROUP BY 
        Year, MonthNumber
)
SELECT 
    Year,
    MonthNumber,
    TotalNumberOfOrders,
    TotalSalesAmount,
    AverageSalesAmountPerOrder
FROM 
    MonthlyAggregates
ORDER BY 
    Year, MonthNumber;

-- For each employee, total sales amount, number of cities, and number of states to which she is assigned.

WITH EmployeeSales AS (
    SELECT 
        e.EmployeeKey,
        e.FirstName,
        e.LastName,
        SUM(s.SalesAmount) AS TotalSalesAmount
    FROM 
        Sales s
        INNER JOIN Employee e ON s.EmployeeKey = e.EmployeeKey
    GROUP BY 
        e.EmployeeKey, e.FirstName, e.LastName
),
EmployeeCitiesStates AS (
    SELECT 
        e.EmployeeKey,
        COUNT(DISTINCT t.CityKey) AS NumberOfCities,
        COUNT(DISTINCT s.StateKey) AS NumberOfStates
    FROM 
        Territories t
        INNER JOIN Employee e ON t.EmployeeKey = e.EmployeeKey
        INNER JOIN City ci ON t.CityKey = ci.CityKey
        LEFT JOIN State s ON ci.StateKey = s.StateKey
    GROUP BY 
        e.EmployeeKey
)
SELECT 
    es.EmployeeKey,
    es.FirstName,
    es.LastName,
    es.TotalSalesAmount,
    ecs.NumberOfCities,
    ecs.NumberOfStates
FROM 
    EmployeeSales es
    INNER JOIN EmployeeCitiesStates ecs ON es.EmployeeKey = ecs.EmployeeKey
ORDER BY 
    es.EmployeeKey;