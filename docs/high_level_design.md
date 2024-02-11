# Top Hashtags Engagement Analyzer

## Overview

The Top Hashtags Engagement Analyzer is a web-based application that analyzes and retrieves the top hashtags within a specified date range from a given dataset. The system consists of a backend service responsible for data processing and an interactive frontend for user interaction.

## Components

Here is the system architecture diagram:

![System Architecture](docs/images/system_architecture.png)

### Backend Service

The backend service is responsible for handling data processing and providing an API for fetching top hashtags. It is built using FastAPI, a modern, fast web framework for building APIs with Python.

#### Components:

1. **FastAPI Application (main.py):**

   - Implements the main FastAPI application.
   - Includes CORS middleware for cross-origin resource sharing.
   - Includes routers for handling top hashtags endpoints.

2. **Hashtags Router (hashtags_router.py):**

   - Defines an APIRouter instance to organize routes.
   - Reads CSV data from a file and processes it to extract top hashtags based on click counts.
   - Defines an endpoint for fetching top hashtags within a specified date range.

3. **CSV Data Loader (hashtags_router.py):**
   - Reads CSV data from a specified file path.
   - Provides a function to load and return data from the CSV file.

#### API Endpoints:

- `/top_hashtags` (GET):
  - Accepts start_date and end_date as query parameters.
  - Returns a JSON response containing the top hashtags and their click counts.

### Frontend Service

The frontend service provides an interactive user interface for selecting a date range, calling the backend API, and displaying the results.

#### Components:

1. **React Application (App.js):**

   - Implements the main React application.
   - Allows users to input a date range and submit requests to the backend.
   - Displays the results in an intuitive and user-friendly interface.

2. **API Integration (App.js):**
   - Communicates with the backend API to fetch and display top hashtags based on the selected date range.

## Deployment

The system is containerized using Docker for easy deployment. The Docker Compose configuration defines services for both the backend and frontend.

- **Backend Service Container (backend):**

  - Uses uvicorn as the ASGI server to run the FastAPI application.
  - Exposes the service on port 8000.

- **Frontend Service Container (frontend):**
  - Serves the React application using a production-ready web server.
  - Exposes the service on port 3000.

## Development Environment

- **Programming Languages:**

  - Python for the backend (FastAPI).
  - JavaScript/React for the frontend.

- **Version Control:**

  - Git for source code version control.

- **Dependencies:**
  - FastAPI, uvicorn, Docker, React, npm.

## Future Enhancements

- Implementation of user authentication and authorization.
- Improved data processing algorithms for scalability.
- Support for additional data formats beyond CSV.
- Enhanced user interface features, such as charts and graphs.

This high-level design spec provides an overview of the Top Hashtags Engagement Analyzer system, its components, and deployment details. Detailed technical specifications and diagrams can be included in subsequent documents for a more in-depth understanding of the system architecture.
