from app_pac import app_var
from app_pac import db
from app_pac.api import bp
from app_pac.models import Advert
from flask import request

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
    ad = Advert.query.get_or_404(id)
    response = {
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'created_at': ad.created_at,
        'user_id': ad.user_id
    }
    return {"message": "success", "advertisement": response}

@bp.route('/ads', methods=['POST'])
def create_ad():
    if request.is_json:
        data = request.get_json()
        new_ad = Advert(title=data['title'], description=data['description'], user_id=data['user_id'])
        db.session.add(new_ad)
        db.session.commit()
        return {'message': f'Advertisment named #{new_ad.title}# has been created'}
    else:
        return {'error': "The request payload is not in JSON format"}


@bp.route('/ads/<int:id>', methods=['DELETE'])
def delete_ad(id):
    ad = Advert.query.get_or_404(id)
    db.session.delete(ad)
    db.session.commit()
    return {"message": f"Advertisement named #{ad.title}# has been successfully deleted"}


# @bp.route('/ads/<int:id>', methods=['PUT'])
# def update_ad(id):
#     ad = Advert.query.get_or_404(id)
#     data = request.get_json()
#
#     ad.id = data['id']
#     ad.title = data['title']
#     ad.description = data['description']
#     ad.created_at = data['created_at']
#     ad.user_id = data['user_id']
#
#     db.session.add(ad)
#     db.session.commit()
#
#     return {"message": f"Advertisement named #{ad.title}# has been successfully updated"}
