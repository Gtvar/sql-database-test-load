# Postgres Transaction isolation levels Session 2

```
SELECT current_setting('transaction_isolation');
```
##  Dirty read
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
UPDATE users SET age = 21 WHERE id = 1;
-- run Session 1
ROLLBACK;
-- run Session 1
```

##  Non-repeatable reads
```
-- run Session 1
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
UPDATE users SET age = 21 WHERE id = 1;
COMMIT;
-- run Session 1
```

##  Phantom reads
```
-- run Session 1
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
INSERT INTO users(id, name, age) VALUES (3, 'Bob', 27);  -- Error after some time(~60s)
COMMIT;
-- run Session 1
```

##  Lost updates
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- run Session 1
SELECT * FROM users WHERE id = 1;
UPDATE users SET name='x' WHERE id=1; -- Error after some time(~60s)
COMMIT;
-- run Session 1
```

## Lost updates 2
```
START TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- run Session 1
SELECT * FROM users WHERE id = 1; -- age = 20
UPDATE users SET age=20+1 WHERE id=1; --
COMMIT;
-- run Session 1
SELECT * FROM users WHERE id = 1; -- age = 21
```