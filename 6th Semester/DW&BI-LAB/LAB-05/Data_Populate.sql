-- Insert data into the Category table
INSERT INTO Category (CategoryKey, CategoryName, Description) VALUES
(1001, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
(1002, 'Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'),
(1003, 'Confections', 'Desserts, candies, and sweet breads'),
(1004, 'Dairy Products', 'Cheeses');

-- Insert data into the Product table
INSERT INTO Product (ProductKey, ProductName, QuantityPerUnit, UnitPrice, Discontinued, CategoryKey) VALUES
(2001, 'Chai', '10 boxes x 20 bags', 18.00, 0, 1001),
(2002, 'Aniseed Syrup', '12 - 550 ml bottles', 10.00, 0, 1002),
(2003, 'Chef Anton\s Cajun Seasoning', '48 - 6 oz jars', 22.00, 0, 1002),
(2004, 'Chef Anton\s Gumbo Mix', '36 boxes', 21.35, 1, 1002);

-- Insert data into the Time table
INSERT INTO Time (TimeKey, Date, DayNbWeek, DayNameWeek, DayNbMonth, DayNbYear, WeekNbYear, MonthNumber, MonthName, Quarter, Semester, Year) VALUES
(3001, '2024-01-01', 1, 'Monday', 1, 1, 1, 1, 'January', 1, 1, 2024),
(3002, '2024-01-02', 2, 'Tuesday', 2, 2, 1, 1, 'January', 1, 1, 2024),
(3003, '2024-01-03', 3, 'Wednesday', 3, 3, 1, 1, 'January', 1, 1, 2024);

-- Insert data into the Shipper table
INSERT INTO Shipper (ShipperKey, CompanyName) VALUES
(4001, 'Speedy Express'),
(4002, 'United Package'),
(4003, 'Federal Shipping');

-- Insert data into the Employee table
INSERT INTO Employee (EmployeeKey, FirstName, LastName, Title, BirthDate, HireDate, Address, City, Region, PostalCode, Country, SupervisorKey) VALUES
(5001, 'David', 'Cohen', 'Manager', '1985-01-01', '2010-06-15', '123 Main St', 'Tel Aviv', 'TA', '61000', 'Israel', NULL),
(5002, 'Yael', 'Levy', 'Sales Representative', '1990-02-20', '2015-09-30', '456 Side St', 'Jerusalem', 'JM', '91000', 'Israel', 5001),
(5003, 'Moshe', 'Rabin', 'Sales Representative', '1988-03-15', '2012-05-10', '789 Cross St', 'Haifa', 'HA', '32000', 'Israel', 5001);

-- Insert data into the Continent table
INSERT INTO Continent (ContinentKey, ContinentName) VALUES
(6001, 'Asia'),
(6002, 'Europe'),
(6003, 'North America');

-- Insert data into the Country table
INSERT INTO Country (CountryKey, CountryName, CountryCode, CountryCapital, Population, Subdivision, ContinentKey) VALUES
(7001, 'Israel', 'IL', 'Jerusalem', 9216900, 'Districts', 6001),
(7002, 'United States', 'US', 'Washington D.C.', 331002651, 'States', 6003);

-- Insert data into the State table
INSERT INTO State (StateKey, StateName, EnglishStateName, StateType, StateCode, StateCapital, RegionName, RegionCode, CountryKey) VALUES
(8001, 'Tel Aviv', 'Tel Aviv', 'District', 'TA', 'Tel Aviv', 'Central', 'C', 7001),
(8002, 'Jerusalem', 'Jerusalem', 'District', 'JM', 'Jerusalem', 'Central', 'C', 7001),
(8003, 'Haifa', 'Haifa', 'District', 'HA', 'Haifa', 'Northern', 'N', 7001);

-- Insert data into the City table
INSERT INTO City (CityKey, CityName, StateKey, CountryKey) VALUES
(9001, 'Tel Aviv', 8001, 7001),
(9002, 'Jerusalem', 8002, 7001),
(9003, 'Haifa', 8003, 7001);

-- Insert data into the Territories table
INSERT INTO Territories (EmployeeKey, CityKey) VALUES
(5001, 9001),
(5002, 9002),
(5003, 9003);

-- Insert data into the Supplier table
INSERT INTO Supplier (SupplierKey, CompanyName, Address, PostalCode, CityKey) VALUES
(10001, 'Exotic Liquids', '49 Gilbert St.', '61000', 9001),
(10002, 'New Orleans Cajun Delights', 'P.O. Box 78934', '32000', 9003);

-- Insert data into the Customer table
INSERT INTO Customer (CustomerKey, CustomerID, CompanyName, Address, PostalCode, CityKey) VALUES
(11001,  'ALFKI', 'Alfreds Futterkiste', 'Obere Str. 57', '12209', 9002),
(11002, 'ANATR', 'Ana Trujillo Emparedados y helados', 'Avda. de la Constitución 2222', '05021', 9003);

-- Insert data into the Sales table
INSERT INTO Sales (CustomerKey, EmployeeKey, OrderDateKey, DueDateKey, ShippedDateKey, ShipperKey, ProductKey, SupplierKey, TimeKey, OrderNo, OrderLineNo, Quantity, Discount, SalesAmount, Freight) VALUES
(11001, 5001, 3001, 3002, 3003, 4001, 2001, 10001, 3001, 10248, 1, 10, 0.00, 200.00, 32.38),
(11002, 5002, 3002, 3003, 3001, 4002, 2002, 10002, 3002, 10249, 1, 5, 0.10, 150.00, 11.61);