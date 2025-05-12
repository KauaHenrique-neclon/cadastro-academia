from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user




# criando os varificadores adm
def verificarAdm(f):
    @wraps(f)
    def decorarAdm(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Voce precisa esta logado para acessar")
            return redirect(url_for('login.login_index'))
        
        if current_user.role != 'aluno':
            flash('Acesso não autorizado. Você não tem permissão para acessar esta página.')
            return redirect(url_for('login.login_index'))
        return f(*args, **kwargs)
    return decorarAdm