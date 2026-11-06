from apps.schemas.users_schemas import UserCreate, UserLoginSchemas, UserUpdateSchemas, UserPasswordUpdateSchemas
from apps.repository.users_repository import UserRepository
import bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def register_user(self, name, password, email):
        user_create = UserCreate(name=name, password=password, email=email)
        
        existing_user = self.user_repository.get_user_by_email(user_create.email)
        if existing_user:
            raise ValueError("O usuário com esse email já está cadastrado")

        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
        return self.user_repository.register_user(
            user_create.name,
            password_hash,
            user_create.email,
        )


    def login(self,email, password):
        login_data = UserLoginSchemas(email=email, password=password)
        user = self.user_repository.get_user_by_email(login_data.email)
        if not user:
            raise ValueError("Email ou senha inválidos")
        if not bcrypt.checkpw(login_data.password.encode('utf-8'), user["password"].encode('utf-8')):
            raise ValueError("Email ou senha inválidos")
        user.pop("password", None)
        return user


    def update_user(self,id_user, name, email, adress, img):
        user_update = UserUpdateSchemas( name=name, email=email,adress=adress, img=img)
        user_existing = self.user_repository.get_user(id_user=id_user)
        if not user_existing:
            raise ValueError("Usuário não encontrado")
        if user_existing["type"] == 'client' and not user_update.adress:
            raise ValueError("Endereço do usuário é obrigatório para clientes")
        return self.user_repository.update_user(
            id_user,
            user_update.name,
            user_update.email,
            user_update.adress,
            user_update.img
        ) 


    def update_password(self,id_user,password,new_password):
        user_password_update = UserPasswordUpdateSchemas(password=password, new_password=new_password)
        user_existing = self.user_repository.get_user(id_user=id_user)
        if not user_existing:
            raise ValueError("Usuário não encontrado")
        if not bcrypt.checkpw(user_password_update.password.encode('utf-8'), user_existing["password"].encode('utf-8')):
            raise ValueError("Senha atual incorreta")
        new_password_bytes = user_password_update.new_password.encode('utf-8')
        salt = bcrypt.gensalt()
        new_password_hash = bcrypt.hashpw(new_password_bytes, salt).decode('utf-8')
        return self.user_repository.update_password(
            id_user,
            user_password_update.password,
            new_password_hash
        )


    def list_users(self):
        users = self.user_repository.list_users()
        for user in users:
            user.pop("password", None)
        return users


    def get_user(self,id_user):
        user = self.user_repository.get_user(id_user=id_user)
        if not user:
            raise ValueError("Usuário não encontrado")
        user.pop("password", None)
        return user


    def delete_user(self,id_user):
        user_existing = self.user_repository.get_user(id_user=id_user)
        if not user_existing:
            raise ValueError("Usuário não encontrado")
        return self.user_repository.delete_user(id_user=id_user)