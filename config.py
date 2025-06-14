import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your-secret-key-here'
    DATA_FOLDER = os.path.join(BASE_DIR, 'data')
    UPLOAD_FOLDER = os.path.join(DATA_FOLDER, 'uploads')
    MODEL_FOLDER = os.path.join(DATA_FOLDER, 'models')
    EXPENSE_FILE = os.path.join(DATA_FOLDER, 'pengeluaran.csv')
    ALLOWED_EXTENSIONS = {'csv'}
    
    @staticmethod
    def init_app(app):
        # Ensure folders exist
        os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['MODEL_FOLDER'], exist_ok=True)
