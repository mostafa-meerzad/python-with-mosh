import subprocess

# # Run a simple command like `ls` or `dir` depending on the OS
# result = subprocess.run(["dir"], capture_output=True, text=True, shell=True)

# # Output the result
# print(result.stdout)

result = subprocess.run(
    ["echo", "Hello world"], capture_output=True, text=True, shell=True
)

print("here is the captured output of the commands we just run")
print()
print(
    result
)  # => CompletedProcess(args=['echo', 'Hello world'], returncode=0, stdout='"Hello world"\n', stderr='')
print(type(result))  # => <class 'subprocess.CompletedProcess'>
pritn()
# this result is an object of type "CompleteProcess" and these are the properties (args, returncode, stdout, stderr)

print("args :", result.args)
print("returnCode :", result.returncode)
print("stdout :", result.stdout)
print("stderr :", result.stderr)
