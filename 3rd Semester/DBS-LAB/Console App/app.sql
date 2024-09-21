use app;


create table books(
Id int Primary Key Auto_Increment,
Title Varchar(50) not null ,
Author Varchar(50) not null,
Genre Varchar(50),
Publisher varchar(50) not null,
Publish_date date not Null,
Price decimal not null,
description TEXT);

INSERT INTO books (title, author, genre, publisher, publish_date, price, description)
VALUES

('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age Fiction', 'Little, Brown and Company', '1951-07-16', 12, 'The story of Holden Caulfield, a young man who struggles with the complexities of adulthood.'),
('Pride and Prejudice', 'Jane Austen', 'Romantic Fiction', 'T. Egerton, Whitehall', '1813-01-28', 8, 'The story of the Bennet family and their quest to find suitable husbands for their five daughters in Regency-era England.'),
('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy Fiction', 'Allen & Unwin', '1954-07-29', 25, 'A story of the struggle for control of the mythical land of Middle-earth, and the quest to destroy the One Ring.'),
('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 'Pan Books', '1979-10-12', 9, 'The misadventures of the last surviving human and his alien friend as they travel through space and time.'),
('The Da Vinci Code', 'Dan Brown', 'Thriller Fiction', 'Doubleday', '2003-03-18', 15, 'The story of a symbologist and a cryptologist who try to unravel the mystery behind the murder of the curator of the Louvre.'),
('Gone with the Wind', 'Margaret Mitchell', 'Historical Fiction', 'Macmillan Publishers', '1936-06-30', 20, 'A sweeping story of the American Civil War and its aftermath, centered around the life of Scarlett O''Hara.'),
('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mystery Fiction', 'Norstedts Förlag', '2005-08-01', 14, 'The story of a journalist and a hacker who investigate the disappearance of a wealthy businessman''s niece.');