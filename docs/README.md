# Top Hashtags Engagement Analyzer

## Table of Contents

- [Backend Service](#backend-service)

  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Run Locally](#run-locally)
    - [Run with Docker](#run-with-docker)
  - [API Documentation](#api-documentation)
  - [Testing](#testing)

- [Frontend Service](#frontend-service)

  - [Getting Started](#getting-started-1)
    - [Prerequisites](#prerequisites-1)
    - [Installation](#installation-1)
  - [Usage](#usage-1)
    - [Run Locally](#run-locally-1)
    - [Run with Docker](#run-with-docker-1)
  - [Styling and UI](#styling-and-ui)
  - [API Integration](#api-integration)

- [Notes](#notes)

  - [To start Docker containers by building images for the entire project](#to-start-docker-containers-by-building-images-for-the-entire-project)
  - [To stop Docker containers](#to-stop-docker-containers)

## Backend Service

This is the backend service for the Top Hashtags Engagement Analyzer, providing an API endpoint to analyze and retrieve the top hashtags within a specified date range.

### Getting Started

#### Prerequisites

- Python 3.7 or later
- Docker (for containerized deployment)

#### Installation

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

### Usage

#### Run Locally

```bash
uvicorn uvicorn_conf:app --host 0.0.0.0 --port 8000 --reload
```

The backend service will be accessible at [http://localhost:8000](http://localhost:8000).

#### Run with Docker

```bash
docker-compose up --build backend
```

The Docker container will expose the service on port 8000.

#### API Documentation

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs) using Swagger UI.

## Testing

To run tests for the backend, you can use the following command:

```bash
pytest backend/tests/
```

## Frontend Service

This is the frontend service for the Top Hashtags Engagement Analyzer, providing a user interface for selecting a date range, calling the backend API, and displaying the results.

### Getting Started

#### Prerequisites

- Node.js and npm

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/top-hashtags-engagement-analyzer.git
   ```

2. Navigate to the frontend folder:

   ```bash
   cd top-hashtags-engagement-analyzer/frontend
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

### Usage

#### Run Locally

```bash
npm start
```

The frontend service will be accessible at [http://localhost:3000](http://localhost:3000).

#### Run with Docker

```bash
docker-compose up --build frontend
```

The Docker container will expose the service on port 3000.

#### Styling and UI

The frontend is designed to provide an intuitive and user-friendly interface for interacting with the Top Hashtags Engagement Analyzer. Feel free to explore and customize the styling based on your design preferences.

#### API Integration

The frontend communicates with the backend API to fetch and display the top hashtags based on the selected date range.

## Notes

#### To start Docker containers by building images for the entire project

```bash
docker-compose up --build -d
```

Just spinning up the docker containers

```bash
docker-compose up -d
```

#### To stop Docker containers

```bash
docker-compose down
```

This command will stop and remove the containers defined in your `docker-compose.yml` file. If you want to remove volumes as well, you can add the `-v` option:

```bash
docker-compose down -v
```

This is useful when you want to clean up all the resources created by your Docker Compose setup. Remember to run these commands from the same directory where your `docker-compose.yml` file is located.
