-- Creating a new City table with CityID as the auto-increment primary key

CREATE TABLE City
(
    CityID INT IDENTITY(1,1) PRIMARY KEY,
    CityName VARCHAR(100) NOT NULL
);

-- Creating state table 

CREATE TABLE State
(

    StateName VARCHAR(100) PRIMARY KEY,
    EnglishStateName VARCHAR(100),
    StateType VARCHAR(50),
    StateCode VARCHAR(10),
    StateCapital VARCHAR(100),
    CityName VARCHAR(100),
    CityID INT,
    FOREIGN KEY (CityID) REFERENCES City(CityID)
);

-- Creating the Region table

CREATE TABLE Region
(
    RegionName VARCHAR(100) PRIMARY KEY,
    RegionCode VARCHAR(10),
    StateName VARCHAR(100),
    FOREIGN KEY (StateName) REFERENCES State(StateName)
);

-- Creating the country table
CREATE TABLE Country
(
    CountryName VARCHAR(100) PRIMARY KEY,
    CountryCapital VARCHAR(100),
    CountryCode VARCHAR(10),
    Population INT,
    RegionName VARCHAR(100),
    Subdivision VARCHAR(100),
    FOREIGN KEY (RegionName) REFERENCES Region(RegionName)
);

-- creating the continent table

CREATE TABLE Continent
(
    CountryName VARCHAR(100),
    ContinentName VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY (CountryName) REFERENCES Country(CountryName)
);


-- Creating the  Employee Table

CREATE TABLE Employee
(
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE,
    Title VARCHAR(50),
    HireDate DATE,
    Address VARCHAR(100),
    City VARCHAR(50),
    CityId INT,
    Region VARCHAR(50),
    PostalCode VARCHAR(20),
    SupervisorID INT,
    Country VARCHAR(50),
    FOREIGN KEY (SupervisorID) REFERENCES Employee(EmployeeID),
    FOREIGN key (CityID) REFERENCES City(CityID)
);


-- Create Supplier Table

CREATE TABLE Supplier
(
    SupplierID INT PRIMARY KEY,
    Address VARCHAR(100),
    CompanyName VARCHAR(100),
    PostalCode VARCHAR(20)
);

-- Create Customer Table

CREATE TABLE Customer
(
    CustomerID INT PRIMARY KEY,
    CompanyName VARCHAR(100),
    Address VARCHAR(100),
    PostalCode VARCHAR(20)
);

-- Create Category Table

CREATE TABLE Category
(
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50),
    Description TEXT
);

-- Create Product Table

CREATE TABLE Product
(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    QuantityPerUnit VARCHAR(50),
    UnitPrice DECIMAL(10, 2),
    Discontinued BIT,
    CategoryID INT,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

-- Creating Time Tables

CREATE TABLE Year
(
    YearId INT IDENTITY(1,1) PRIMARY KEY,
    Year INT
);

-- Creating the semester

CREATE TABLE Semester
(
    Semester INT PRIMARY KEY,
    YearId Int,
    FOREIGN KEY (YearId) REFERENCES Year(YearId)
);

-- creating the quarter table

CREATE TABLE Quarter
(
    Quarter INT PRIMARY KEY,
    Semester INT,
    FOREIGN KEY (Semester) REFERENCES Semester(Semester)
);

-- creating the month table

CREATE TABLE Month
(
    MonthNumber INT PRIMARY KEY,
    MonthName VARCHAR(20),
    Quarter INT,
    FOREIGN KEY (Quarter) REFERENCES Quarter(Quarter)
);

-- creating the time table

CREATE TABLE Time
(
    Date DATE PRIMARY KEY,
    DayNbWeek INT,
    DayNameWeek VARCHAR(20),
    DayNbMonth INT,
    DayNbYear INT,
    WeekNbYear INT,
    MonthNumber INT,
    Quarter INT,
    Semester INT,
    Year INT,
    FOREIGN KEY (MonthNumber) REFERENCES Month(MonthNumber),
    FOREIGN KEY (Quarter) REFERENCES Quarter(Quarter),
    FOREIGN KEY (Semester) REFERENCES Semester(Semester),
    FOREIGN KEY (Year) REFERENCES Year(YearId)
);

-- Create Shipper Table
CREATE TABLE Shipper
(
    ShipperID INT PRIMARY KEY,
    CompanyName VARCHAR(100)
);

-- Create Order Table
CREATE TABLE [Order]
(
    OrderNo INT,
    OrderLineNo INT,
    PRIMARY KEY (OrderNo, OrderLineNo)
);
-- Creating Sales Table at the end beacuse of all the keys
CREATE TABLE Sales
(
    OrderDate DATE,
    DueDate DATE,
    ShippedDate DATE,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    Discount DECIMAL(5, 2),
    SalesAmount DECIMAL(15, 2),
    Freight DECIMAL(10, 2),
    NetAmount DECIMAL(15, 2),
    EmployeeID INT,
    SupplierID INT,
    CustomerID INT,
    ProductID INT,
    Date DATE,
    ShipperID INT,
    OrderNo INT,
    OrderLineNo INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (Date) REFERENCES Time(Date),
    FOREIGN KEY (ShipperID) REFERENCES Shipper(ShipperID),
    FOREIGN KEY (OrderNo, OrderLineNo) REFERENCES [Order](OrderNo, OrderLineNo)
);
