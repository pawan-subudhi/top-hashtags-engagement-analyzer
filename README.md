# Top Hashtags Engagement Analyzer

## Backend Service

This is the backend service for the Top Hashtags Engagement Analyzer. It provides an API endpoint to analyze and retrieve the top hashtags within a specified date range.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run Locally](#run-locally)
  - [Run with Docker](#run-with-docker)
- [API Documentation](#api-documentation)

## Getting Started

### Prerequisites

- Python 3.7 or later
- Docker (for containerized deployment)
- Pipenv (optional, but recommended for managing dependencies)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/top-hashtags-engagement-analyzer.git
   ```

2. Navigate to the backend folder:

   ```bash
   cd top-hashtags-engagement-analyzer/backend
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Locally

```bash
uvicorn uvicorn_conf:app --host 0.0.0.0 --port 8000 --reload
```

The backend service will be accessible at `http://localhost:8000`.

### Run with Docker

```bash
docker-compose up --build backend
```

The Docker container will expose the service on port 8000.

## API Documentation

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs) using Swagger UI.
