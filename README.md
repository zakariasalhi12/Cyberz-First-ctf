# CyberZ Beginner CTF

Welcome to the CyberZ Beginner CTF! This is a small, beginner-friendly Capture The Flag repository built to help learners practice basic web and forensics challenges.

## What is included

This repository contains a few simple challenges across different categories:

- `web/hidden/` - Web challenge with JWT authentication and an admin-only route.
- `web/ssti/` - Simple Flask web app vulnerable to server-side template injection.
- `web/upload/` - Insecure file upload example in PHP.
- `web/meow/` - Java/Tomcat-based challenge with a flag file and an upload/execution concept.
- `misc/Characters/` - A toy network service that reveals one character of a flag at a time.
- `forensics/noisy_traffic/` - A packet capture challenge that requires rebuilding and extracting hidden data.
- `forensics/intro/` - A beginner-friendly network capture sample.

## Why this repo is useful

This is a practice playground for beginners to learn real CTF techniques safely. The code is intentionally simple and easy to read, so you can explore the source and understand the vulnerability.

## How to start

### 1. Clone the repo

```bash
git clone <repo-url>
cd Cyberz-First-ctf
```

### 2. Install Python dependencies

Two Flask apps are included. Use a virtual environment if you like:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r web/hidden/requirements.txt
pip install -r web/ssti/requirements.txt
pip install scapy
```

### 3. Run the web challenges

- `web/hidden` service:

```bash
cd web/hidden
python3 app.py
```

- `web/ssti` service:

```bash
cd web/ssti
python3 app.py
```

- `web/upload` is a PHP app. You can run it with a local PHP server:

```bash
cd web/upload
php -S 0.0.0.0:8000
```

- `web/meow` is intended to run in a Tomcat container. The `Dockerfile` shows how it is packaged.

## Challenge summaries

### 1. Hidden JWT challenge (`web/hidden`)

A small Flask app uses JWT tokens and checks for the `admin` role on `/admin`.

Key learning points:
- JWT creation and validation
- Role-based access control
- How a weak key or token tampering can be abused

### 2. SSTI challenge (`web/ssti`)

A Flask app renders user input directly through `render_template_string`.

Key learning points:
- Server-side template injection
- Why untrusted input must never be passed directly into templates
- How payloads can execute code or leak data

### 3. Upload challenge (`web/upload`)

A PHP upload page accepts only `.jpg` extensions, but does not verify the file contents or MIME type.

Key learning points:
- Insecure file upload handling
- Why extension checks alone are unsafe
- How attackers may try to upload executable content using crafted input

### 4. Java/Tomcat challenge (`web/meow`)

A Tomcat-based challenge that includes a `flag` file and an example exploit script.

Key learning points:
- Java web application behavior
- Upload and file handling attacks against web servers
- How a bad deployment can expose sensitive files

### 5. Network service challenge (`misc/Characters`)

A simple TCP server asks for a flag character index and returns the character.

Key learning points:
- Basic socket programming
- Oracle-style leaks where one bit of secret information is revealed at a time
- Iterating or automating input to recover secrets

### 6. Forensics challenge (`forensics/noisy_traffic`)

A packet capture contains noisy traffic and a hidden payload.

Key learning points:
- Packet capture analysis with `scapy`
- Reassembling transport-layer data from PCAPs
- Finding hidden information inside network traffic

## Tips for beginners

- Read the source code before you attack. These challenges are designed to be learned from.
- Try each challenge locally first.
- Use tools like `curl`, browser DevTools, and Python scripts to experiment.
- For the forensics challenge, inspect the PCAP with Wireshark or use Python to parse packets.

## Notes

- This repo is for learning only. Do not run these apps on a public-facing server.
- Flags are intentionally simple and embedded in the challenge code or files.
- If you want, add your own challenge by copying a folder and changing the code.
