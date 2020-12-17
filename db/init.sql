CREATE DATABASE taxablesData;
use taxablesData;

CREATE TABLE IF NOT EXISTS taxables (
    'id' int AUTO_INCREMENT,
    'Index' int,
    `Item` VARCHAR(34) CHARACTER SET utf8,
    `Cost` VARCHAR(24) CHARACTER SET utf8,
    `Tax` NUMERIC(4, 2),
    `Total` NUMERIC(4, 2),
    `Column_6` NUMERIC(4, 2),
    PRIMARY KEY (`id`)
);
INSERT INTO taxables ('Index', Item, Cost, Tax, Total) VALUES
    (100-150, 'Fruit of the Loom Girl''s Socks','$7.97', 0.60,  8.57,),
    (100-175, 'Rawlings Little League Baseball', '$2.97', 0.22,  3.19,),
    (200-225, 'Secret Antiperspirant', '$1.29', 0.10,  1.39),
    (100-655, 'Deadpool DVD"', '14.96', '$1.12', 16.08),
    (200-855, 'Maxwell House Coffee 28 oz', '$7.28', 0.55,  7.83),
    (100-063, 'Banana Boat Sunscreen', '$6.68', 0.50,  7.18),
    (100-352, 'Wrench Set', '$10.00', 0.75, 10.75),
    (200-251, 'M and M', '$8.98', 0.67, 9.65),
    (100-144, 'Bertoli Alfredo Sauce', '$2.12', 0.16,  2.28),
    (200-150, 'Large Paperclips', '$6.19', 0.46,  6.65);
