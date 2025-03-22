echo [$(date)]: "START"
echo [$(date)]: "Creating venv with python 3.12"
python3 -m venv venv
echo [$(date)]: "Activate env"
source venv/bin/activate
echo [$(date)]: "Install required packages"
pip install -r requirements.txt
echo [$(date)]: "End"