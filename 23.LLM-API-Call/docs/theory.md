# Interacting with Large Language Models (LLMs) via API

This document provides a brief overview of the theoretical concepts used in this project.

## Application Programming Interfaces (APIs)
An API allows different software systems to communicate with each other. In this project, we use an API to communicate with a remote server that hosts an LLM. We send our prompt as part of an HTTP request, and the server returns the generated response.

## OpenAI Compatible Endpoints
Many services that host LLMs provide APIs that match the specification of the OpenAI API. This allows developers to use standard libraries like the official `openai` Python package, simply by changing the `base_url` to point to the alternative service (in our case, `https://api.ai-box.vn/v1`).

## Environment Variables
Hardcoding secrets like API keys directly into your code is a major security risk. Instead, we store these secrets in a `.env.local` file and load them into the application's environment variables at runtime. This keeps sensitive information out of version control systems like Git.
