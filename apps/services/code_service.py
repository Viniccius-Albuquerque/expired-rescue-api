from apps.modules.code_modules import CodeCreate, CodeGet, CodeValidate
from apps.repository.code_repository import CodeRepository
from apps.repository.users_repository import UserRepository
import random
import datetime

class CodeService:
    def __init__(self):
        self.code_repository = CodeRepository()
        
    def generate_code(self):
        return random.randint(1000, 9999)
        
    def create_code(self, email, id_user=None):
        code = CodeCreate(email, id_user)
        value = self.generate_code()
        time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        
        result = self.code_repository.create_code(value, time, code.id_user, code.email)
        if result is None:
            raise ValueError("Erro ao criar o código")
        
        return result
        
    def delete_code(self, id_code):
        code = CodeGet(id_code)
        
        result = self.code_repository.delete_code(code.id_code)
        if result == 0:
            raise ValueError("Código não encontrado")
        
        return result
    
    def valid_code(self, id_user, user_code, email):
        code = CodeValidate(id_user, user_code, email)
        
        if id_user is not None:
            verificacao = UserRepository.get_user(code.id_user)
            if verificacao is None:
                raise ValueError("Usuário não encontrado")
            
        result = self.code_repository.valid_code(code.id_user, code.user_code, code.email)
        if result == 0:
            raise ValueError("Código inválido ou expirado")
        
        return 1