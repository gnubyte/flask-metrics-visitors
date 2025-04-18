# Flask Metrics Visitors

A Flask extension for tracking and visualizing visitor metrics.

## Features

- Track visitor sessions and page views
- Display real-time session analytics
- Filterable session data with DataTables
- Session duration and click tracking
- Page URL tracking
- Timezone-aware timestamps
- Persistent SQLite database storage

## Demo

### Dashboard Overview
![Dashboard Overview](screenshots/dash1.png)

### Session Analytics
![Session Analytics](screenshots/dash2.png)

### Detailed Session View
![Detailed Session View](screenshots/dash3.png)

## Requirements

- Python 3.7 or higher
- Flask 2.0.0 or higher
- Flask-SQLAlchemy 3.0.0 or higher
- Flask-Login 0.6.0 or higher

## Installation

```bash
pip install flask-metrics-visitors
```

## Development Setup

To build the package locally:

1. Install build dependencies:
```bash
pip install twine
```

2. Build the package with version increment:
```bash
# For a patch release (bug fixes)
./build.sh patch

# For a minor release (new features)
./build.sh minor

# For a major release (breaking changes)
./build.sh major
```

3. Upload to PyPI (if you have access):
```bash
./push.sh
```

The version number follows semantic versioning (MAJOR.MINOR.PATCH):
- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality
- PATCH version for backwards-compatible bug fixes

## Setup

You can initialize the extension in two ways:

### 1. Direct Initialization

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_metrics_visitors import MetricsVisitors

app = Flask(__name__)
db = SQLAlchemy(app)

# Initialize the metrics extension
metrics = MetricsVisitors(app, db)

# Get and register the blueprint after initialization
app.register_blueprint(metrics.get_blueprint())
```

### 2. Factory Pattern (Recommended)

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_metrics_visitors import MetricsVisitors

db = SQLAlchemy()
metrics = MetricsVisitors()

def create_app():
    app = Flask(__name__)
    
    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metrics.db'
    app.config['METRICS_VISITORS_SESSION_LIFETIME'] = 30
    app.config['METRICS_VISITORS_UPDATE_INTERVAL'] = 30
    
    # Initialize extensions
    db.init_app(app)
    metrics.init_app(app, db)
    
    # Register the blueprint after initialization
    app.register_blueprint(metrics.get_blueprint())
    
    return app

app = create_app()
```

3. Include the session tracking JavaScript in your base template:

```html
<script src="{{ url_for('metrics_visitors.static', filename='js/session-tracker.js') }}"></script>
```

4. Create the database tables:

```python
with app.app_context():
    db.create_all()
```

## Database Configuration

The extension uses SQLite for persistent storage of session data. By default, the database is stored in the application's instance folder. You can configure the database path using:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/your/database.db'
```

### Database Backup

It's recommended to implement regular backups of your SQLite database. Here's a simple backup strategy:

1. Create a backup directory:
```bash
mkdir -p backups
```

2. Set up a cron job to backup the database daily:
```bash
0 0 * * * cp /path/to/your/database.db /path/to/backups/database_$(date +\%Y\%m\%d).db
```

### Database Maintenance

The extension automatically:
- Cleans up old session data based on the configured retention period
- Handles database migrations when the schema changes
- Optimizes the database for performance

## Usage

1. Access the metrics dashboard at `/metrics`
2. View session analytics at `/metrics/session-analytics`
3. Session data is automatically tracked and updated every 30 seconds
4. Use the DataTables interface to filter and sort session data

## Session Tracking

The session tracker automatically:
- Tracks session duration
- Counts clicks
- Records page URLs
- Updates stats periodically
- Sends final stats on page unload
- Handles page visibility changes

## Configuration

The following configuration options are available:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metrics.db'  # SQLite database path
app.config['METRICS_VISITORS_SESSION_LIFETIME'] = 30  # Session lifetime in days
app.config['METRICS_VISITORS_UPDATE_INTERVAL'] = 30  # Update interval in seconds
```

## Package Information

- **Author**: Patrick Hastings
- **License**: MIT
- **Python Support**: 3.7, 3.8, 3.9, 3.10
- **Development Status**: Beta
- **Framework**: Flask
- **Environment**: Web Environment

## License

MIT