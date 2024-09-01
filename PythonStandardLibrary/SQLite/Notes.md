### What is SQLite?

SQLite is a lightweight, self-contained, and serverless relational database management system (RDBMS). Unlike other RDBMS like MySQL or PostgreSQL, SQLite doesn’t require a separate server process; it stores the entire database (including tables, schemas, and data) in a single file on disk. This makes it ideal for applications that need a simple, low-overhead database, like mobile apps, small desktop applications, or for development and testing purposes.

### Working with SQLite in Python

Python has a built-in module called `sqlite3` that allows you to work with SQLite databases without needing any external libraries. Here’s how you can work with SQLite in Python:

#### 1. **Import the `sqlite3` Module**

```python
import sqlite3
```

#### 2. **Connecting to a Database**

You can connect to an existing SQLite database or create a new one if it doesn’t exist by using the `connect()` function:

```python
conn = sqlite3.connect('example.db')
```

This will create a file named `example.db` in the current directory if it doesn’t already exist.

#### 3. **Creating a Cursor Object**

A cursor object is used to interact with the database. It allows you to execute SQL commands.

```python
cursor = conn.cursor()
```

#### 4. **Executing SQL Commands**

You can use the `execute()` method to run SQL commands. For example, to create a table:

```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')
```

#### 5. **Inserting Data**

To insert data into the table:

```python
cursor.execute('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', ('Alice', 30))
```

You can also insert multiple rows at once using `executemany()`:

```python
users = [('Bob', 25), ('Charlie', 35)]
cursor.executemany('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', users)
```

#### 6. **Querying Data**

To retrieve data, you can use the `execute()` method followed by `fetchall()` or `fetchone()`:

```python
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)
```

#### 7. **Committing Changes**

If you make changes to the database (e.g., inserting, updating, or deleting data), you need to commit those changes:

```python
conn.commit()
```

#### 8. **Closing the Connection**

Once you’re done with the database, you should close the connection to free up resources:

```python
conn.close()
```

### Example: Putting It All Together

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', ('Alice', 30))
cursor.executemany('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', [('Bob', 25), ('Charlie', 35)])

# Commit changes
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
```

This is a basic overview, but SQLite supports more advanced features like transactions, foreign keys, and indexing, which you can explore as needed.

The common extension for a SQLite database file is `.sqlite`. However, you may also encounter other extensions like:

- **`.db`**
- **`.sqlite3`**
- **`.db3`**

These extensions are interchangeable and don't affect the functioning of the database. The choice of extension is often based on personal or project-specific conventions.
