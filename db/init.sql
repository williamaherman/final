CREATE DATABASE taxablesData;
use taxablesData;

CREATE TABLE IF NOT EXISTS taxables (id int AUTO_INCREMENT,
    Item VARCHAR(48),
    Cost VARCHAR(48),
    Tax NUMERIC(4, 2),
    Total NUMERIC(4, 2),
    PRIMARY KEY (id)
);
INSERT INTO taxables(Item, Cost, Tax, Total) VALUES
    ('Fruit of the Loom Girl''s Socks','7.97', 0.60,  8.57),
    ('Rawlings Little League Baseball', '2.97', 0.22,  3.19),
    ('Secret Antiperspirant', '1.29', 0.10,  1.39),
    ('Deadpool DVD"', '14.96', 1.12, 16.08),
    ('Maxwell House Coffee 28 oz', '7.28', 0.55,  7.83),
    ('Banana Boat Sunscreen', '$6.68', 0.50,  7.18),
    ('Wrench Set', '$10.00', 0.75, 10.75),
    ('M and M', '$8.98', 0.67, 9.65),
    ('Bertoli Alfredo Sauce', '$2.12', 0.16,  2.28),
    ('Large Paperclips', '$6.19', 0.46,  6.65);
