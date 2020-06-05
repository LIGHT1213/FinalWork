DROP DATABASE IF EXISTS SELLManageSystem;
CREATE DATABASE SELLManageSystem;
USE SELLManageSystem;

CREATE TABLE Tb_Pros
(
NumberOfPros VARCHAR(20) PRIMARY KEY,
NameOfPros VARCHAR(30) NOT NULL,
PriceOfPros DECIMAL(10,2) NOT NULL,
SaveNum INT NOT NULL
);
INSERT INTO Tb_Pros VALUE ("0001","风筝",18.8,1024);
INSERT INTO Tb_Pros VALUE ("0112358","洗发露",18999.68,520);
CREATE TABLE Tb_Saler
(
NumberOfSaler VARCHAR(20) PRIMARY KEY,
NameOfSaler VARCHAR(30) ,
LocalOfSaler VARCHAR(10) NOT NULL,
PeopleForSaler VARCHAR(10) NOT NULL,
PhoneNumber VARCHAR(20) NOT NULL
);
INSERT INTO Tb_Saler VALUE ("000061","山东大德日用","华中","张三","18703993534");
INSERT INTO Tb_Saler VALUE ("000062","北京天成","华北","李四","18703111134");
INSERT INTO Tb_Saler VALUE ("000063","喜田有限公司","华中","张三","18703993534");
CREATE TABLE Tb_SalPros
(
SallDate DATE NOT NULL,
NumberOfPros VARCHAR(20) NOT NULL,
NumberOfSaler VARCHAR(20) NOT NULL,
NumberOfSall INT NOT NULL,
TotalMoney DECIMAL(10,2) NOT NULL,

CONSTRAINT Fk_Tb_SalPros_Tb_Pros FOREIGN KEY(NumberOfPros) REFERENCES Tb_Pros(NumberOfPros),
CONSTRAINT Fk_Tb_SalPros_Tb_Saler FOREIGN KEY(NumberOfSaler) REFERENCES Tb_Saler(NumberOfSaler)
);
INSERT INTO Tb_SalPros VALUE ("20201220","0001","000062",100,1880);
INSERT INTO Tb_SalPros VALUE ("19901220","0112358","000061",1,18999.68);

SELECT NameOfSaler,LocalOfSaler FROM Tb_Saler WHERE LocalOfSaler='华中' OR LocalOfSaler='华北' OR LocalOfSaler='东南';
SELECT NumberOfPros,SallDate FROM Tb_SalPros WHERE NumberOfSall>=100 AND (TotalMoney>=2000 AND TotalMoney<=6000);
SELECT NameOfSaler FROM Tb_Saler WHERE PhoneNumber IS NOT NULL;
SELECT Tb_Saler.NameOfSaler,Tb_SalPros.NumberOfPros ,NumberOfSall FROM Tb_Saler INNER JOIN Tb_SalPros ON Tb_SalPros.NumberOfSaler=Tb_Saler.NumberOfSaler;
SELECT NameOfSaler,PeopleForSaler,LocalOfSaler FROM Tb_Saler WHERE LocalOfSaler=(SELECT LocalOfSaler FROM Tb_Saler WHERE NameOfSaler='喜田有限公司') AND NameOfSaler!='喜田有限公司';
SELECT NameOfPros,Tb_SalPros.NumberOfPros,PriceOfPros,TotalMoney FROM Tb_SalPros INNER JOIN Tb_Pros ON Tb_SalPros.NumberOfPros=Tb_Pros.NumberOfPros HAVING TotalMoney<AVG(TotalMoney);
SELECT LocalOfSaler,TotalMoney FROM Tb_SalPros INNER JOIN Tb_Saler ON Tb_SalPros.NumberOfSaler=Tb_Saler.NumberOfSaler GROUP BY (LocalOfSaler) ORDER BY SUM(TotalMoney)  DESC LIMIT 1 ;