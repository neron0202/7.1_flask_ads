from app_pac import app_var
from app_pac import db
from app_pac.api import bp
from app_pac.models import User
from flask import request


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    results = [
        {
            'id': user.id,
            'login': user.login,
            'password': user.password,
            # 'advert': user.advert
        } for user in users
    ]
    return {'count': len(results), 'users': results}

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    response = {
        'id': user.id,
        'login': user.login,
        'password': user.password,
    }
    return {"message": "success", "user": response}


@bp.route('/users', methods=['POST'])
def create_user():
    if request.is_json:
        data = request.get_json()
        new_user = User(login=data['login'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': f'User {new_user.login} has been created'}
    else:
        return {'error': "The request payload is not in JSON format"}




@bp.route('/ads/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User named #{user.login}# has been successfully deleted"}


