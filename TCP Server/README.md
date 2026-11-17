COSC 2327 TCP Group Chat Application

Overview

This project is a TCP-based chat application developed for COSC 2327: Introduction to Computer Networks.



The application supports:



Multiple concurrent clients

Username-based chat

Color-coded usernames

Multiple chat groups

Group-isolated messaging

Single-server architecture

Clients connect to a central TCP server and exchange messages through group channels. Messages sent within a group are only visible to members of that group.



Features

Step 1

Basic TCP client/server communication

Two clients communicate through a single server

Step 2

Multiple concurrent clients

Username support

Colored usernames

Connection and disconnection notifications

Step 3

Multiple chat groups

Dynamic group creation

Group-isolated message broadcasting

Group management commands

Project Structure

TCP\_Server/

│

├── server/

│   ├── \_\_init\_\_.py

│   ├── server.py

│   ├── client\_handler.py

│   └── groups.py

│

├── client/

│   ├── \_\_init\_\_.py

│   ├── client.py

│   └── commands.py

│

├── shared/

│   ├── \_\_init\_\_.py

│   ├── config.py

│   └── protocol.py

│

├── screenshots/

│

├── requirements.txt

│

└── README.md

Requirements

Python 3.14 or newer

External packages:



pip install colorama

If Colorama is not used, no external dependencies are required.



Running the Server

From the project root:



python -m server.server

Expected output:



Server listening on 127.0.0.1:12000

Running a Client

Open a new terminal:



python -m client.client

Enter a username when prompted:



Enter username: Alpha

Open additional terminals to connect more clients.



Available Commands

Join a Group

/join networking

Example:



/join gaming

List Available Groups

/groups

Example output:



Groups: general, networking, gaming, security

Example Usage

Client Alpha:



/join networking

Hello team

Client Beta:



/join networking

Client Beta receives:



\[networking] Alpha: Hello team

Client Charlie:



/join gaming

Client Charlie does not receive networking messages.



Network Design

The application uses:



TCP sockets

Multi-threaded server architecture

One thread per connected client

Centralized message routing

Group-based message broadcasting

Communication flow:



&#x20;         Client A

&#x20;             |

&#x20;             |

Client B ---- Server ---- Client C

&#x20;             |

&#x20;             |

&#x20;         Client D

Group routing:



Networking Group

\----------------

Alpha

Beta



Gaming Group

\------------

Charlie

Delta

Messages stay within their assigned groups.



Testing Completed

Client-to-client communication

Multiple concurrent connections

Group isolation

User join notifications

User disconnect notifications

Dynamic group creation

Colored username display

Author

Benjamin Costantino



COSC 2327 - Introduction to Computer Networks



Fall 2026

