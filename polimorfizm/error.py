class PasswordError(Exception):
    
    def __init__(self, error: str):
        self.error = error        
    
    def __str__(self) -> str:
        return self.error