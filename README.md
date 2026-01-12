## Dead Drop C2
DISCLAIMER

This project is provided for educational and research purposes only.
The author is not responsible for any misuse, damage, or illegal activity
caused by this software. Any use of this code for malicious purposes is
solely the responsibility of the user or third party using it.

By using this software, you agree to use it responsibly and in compliance
with all applicable laws and regulations.

## Overview

This project implements a **client-server polling system** where managed clients periodically query a central server for instructions and report back command execution results.

The client component is designed to poll the server at regular intervals (every 10 seconds) and perform the following workflow:

1. The client makes a **HTTP/HTTPS request** to the server to fetch the next command.
2. The server responds with a command (e.g., `whoami`).
3. The client executes the received command locally.
4. The client sends a follow-up request to the server containing the **result of the command execution**.

This model can also support remote tasking by allowing administrators to set or update the next command that clients should execute.

## Functionality

### Client Behavior

- Periodically (every 10 seconds) contacts the server endpoint.
- Requests the current command to be executed.
- Executes the returned command in the local environment.
- Returns the output of the command back to the server.

### Server Behavior

- Serves a current command when queried by a client.
- Stores/updates commands received from administrators.
- Receives and logs results sent by clients.

## Setting Commands

Administrators can update the command that clients should execute by sending a request to the server with the appropriate data payload. For example:

```bash
curl -X POST https://127.0.0.1:5000/postCMD -k -d "cmd=chdir"
```
(please note that the command above uses -k to ignore certificate verification. Please use --cacert /path/to/file.crt to specify the crt file.)
