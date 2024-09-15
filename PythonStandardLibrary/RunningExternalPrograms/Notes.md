# Running External Programs/Commands

In Python, you can run external programs and commands using the `subprocess` module. This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. Here's how you can use it:

### 1. Running a Command

To run a simple external command, use `subprocess.run()`.

python runs each of the provided commands and for each one waits till it ends and then goes for the next one.

```python
import subprocess

# Run a simple command like `ls` or `dir` depending on the OS
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Output the result
print(result.stdout)
```

for Windows

```python
import subprocess

# Run a simple command like `ls` or `dir` depending on the OS
result = subprocess.run(["dir"], capture_output=True, text=True, shell=True)

# Output the result
print(result.stdout)
```

### Key Parameters:

- `capture_output=True`: Captures the output of the command (both stdout and stderr)/(standard-output, standard-error).
- `text=True`: Returns output as a string instead of bytes.

### 2. Capturing Output

To capture the output and store it in a variable for further processing:

```python
import subprocess

# Running a command and capturing the output
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)

# Print the captured output
print(result.stdout)  # Should print: Hello, World!
```

### 3. Running a Command Without Waiting

If you don't want Python to wait for the command to complete (i.e., you want to run it asynchronously), use `subprocess.Popen()`:

```python
import subprocess

# Running a command in the background
process = subprocess.Popen(['sleep', '5'])

# Do other tasks while the process is running
print("Command is running in the background")
```

### 4. Handling Errors

If you want to check for errors (e.g., if the command fails), you can use `check=True`:

```python
import subprocess

try:
    # This will raise an exception if the command returns a non-zero exit code
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
```

### 5. Passing Input to a Program

You can pass input to the external command using the `input` parameter:

```python
import subprocess

# Passing input to a command
result = subprocess.run(['grep', 'hello'], input='hello world\nhello python\nhi there', text=True, capture_output=True)

# Output the result
print(result.stdout)  # Should print: hello world\nhello python
```

These methods allow you to run and interact with external programs or system commands from within your Python code effectively.
