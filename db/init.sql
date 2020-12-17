CREATE DATABASE taxablesData;
use taxablesData;

CREATE TABLE IF NOT EXISTS taxables (
    `Index` INT,
    `Item` VARCHAR(34) CHARACTER SET utf8,
    `Cost` VARCHAR(24) CHARACTER SET utf8,
    `Tax` NUMERIC(4, 2),
    `Total` NUMERIC(4, 2),
    `Column_6` NUMERIC(4, 2)
);
INSERT INTO taxables VALUES
    ( 1,' "Fruit of the Loom Girl''s Socks"','  7.97', 0.60,  8.57,NULL),
    ( 2,' "Rawlings Little League Baseball"',' 2.97', 0.22,  3.19,NULL),
    ( 3,' "Secret Antiperspirant"','           1.29', 0.10,  1.39,NULL),
    ( 4,' "Deadpool DVD"','                   14.96', 1.12, 16.08,NULL),
    ( 5,' "Maxwell House Coffee 28 oz"','      7.28', 0.55,  7.83,NULL),
    ( 6,' "Banana Boat Sunscreen',' 8 oz"',     6.68, 0.50,  7.18),
    ( 7,' "Wrench Set',' 18 pieces"',          10.00, 0.75, 10.75),
    ( 8,' "M and M',' 42 oz"',                  8.98, 0.67,  9.65),
    ( 9,' "Bertoli Alfredo Sauce"','           2.12', 0.16,  2.28,NULL),
    (10,' "Large Paperclips',' 10 boxes"',      6.19, 0.46,  6.65);
