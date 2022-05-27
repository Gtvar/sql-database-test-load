# Postgres Transaction isolation levels Session 1

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
SELECT current_setting('transaction_isolation');
```

##  Dirty read
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT age FROM users WHERE id = 1;
-- run Session 2
SELECT age FROM users WHERE id = 1; -- Here is wrong value
-- run Session 2
SELECT age FROM users WHERE id = 1;
COMMIT ;
```

##  Non-repeatable reads
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM users WHERE id = 1;
-- run Session 2
SELECT * FROM users WHERE id = 1;
COMMIT;
```

## Phantom reads
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM users
WHERE age BETWEEN 10 AND 30;
-- run Session 2
SELECT * FROM users
WHERE age BETWEEN 10 AND 30;
COMMIT;
```

##  Lost updates
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM users WHERE id = 1;
-- run Session 2
UPDATE users SET name='y' WHERE id=1;
COMMIT;
```

## Lost updates 2
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM users WHERE id = 1; -- age = 20
-- run Session 2
UPDATE users SET age=20+1 WHERE id=1;
COMMIT;
SELECT * FROM users WHERE id = 1; -- age = 21
```