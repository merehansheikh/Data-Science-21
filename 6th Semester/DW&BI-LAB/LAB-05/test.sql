CREATE table Employee (
    EmployeeID int PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Title VARCHAR(255),
    BirthDate DATE,
    HireDate DATE,
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode INT,
    Country VARCHAR(255)
);


CREATE TABLE [dbo].[Supplier] (
    [SupplierID]  INT           NOT NULL,
    [CompanyName] VARCHAR (255) NULL,
    [Address]     VARCHAR (255) NULL,
    [PostalCode]  INT           NULL,
    CONSTRAINT [PK_Supplier] PRIMARY KEY CLUSTERED ([SupplierID] ASC)
);


CREATE TABLE [dbo].[City] (
    [CityName] VARCHAR (255) NOT NULL
);


CREATE TABLE [dbo].[Customer] (
    [CustomerID]  INT           NOT NULL,
    [CompanyName] VARCHAR (255) NULL,
    [Address]     VARCHAR (255) NULL,
    [PostalCode]  INT           NULL,
    CONSTRAINT [PK_Customer] PRIMARY KEY CLUSTERED ([CustomerID] ASC)
);

CREATE TABLE [dbo].[State] (
    [StateName]        VARCHAR (255) NOT NULL,
    [EnglishStateName] VARCHAR (255) NULL,
    [StateType]        VARCHAR (255) NULL,
    [StateCode]        VARCHAR (255) NULL,
    [StateCapital]     VARCHAR (255) NULL,
    CONSTRAINT [PK_State] PRIMARY KEY CLUSTERED ([StateName] ASC)
);
CREATE TABLE [dbo].[Region] (
    [RegionName] VARCHAR (255) NOT NULL,
    [RegionCode] INT           NULL,
    CONSTRAINT [PK_Region] PRIMARY KEY CLUSTERED ([RegionName] ASC)
);

CREATE TABLE [dbo].[Country] (
    [CountryName]    VARCHAR (255) NOT NULL,
    [CountryCode]    INT           NULL,
    [CountryCapital] VARCHAR (255) NULL,
    [Population]     INT           NULL,
    [Subdivision]    VARCHAR (255) NULL,
    CONSTRAINT [PK_Country] PRIMARY KEY CLUSTERED ([CountryName] ASC)
);

CREATE TABLE [dbo].[Continent] (
    [ContinentName] VARCHAR (255) NOT NULL,
    CONSTRAINT [PK_Continent] PRIMARY KEY CLUSTERED ([ContinentName] ASC)
);

CREATE TABLE [dbo].[Product] (
    [ProductID]       INT           NOT NULL,
    [ProductName]     VARCHAR (255) NOT NULL,
    [QuantityPerUnit] INT           NOT NULL,
    [UnitPrice]       INT           NOT NULL,
    [Discontinued]    VARCHAR (255) NOT NULL,
    CONSTRAINT [PK_Product] PRIMARY KEY CLUSTERED ([ProductID] ASC)
);

CREATE TABLE [dbo].[Category] (
    [CategoryID]   INT           NOT NULL,
    [CategoryName] VARCHAR (255) NOT NULL,
    [Description]  VARCHAR (255) NOT NULL,
    CONSTRAINT [PK_Category] PRIMARY KEY CLUSTERED ([CategoryID] ASC)
);

CREATE TABLE [dbo].[Shipper] (
    [ShipperID]   INT           NOT NULL,
    [CompanyName] VARCHAR (255) NOT NULL,
    CONSTRAINT [PK_Shipper] PRIMARY KEY CLUSTERED ([ShipperID] ASC)
);

CREATE TABLE [dbo].[Year] (
    [Year] INT NOT NULL,
    CONSTRAINT [PK_Year] PRIMARY KEY CLUSTERED ([Year] ASC)
);


CREATE TABLE [dbo].[Semester] (
    [Semester] INT NOT NULL,
    CONSTRAINT [PK_Semester] PRIMARY KEY CLUSTERED ([Semester] ASC)
);


CREATE TABLE [dbo].[Quarter] (
    [Quarter] INT NOT NULL,
    CONSTRAINT [PK_Quarter] PRIMARY KEY CLUSTERED ([Quarter] ASC)
);

