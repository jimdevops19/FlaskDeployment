from market import app
import os

#Checks if the run.py file has executed directly and not imported
# Run this command to run the application in DEBUG mode
# docker run -p 5000:5000 -e DEBUG=1 <image-name>
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG') == '1')