CREATE DATABASE sunlab_homework1;
USE sunlab_homework1;

CREATE TABLE accounts (
    stu_id VARCHAR(15) PRIMARY KEY,
    stts bool,
    position varchar(15)
);

CREATE TABLE time_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stu_id VARCHAR(15), 
    CONSTRAINT sunlab_usr
    FOREIGN KEY (stu_id) 
        REFERENCES accounts(stu_id), 
    enter TIMESTAMP,
    departure TIMESTAMP
);
SELECT * FROM accounts;
SELECT stu_id, enter, departure FROM time_records;
INSERT INTO accounts (stu_id, stts, position) VALUES (12345,True,'Student');
INSERT INTO accounts (stu_id, stts, position) VALUES (12346,False,'Faculty');
INSERT INTO accounts (stu_id, stts, position) VALUES (12347,True,'Janitor');
INSERT INTO accounts (stu_id, stts, position) VALUES (12348,True,'Student');
INSERT INTO accounts (stu_id, stts, position) VALUES (12349,False,'Student');
SET time_zone= '+00:00';
INSERT INTO time_records (stu_id, enter, departure) VALUES (12345,'2021-01-01 12:00:01','2021-01-01 17:00:01');
INSERT INTO time_records (stu_id, enter, departure) VALUES (12346,'2022-01-01 13:00:01','2021-01-01 16:00:01');
INSERT INTO time_records (stu_id, enter, departure) VALUES (12347,'2001-01-01 14:00:01','2021-01-01 18:00:01');
INSERT INTO time_records (stu_id, enter, departure) VALUES (12348,'2001-01-01 15:00:01','2021-01-01 20:00:01');
