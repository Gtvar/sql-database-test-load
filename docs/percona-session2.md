# SQL Transaction isolation levels Session 2

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

START TRANSACTION;
UPDATE users SET age = 21 WHERE id = 1;
-- run Session 1
ROLLBACK;
-- run Session 1
```

## Non-repeatable reads
```
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED ;

-- run Session 1
UPDATE users SET age = 21 WHERE id = 1;
COMMIT;
-- run Session 1
```

## Phantom reads
```
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;
-- run Session 1
INSERT INTO users(id, name, age) VALUES (3, 'Bob', 27); # Error after some time(~60s)
COMMIT;
-- run Session 1
```

## Lost updates
```
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;

START TRANSACTION;
-- run Session 1
SELECT * FROM users WHERE id = 1;
UPDATE users SET name='x' WHERE id=1; # Error after some time(~60s)
COMMIT;
-- run Session 1
```


