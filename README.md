# Visited Links Service

This is a simple web service that allows you to track and retrieve a list of unique domains visited by an employee. The
service accepts a list of visited links and provides functionality to retrieve domains within specified time intervals.

## Getting Started

To run in docker:

```bash
docker-compose up --build -d
```

## Endpoints

### POST /visited_links

Submit a list of links visited by an employee.

### GET /visited_domains

Retrieve a list of unique visited domains within a specified time range.
