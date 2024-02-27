# Flask URL Shortener

This is a simple URL shortening service created with Flask, a Python web framework. It allows users to enter a long URL and receive a shortened version of it, which redirects to the original URL when accessed.

## Features

- **URL Shortening**: Convert long URLs into manageable short links.
- **Redirect**: Use the short link to redirect to the original URL.
- **Database Storage**: Store the original and short URLs in a database.

## Installation

To get started with this project, you'll need to have Python installed on your system. Once you have Python, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install Dependencies**

   ```sh
   pip install Flask Flask-SQLAlchemy
   ```
3. **Environment Variables**
   Set the `DATABASE_URL` environment variable to your database connection URI.

   ```sh
   export DATABASE_URL="sqlite:///your-database.db"  # Example for SQLite
   ```
4. **Initialize the Database**
   With the Flask application context, create the database tables.

   ```sh
   from yourapp import db
   with app.app_context():
       db.create_all()
   ```

## Usage
To start the server, run:

```sh
flask run
```

Now, you can access the application in your web browser at http://127.0.0.1:5000/.

## Endpoints

- `POST /shorten`: Accepts a URL and returns a shortened version.
- `GET /<shortened_url>`: Redirects to the original URL associated with the shortened link.

## How It Works

1. **Shortening a URL**

   Send a POST request to the `/shorten` endpoint with the URL you wish to shorten. The server will generate a unique short identifier and return a JSON response with the shortened URL.

2. **Redirecting a Short URL**

   When you visit a short URL, the server looks up the short identifier in the database, retrieves the original URL, and redirects you to it.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements or suggestions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.




    
