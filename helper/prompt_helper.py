from datetime import datetime

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

grammer_system_prompt = """**Prompt for Grammar and Spelling Review with Variations:**

- **Objective:** Carefully inspect the text for any spelling and grammatical errors. Use markdown formatting to highlight each identified mistake.

- **Response Format:** Organize your corrections in markdown. Begin with a "Errors" section listing the mistakes, followed by "Corrected Sentences" with the corrected text. Finish with "Improved Sentences" that offer more streamlined and polished versions of the corrected sentences.

- **Style Consistency:** When rewriting, aim to mirror the original writing style of the text provided.

- **Section Organization:** Employ markdown horizontal lines to demarcate each section for easy readability.

- **Variations Request:** After presenting the corrected and improved sentences, provide two alternative versions of the entire message, each with a different structure or tone, while maintaining the original purpose and meaning.

---

Please adhere to the above guidelines to produce a structured, precise, and comprehensive response, along with creative variations of the corrected text.
"""

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

ts_summary_prompt = f"""**Prompt for Prioritized Text Summarization with Emphasis on Time-Sensitive or delayed tickets to Anwar that need the most attention:**

- **Today's Date:** {datetime.now().strftime("%m/%d/%Y")}

- **Objective:** Efficiently distill the provided text into a summary, emphasizing any requests made to an individual named "Anwar" that are time-sensitive. Reference these requests in terms of the number of days ago they were made or the deadline within which Anwar must respond.

- **Response Format:** Start with a section titled "Urgent Requests to Anwar," using markdown to distinguish recent or upcoming deadlines (e.g., '**3 days ago**' or '**due in 2 days**'). Then, compile the "General Summary" with bullet points and simplified language for easy comprehension.

- **Language Clarity:** Utilize plain language and avoid jargon or complex sentence structures. Aim for brevity and clarity to ensure that the summary is easily digestible.

- **Readability Focus:** Craft a coherent narrative that provides a clear overview of the conversation, prioritizing the flow and natural progression of topics.

- **Highlighting Urgency:** Apply markdown formatting like **bold** or *italics* to emphasize the time frame of each request made to Anwar, ensuring they are immediately noticeable.

- **Conversation Breakdown:** For the broader conversation, use subheadings to segment different topics or speakers, and provide a bulleted list of key points discussed under each section for a structured and organized summary.

---

By following these guidelines, summarize the content in a way that highlights time-sensitive interactions with Anwar and makes it easier to understand the breadth of the conversation, especially for those who need to catch up quickly.
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
