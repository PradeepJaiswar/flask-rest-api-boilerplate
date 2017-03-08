import os
from app import create_app
from config.env import get_config

app = create_app(get_config('LOCAL'))

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port, debug=True)
