# Conversational Care Engine Architecture

## Overview

The Conversational Care Engine is a lightweight multi-turn health coaching backend built with FastAPI.

## Request Flow

User
↓
FastAPI API
↓
Session Memory
↓
Health Coaching Engine
↓
Conversation Summarizer
↓
Response

## Components

### FastAPI API

Handles incoming requests and returns responses.

### Session Memory

Stores user conversation history in memory.

### Health Coaching Engine

Provides condition-specific recommendations.

Supported conditions:

* Diabetes
* Thyroid
* Obesity

### Summarizer

Generates compact summaries of recent interactions.

## Future Improvements

* Redis session storage
* OpenAI/Gemini integration
* Twilio voice interface
* Whisper speech-to-text
* User authentication
* Analytics dashboard
