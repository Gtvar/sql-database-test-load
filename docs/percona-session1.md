# SQL Transaction isolation levels Session 1

###Init
```
create table users
(
    id   serial
        primary key,
    name varchar(30) not null,
    age  integer     not null
);

INSERT INTO yk.users (id, name, age) VALUES (1, 'Jack', 20);
INSERT INTO yk.users (id, name, age) VALUES (2, 'Jill', 25);

```

```
SET autocommit=0;
SET GLOBAL innodb_status_output=ON;
SET GLOBAL innodb_status_output_locks=ON;

show engine innodb status;

SELECT @@transaction_ISOLATION;
```

## Dirty read
```
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

SELECT age FROM users WHERE id = 1;
-- run Session 2
SELECT age FROM users WHERE id = 1; -- Here is wrong value
-- run Session 2
SELECT age FROM users WHERE id = 1;
```

## Non-repeatable reads
```
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

START TRANSACTION;
SELECT * FROM users WHERE id = 1;
-- run Session 2
SELECT * FROM users WHERE id = 1;
COMMIT;
```

## Phantom reads
```
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;

START TRANSACTION;
SELECT * FROM users
WHERE age BETWEEN 10 AND 30;
-- run Session 2
SELECT * FROM users
WHERE age BETWEEN 10 AND 30;
COMMIT;
```

## Lost updates
```
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;

START TRANSACTION;
SELECT * FROM users WHERE id = 1;
-- run Session 2
UPDATE users SET name='y' WHERE id=1;
COMMIT;
```


