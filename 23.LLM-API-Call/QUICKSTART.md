# Quickstart Guide

Follow these steps to run the LLM API Call script.

## 1. Prerequisites
Ensure you have `uv` and Python installed on your system.

## 2. Environment Setup
The API key is required to authenticate with the AI Box API endpoint.
We already created a `.env.local` file for you with the following content:

```env
AI_BOX_API_KEY=sk-your-api-key
```

## 3. Running the Application
The `Makefile` simplifies running the script.

To execute the application:
```bash
make run
```
This command uses `uv` to run `main.py` securely, ensuring all dependencies are handled.

## 4. Running the Tests
To ensure everything is working correctly, you can run the minimal end-to-end tests provided:
```bash
make test
```
