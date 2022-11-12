# PyMultiNotifier

A python flet app to post messages to Discord, Twitter or Telegram (more platforms could be supported in later versions).


## Installation
### 1. Configuration of the app

Config file is needed!

1. Copy the file `pymultinotifier/doc/examples/config_example.toml` in 
path `pymultinotifier/pymultinotifier/config/` and rename the file to `config.toml` 

2. Add your platform credentials (you can remove platforms by deleting the whole related section)

## Development

### Database Management
#### Alembic ASYNC:
alembic init alembic

#### Alembic Auto-Migration
alembic revision --autogenerate -m "MIGRATION NAME"

#### Alembic Upgrade:
alembic upgrade head
