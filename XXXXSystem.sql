DROP DATABASE IF EXISTS XXXXSystem;
CREATE DATABASE XXXXSystem;
USE XXXXSystem;

CREATE TABLE SysManager
(
	ManagerID VARCHAR(20) PRIMARY KEY,
	ManagerPWD VARCHAR(10) NOT NULL
);

INSERT INTO SysManager VALUES('admin','admin');
`librarymanagesystem`
CREATE TABLE SysUser
(
	SysUserID VARCHAR(20) PRIMARY KEY,
	SysUserPWD VARCHAR(10) NOT NULL
);
INSERT INTO SysUser VALUES('test','1234');
INSERT INTO SysUser VALUES('test1','1234');
CREATE TABLE MoneyRecord
(
	SysUserID VARCHAR(20),
	InOrOut INT, #in 1 out 0
	NumOfMoney DECIMAL(10,2) NOT NULL,
	InOrOutCauseDate DATE NOT NULL,
	CONSTRAINT Fk_MoneyRecord_SysUser FOREIGN KEY(SysUserID) REFERENCES SysUser(SysUserID)
);
INSERT INTO MoneyRecord VALUES('test',1,100,20200101);
INSERT INTO MoneyRecord VALUES('test',0,100,20200101);
INSERT INTO MoneyRecord VALUES('test1',0,100,20200101);