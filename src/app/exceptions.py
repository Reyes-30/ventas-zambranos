from dataclasses import dataclass

class AppError(Exception):
    """Error base de la aplicación con mensaje amigable."""
    def __init__(self, message: str, detail: str | None = None):
        super().__init__(message)
        self.detail = detail

@dataclass
class ValidationError(AppError):
    """Errores de validación de datos o esquema."""
    message: str
    detail: str | None = None

@dataclass
class FileIOError(AppError):
    """Errores de entrada/salida de archivos."""
    message: str
    detail: str | None = None

@dataclass
class ProcessingError(AppError):
    """Errores durante procesamiento/ML."""
    message: str
    detail: str | None = None
