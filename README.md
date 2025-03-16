# Abdullah-innovaxel-khan
# URL Shortener API

A RESTful API service for shortening URLs built with Flask and SQLITE.

## Overview

This application provides a URL shortening service that allows users to create, retrieve, update, and delete short URLs. It also tracks statistics about how many times each short URL has been accessed.

## Features

- Create short URLs from long URLs
- Retrieve original URLs using short codes
- Update existing short URLs
- Delete short URLs
- Track and display usage statistics

## Technology Stack

- Backend: Flask (Python)
- Database: SQLITE
- ORM: SQLAlchemy

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/shorten` | POST | Create a new short URL |
| `/shorten/<short_code>` | GET | Retrieve details of a short URL |
| `/shorten/<short_code>` | PUT | Update an existing short URL |
| `/shorten/<short_code>` | DELETE | Delete a short URL |
| `/shorten/<short_code>/stats` | GET | Get usage statistics for a short URL |
| '/shorten/<short_code>/stats' | GET | Redirect to the original URL |

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL database
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/firstname-innovaxel-lastname.git
   cd Abdullah-innovaxel-khan


   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
   ```sql
   CREATE DATABASE url_shortener;
   USE url_shortener;
   ```


5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

### Running the Application

1. Start the Flask server:
   ```
   flask run
   ```

2. Access the application:
   - Web interface: http://localhost:5000
   - API: http://localhost:5000/shorten

## Usage Examples

### Create a short URL

```bash
curl -X POST http://localhost:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/some/long/url"}'
```

### Retrieve a short URL

```bash
curl -X GET http://localhost:5000/shorten/abc123
```

### Update a short URL

```bash
curl -X PUT http://localhost:5000/shorten/abc123 \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/updated/url"}'
```

### Delete a short URL

```bash
curl -X DELETE http://localhost:5000/shorten/abc123
```

### Get statistics for a short URL

```bash
curl -X GET http://localhost:5000/shorten/abc123/stats
```

## Development Notes

- The application uses SQLAlchemy as an ORM for database interactions
- Short codes are generated randomly and are guaranteed to be unique
- The application validates URLs to ensure they are properly formatted
- Access counts are tracked for each short URL
- The web interface provides a simple way to create and use short URLs

## Project Structure

```
url-shortener/
├── shortner.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
```

## Future Improvements

- User authentication and authorization
- Custom short code selection
- QR code generation for short URLs
- Analytics dashboard
- API rate limiting
- Expiration dates for short URLs

## License

This project is licensed under the MIT License - see the LICENSE file for details.
