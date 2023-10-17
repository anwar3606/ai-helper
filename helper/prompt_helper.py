powershell_prompt = """Correctly answer the asked question. Return 'Sorry, Can't answer that.' if the question isn't related to technology.

Q - get into a docker container.
A - ```docker exec -it <container>```

Q - Check what's listening on a port.
A - ```netstat -ano | findstr :<port>```

Q - How to ssh into a server with a specific file.
A - ```ssh -i <file_path> <user>@<port>```

Q - How to set relative line numbers in vim.
A - ```:set relativenumber```

Q - How to create alias?
A - ```Set-Alias <new_command> <old_command>```

Q - Tail docker logs.
A - ```docker logs -f mongodb```

Q - Forward port in kubectl.
A - ```kubectl port-forward <pod_name> 8080:3000```

Q - Check if a port is accessible.
A - ```Test-NetConnection -ComputerName <host_name> -Port <port>```

Q - Kill a process running on port 3000.
A - ```Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process```

Q - Backup database from a mongodb container.
A - ```docker exec -it mongodb bash -c "mongoexport --db mongodb --collection collections --outdir backup"```

Q - SSH Tunnel Remote Host port into a local port.
A - ```ssh -L <local_port>:<remote_host>:<remote_port> <user>@<remote_host>```

Q - Copy local file to S3.
A - ```aws s3 cp <local_file> s3://<bucket_name>/<remote_file>```

Q - Copy S3 file to local.
A - ```aws s3 cp s3://<bucket_name>/<remote_file> <local_file>```

Q - Recursively remove a folder.
A - ```Remove-Item -Recurse <folder_name>```

Q - Copy a file from local to ssh server.
A - ``` scp /path/to/file user@server:/path/to/destination```

Q - Download a file from a URL.
A - ```Invoke-WebRequest -Uri <url> -OutFile <file_name>```

Q - Git commit with message.
A - ```git commit -m "my commit message"```

Q - Give a user sudo permissions.
A - ```Add-LocalGroupMember -Group "Administrators" -Member <user>```

Q - Check what's running on a port?
A - ```Get-Process -Id (Get-NetTCPConnection -LocalPort <port>).OwningProcess```

Q - View last 5 files from history
A - ```Get-History -Count 5```

Q - When was China founded?
A - Sorry, Can't answer that.

Q - Filter docker container with labels
A - ```docker ps --filter "label=<KEY>"```

Q - When was Abraham Lincon born?
A - Sorry, Can't answer that.

Q - Get into a running kubernetes pod
A - ```kubectl exec -it <pod_name> bash```

Q - Capital city of Ukrain?
A - Sorry, Can't answer that.

Q - """

grammer_system_prompt = """Check the following text for spelling and grammar errors.
Highlight the error and also provide the correct sentence in a new line.
Provide all responses in markdown format.
Also provide a more concise and improved version of the sentence.
Each section,Errors,Corrected,Improved should be separated by markdown horizontal line."""

assessment = """You are required to provide a time estimate based on the assessment. Follow the below format.

Assessment: Adding a simple one page notice.
Modify ABCDDL001.dfa
Hours: 4
Reasons: 
1. Formatting and setup: 4 hours.

---

Assessment: Setup with a flat file index.
Hours: 8
Reasons: 
1. Configuring and integrating the flat file index: 8 hours.

---

Assessment: Simple flat file Direct Mail setup.
Hours: 5
Reasons: 
1. Formatting and setup: 5 hours.

---

Assessment: Non-selective setup.
Hours: 8
Reasons: 
1. Configuring and setting up the non-selective criteria: 8 hours.

---

Assessment: Setup for elective insert by account list or selective by program.
Hours: 6
Reasons: 
1. Configuring and setting up the elective insert: 6 hours.

---

Assessment: Requirement for a prefilled dividend rate sheet.
Hours: 5
Reasons: 
1. Development of prefilled dividend rate sheet: 5 hours.

---

Assessment: If the rate sheet template is fixed and the values need to update frequently.
Hours: 5
Reasons: 
1. Development of a solution to pull rates values from rate values file: 5 hours.

---"""

unix_prompt_gpt35 = """Provide cli command. Your answer should follow the following format provided in the below two examples. 
Command start with '```' and close with '```'. Must provide explanation of the command in markdown format after a '---' line.

User: get into a docker container.
You: 
```docker exec -it mongodb```
---
Explanation:
- exec -it: Execute a command in a running container.  
  
User: Check what's listening on a port.
You: 
```lsof -i tcp:4000```
---
Explanation:
- lsof -i: List open files associated with Internet connections.  
- tcp:4000: List only TCP connections on port 4000."""

unix_prompt_gpt35_short = """Provide only cli command. Your answer should follow the following format provided in the below two examples.
Command start with '```' and close with '```'.

User: get into a docker container.
You:
```docker exec -it mongodb```

User: Check what's listening on a port.
You:
```lsof -i tcp:4000```

User: How to ssh into a server with a specific file.
You:
```ssh -i <file_path> <user>@<port>```
"""

windows_prompt_gpt35 = """Provide powershell cli command. Your answer should follow the following format provided in the below two examples.
Command start with '```' and close with '```'. Must provide explanation of the command in markdown format after a '---' line.

User: How to ssh into a server with a specific file.
You:
```ssh -i <file_path> <user>@<port>```
---
Explanation:
- ssh: Secure Shell.
- -i: Selects a file from which the identity (private key) for public key authentication is read.
- <file_path>: Path to the private key file.
- <user>: Username of the server.
- <port>: Port of the server.

User: Check what's listening on a port.
You:
```netstat -ano | findstr :<port>```
---
Explanation:
- netstat: Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
- -ano: Show all connections and listening ports in numerical form.
- findstr: Search for strings in files.
- :<port>: Port to search for."""

windows_prompt_gpt35_short = """Provide only powershell cli command. Your answer should follow the following format provided in the below two examples.
Command start with '```' and close with '```'.

User: How to ssh into a server with a specific file.
You:
```ssh -i <file_path> <user>@<port>```

User: Check what's listening on a port.
You:
```netstat -ano | findstr :<port>```
"""
