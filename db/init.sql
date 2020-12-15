CREATE DATABASE InventoryData;
use InventoryData;

CREATE TABLE IF NOT EXISTS Inventory (
    `id` int AUTO_INCREMENT,
    `product_name` VARCHAR(32) CHARACTER SET utf8,
    `product_description` VARCHAR(128) CHARACTER SET utf8,
    `made_in` VARCHAR(32) CHARACTER SET utf8,
    `price` VARCHAR(8) CHARACTER SET utf8,
    `color` VARCHAR(32) CHARACTER SET utf8,
    `condition` VARCHAR(32) CHARACTER SET utf8,
    PRIMARY KEY (`id`)
);
INSERT INTO Inventory(product_name, product_description, made_in, price, color, 'condition') VALUES
    ('Nightstand', 'night stand built by prominent artist', 'New England', '125', 'white' 'fair'),
    ('Coffee table', 'coffee table perfect for living room', 'China', '25', 'brown', 'good'),
    ('Bed', 'queen sized bed', 'Brazil', '300', 'brown', 'excellent'),
    ('lever', 'think about all the levers you''ved pulled', 'Unknown', '10', 'black', 'great'),
    ('kitchen table', 'can sit 4-6 people', 'New Jersey', '100', 'yellow', 'fair'),
    ('recliner', 'adjustable head rest and massage chair', 'Japan', '399', 'green', 'bad')