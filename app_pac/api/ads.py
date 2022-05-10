from app_pac import db
from app_pac.api import bp
from app_pac.models import Advert
from requests import request

@bp.route('/ads', methods=['GET'])
def get_ads():
    ads = Advert.query.all()
    results = [
        {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'created_at': ad.created_at,
            'user_id': ad.user_id
        } for ad in ads
    ]
    return {'count': len(results), 'ads': results}


@bp.route('/ads/<int:id>', methods=['GET'])
def get_ad(id):
    pass


@bp.route('/ads', methods=['POST'])
def create_ad():
    if request.is_json:
        data = request.get_json()
        new_ad = Advert(title=data['title'], description=data['description'], user_id=data['user_id'])
        db.session.add(new_ad)
        db.session.commit()
        return {'message': f'User {new_ad.login} has been created'}
    else:
        return {'error': "The request payload is not in JSON format"}


@bp.route('/ads/<int:id>', methods=['PUT'])
def update_ad(id):
    pass


@bp.route('/ads/<int:id>', methods=['DELETE'])
def delete_ad(id):
    pass

