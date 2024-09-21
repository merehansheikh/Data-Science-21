


-- Create the Category table
CREATE TABLE Category (
    CategoryKey INT PRIMARY KEY,
    CategoryName NVARCHAR(255),
    Description NVARCHAR(MAX)
);
GO
-- Create the Product table
CREATE TABLE Product (
    ProductKey INT PRIMARY KEY,
    ProductName NVARCHAR(255),
    QuantityPerUnit NVARCHAR(50),
    UnitPrice DECIMAL(18, 2),
    Discontinued BIT,
    CategoryKey INT,
    FOREIGN KEY (CategoryKey) REFERENCES Category(CategoryKey)
);
GO




-- Create the Time table
CREATE TABLE Time (
    TimeKey INT PRIMARY KEY,
    Date DATE,
    DayNbWeek INT,
    DayNameWeek NVARCHAR(20),
    DayNbMonth INT,
    DayNbYear INT,
    WeekNbYear INT,
    MonthNumber INT,
    MonthName NVARCHAR(20),
    Quarter INT,
    Semester INT,
    Year INT
);
GO

-- Create the Shipper table
CREATE TABLE Shipper (
    ShipperKey INT PRIMARY KEY,
    CompanyName NVARCHAR(255)
);
GO

-- Create the Employee table
CREATE TABLE Employee (
    EmployeeKey INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Title NVARCHAR(50),
    BirthDate DATE,
    HireDate DATE,
    Address NVARCHAR(MAX),
    City NVARCHAR(100),
    Region NVARCHAR(50),
    PostalCode NVARCHAR(20),
    Country NVARCHAR(100),
    SupervisorKey INT,
    FOREIGN KEY (SupervisorKey) REFERENCES Employee(EmployeeKey)
);
GO



-- Create the Continent table
CREATE TABLE Continent (
    ContinentKey INT PRIMARY KEY,
    ContinentName NVARCHAR(100)
);
GO
-- Create the Country table
CREATE TABLE Country (
    CountryKey INT PRIMARY KEY,
    CountryName NVARCHAR(100),
    CountryCode NVARCHAR(10),
    CountryCapital NVARCHAR(100),
    Population BIGINT,
    Subdivision NVARCHAR(100),
    ContinentKey INT,
    FOREIGN KEY (ContinentKey) REFERENCES Continent(ContinentKey)
);
GO
-- Create the State table
CREATE TABLE State (
    StateKey INT PRIMARY KEY,
    StateName NVARCHAR(100),
    EnglishStateName NVARCHAR(100),
    StateType NVARCHAR(50),
    StateCode NVARCHAR(10),
    StateCapital NVARCHAR(100),
    RegionName NVARCHAR(100) NULL,
    RegionCode NVARCHAR(10) NULL,
    CountryKey INT,
    FOREIGN KEY (CountryKey) REFERENCES Country(CountryKey)
);
GO





-- Create the City table
CREATE TABLE City (
    CityKey INT PRIMARY KEY,
    CityName NVARCHAR(100),
    StateKey INT NULL,
    CountryKey INT NULL,
    FOREIGN KEY (StateKey) REFERENCES State(StateKey),
    FOREIGN KEY (CountryKey) REFERENCES Country(CountryKey)
);
GO

-- Create the Territories table
CREATE TABLE Territories (
    EmployeeKey INT,
    CityKey INT,
    PRIMARY KEY (EmployeeKey, CityKey),
    FOREIGN KEY (EmployeeKey) REFERENCES Employee(EmployeeKey),
    FOREIGN KEY (CityKey) REFERENCES City(CityKey)
);
GO
-- Create the Supplier table
CREATE TABLE Supplier (
    SupplierKey INT PRIMARY KEY,
    CompanyName NVARCHAR(255),
    Address NVARCHAR(MAX),
    PostalCode NVARCHAR(20),
    CityKey INT,
    FOREIGN KEY (CityKey) REFERENCES City(CityKey)
);
GO
-- Create the Customer table
CREATE TABLE Customer (
    CustomerKey INT PRIMARY KEY,
    CustomerID NVARCHAR(50) UNIQUE,
    CompanyName NVARCHAR(255),
    Address NVARCHAR(MAX),
    PostalCode NVARCHAR(20),
    CityKey INT,
    FOREIGN KEY (CityKey) REFERENCES City(CityKey)
);
GO


-- Create the Sales table
CREATE TABLE Sales (
    CustomerKey INT,
    EmployeeKey INT,
    OrderDateKey INT,
    DueDateKey INT,
    ShippedDateKey INT,
    ShipperKey INT,
    ProductKey INT,
    SupplierKey INT,
    TimeKey INT,
    OrderNo INT,
    OrderLineNo INT,
    Quantity INT,
    Discount DECIMAL(5, 2),
    SalesAmount DECIMAL(18, 2),
    Freight DECIMAL(18, 2),
    PRIMARY KEY (CustomerKey, EmployeeKey, OrderDateKey, DueDateKey, ShippedDateKey, ShipperKey, ProductKey,SupplierKey),
    FOREIGN KEY (CustomerKey) REFERENCES Customer(CustomerKey),
    FOREIGN KEY (EmployeeKey) REFERENCES Employee(EmployeeKey),
    FOREIGN KEY (OrderDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (DueDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (ShippedDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (ShipperKey) REFERENCES Shipper(ShipperKey),
    FOREIGN KEY (ProductKey) REFERENCES Product(ProductKey),
    FOREIGN KEY (SupplierKey) REFERENCES Supplier(SupplierKey)
);