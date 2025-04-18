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

## Installation

```bash
pip install flask-metrics-visitors
```

## Development Setup

To build the package locally:

1. Install build dependencies:
```bash
pip install build twine
```

2. Build the package:
```bash
./build.sh
```

3. Upload to PyPI (if you have access):
```bash
./push.sh
```

## Setup

You can initialize the extension in two ways:

### 1. Direct Initialization

```python
from flask import Flask
from flask_metrics_visitors import MetricsVisitors

app = Flask(__name__)
metrics = MetricsVisitors(app)
```

### 2. Factory Pattern (Recommended)

```python
from flask import Flask
from flask_metrics_visitors import MetricsVisitors

metrics = MetricsVisitors()

def create_app():
    app = Flask(__name__)
    metrics.init_app(app)
    return app

app = create_app()
```

3. Include the session tracking JavaScript in your base template:

```html
<script src="{{ url_for('metrics_visitors.static', filename='js/session-tracker.js') }}"></script>
```

4. Add the metrics blueprint to your application:

```python
app.register_blueprint(metrics.blueprint)
```

5. Create the database tables:

```python
with app.app_context():
    metrics.db.create_all()
```

## Database Configuration

The extension uses SQLite for persistent storage of session data. By default, the database is stored in the application's instance folder. You can configure the database path using:

```python
app.config['METRICS_VISITORS_DB_PATH'] = 'path/to/your/database.db'
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
app.config['METRICS_VISITORS_DB_PATH'] = 'metrics.db'  # SQLite database path
app.config['METRICS_VISITORS_SESSION_LIFETIME'] = 30  # Session lifetime in days
app.config['METRICS_VISITORS_UPDATE_INTERVAL'] = 30  # Update interval in seconds
```

## License

MIT 