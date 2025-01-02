# scripts/clear_db.sh
#!/bin/bash
echo "Clearing database..."
python manage.py flush --no-input
python manage.py migrate
