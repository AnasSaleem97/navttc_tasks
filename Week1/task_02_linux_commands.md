# Task 02 — Linux Commands Practice

Practice the following commands in your Linux terminal.
Each command is listed with a short description of what it does.

---

## Navigation Commands

| Command | What it does |
|---------|-------------|
| `pwd` | Print current working directory |
| `cd foldername` | Change into a folder |
| `cd ..` | Go one level up |
| `ls` | List files in current directory |
| `ls -la` | List files with details and hidden files |

## File and Folder Commands

| Command | What it does |
|---------|-------------|
| `mkdir myfolder` | Create a new folder |
| `touch myfile.txt` | Create an empty file |
| `rm myfile.txt` | Delete a file |
| `rmdir myfolder` | Delete an empty folder |
| `cp file1.txt file2.txt` | Copy a file |
| `mv file1.txt newname.txt` | Move or rename a file |

## Reading Files

| Command | What it does |
|---------|-------------|
| `cat myfile.txt` | Show full file content |
| `more myfile.txt` | Show file content page by page |
| `less myfile.txt` | Similar to more, but scroll up/down |
| `head myfile.txt` | Show first 10 lines |
| `file myfile.txt` | Show what type of file it is |

## System Commands

| Command | What it does |
|---------|-------------|
| `sudo command` | Run command as administrator |
| `man ls` | Open manual/help for any command |
| `shutdown now` | Shut down the system |
| `restart` | Restart the system |
| `ps` | List running processes |
| `kill 1234` | Kill a process by its PID |

## Text Editing and Scripting

| Command | What it does |
|---------|-------------|
| `nano myfile.txt` | Open file in nano text editor |
| `bash script.sh` | Run a bash script |
| `sh script.sh` | Run a shell script |
| `chmod +x script.sh` | Give execute permission to a script |

## Software Management

| Command | What it does |
|---------|-------------|
| `sudo apt update` | Update the package list |
| `sudo apt upgrade` | Upgrade installed packages |
| `sudo dpkg -i package.deb` | Install a .deb package |

## Redirection and Aliases

| Command | What it does |
|---------|-------------|
| `echo "hello" > file.txt` | Write output to a file |
| `echo "world" >> file.txt` | Append output to a file |
| `alias ll='ls -la'` | Create a shortcut command |

## Environment Variables

| Command | What it does |
|---------|-------------|
| `echo $HOME` | Print the HOME variable |
| `export MYVAR="hello"` | Set an environment variable |
| `echo $MYVAR` | Print your variable |
