# Django WebSocket Chatbot

## Overview

This project is a minimal WebSocket-based chatbot built using Django and Django Channels. The goal was not to create a sophisticated chat program but rather to learn how to establish real-time communication using Django and WebSockets. This serves as a stepping stone for future projects requiring real-time interaction, such as implementing an AI opponent in a game.

## Features

WebSocket Connection: Handles real-time bidirectional communication.

Basic Chatbot Logic: Responds to predefined messages.

No Frontend Required: Interact with the chatbot using command-line WebSocket clients.

## Installation & Setup

### Prerequisites

Ensure you have Python 3.8+ installed.

### 1. Clone the Repository
```bash
git clone <repository_url>
cd django-chatbot
```
### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install django daphne channels
```
## 4. Create a Django Project & App

Run migrations to set up the database:
```bash
python manage.py migrate
```
### 5. Start the Server
```bash
daphne -b 0.0.0.0 -p 8000 chatbot.asgi:application
```
## Usage

#### Connect to the Chatbot

Use wscat (or any WebSocket client) to interact:
```bash
npm install -g wscat
wscat -c ws://localhost:8000/ws/chat/
```
### Send Messages

Type JSON messages like:
```
{"message": "hello"}
{"message": "bye"}
{"message": "help"}
```
Expected response:
```
{"response": "Hello! How can I help you?"}
```
## Project Structure
```
django-chatbot/
│── chatbot/                 # Django project root
│   ├── settings.py          # Django settings
│   ├── asgi.py              # ASGI configuration
│   ├── urls.py              # URL routing
│── chat/                    # Django app
│   ├── consumers.py         # WebSocket consumer logic
│   ├── routing.py           # WebSocket routes
│── manage.py                # Django entry point
```
## Notes

- This project only serves as a learning exercise for Django WebSockets.

- The chatbot responses are hardcoded for simplicity.

- For a real project, you’d use a database, authentication, and more advanced AI handling.
