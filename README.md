# Abdullah-innovaxel-khan
# URL Shortener API

A simple and efficient RESTful API service for shortening URLs, built with Flask and SQLite.

## Overview

This application provides a URL shortening service that allows users to create, retrieve, update, and delete short URLs. It also tracks statistics on how many times each short URL has been accessed.

## Features

- Shorten long URLs into short, manageable links
- Retrieve original URLs using short codes
- Update existing short URLs
- Delete short URLs
- Track and display usage statistics

## Technology Stack

- Backend: Flask (Python)
- Database: SQLite
- ORM: SQLAlchemy

## API Endpoints

| Endpoint                      | Method | Description                          |
|--------------------------------|--------|--------------------------------------|
| `/shorten`                    | POST   | Create a new short URL              |
| `/shorten/<short_code>`       | GET    | Retrieve details of a short URL     |
| `/shorten/<short_code>`       | PUT    | Update an existing short URL        |
| `/shorten/<short_code>`       | DELETE | Delete a short URL                  |
| `/shorten/<short_code>/stats` | GET    | Get usage statistics for a short URL |
| `/r/<short_code>`             | GET    | Redirect to the original URL        |

## Setup Instructions

### Prerequisites

- Python 3.8+
- SQLite (built-in with Python)
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```
  git clone https://github.com/Abdullahkhan106/Abdullah-innovaxel-khan.git
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

4. Initialize the database:
   ```
   python db_setup.py
   ```

### Running the Application

1. Start the Flask server:
   ```
   flask run
   ```

2. Access the application:
   - API base URL: `http://localhost:5000`

## Usage Examples

### Create a short URL

```
curl -X POST http://localhost:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/some/long/url"}'
```

### Retrieve a short URL

```
curl -X GET http://localhost:5000/shorten/abc123
```

### Update a short URL

```
curl -X PUT http://localhost:5000/shorten/abc123 \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/updated/url"}'
```

### Delete a short URL

```
curl -X DELETE http://localhost:5000/shorten/abc123
```

### Get statistics for a short URL

```
curl -X GET http://localhost:5000/shorten/abc123/stats
```

## Development Notes

- Uses SQLAlchemy as the ORM for database interactions.
- Short codes are generated uniquely and randomly.
- Validates URLs to ensure proper formatting.
- Tracks access counts for each short URL.
- Simple web interface for managing URLs.

## Project Structure

```
url-shortener/
├── app.py                # Main application file
├── db_setup.py           # Database setup script
├── models.py             # Database models
├── config.py             # Configuration settings
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Future Enhancements

- User authentication and authorization
- Custom short code selection
- QR code generation for short URLs
- Analytics dashboard
- API rate limiting
- Expiration dates for short URLs

## License

This project is licensed under the MIT License - see the LICENSE file for details.


