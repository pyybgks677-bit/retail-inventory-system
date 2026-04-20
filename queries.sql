-- Register User
INSERT INTO Users (Username, PasswordHash)
VALUES ('bruno', 'hashedpassword');

-- Add Product
INSERT INTO Products (Name, Stock)
VALUES ('Laptop', 10);

-- Record Purchase
INSERT INTO Transactions (UserID, ProductID, Quantity, Type)
VALUES (1, 1, 5, 'purchase');

-- Update Stock
UPDATE Products
SET Stock = Stock + 5
WHERE ProductID = 1;

-- View Products
SELECT * FROM Products;
