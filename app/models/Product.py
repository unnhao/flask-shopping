from app.extensions import db, ma
from datetime import datetime



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Integer)
    image = db.Column(db.String(1024))
    url = db.Column(db.String(1024))
    description = db.Column(db.String(1024))
    product_type = db.Column(db.String(256))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id'          : self.id,
            'name'        : self.name,
            'price'       : self.price,
            'image'       : self.image,
            'url'         : self.url,
            'description' : self.description,
            'product_type': self.product_type,
            'category': self.category.serialize
        }

class ProductSchema(ma.Schema):
    name = ma.Str(required=True)
    price = ma.Int(required=True)
    image = ma.Str(required=True)
    url = ma.Str(required=True)
    description = ma.Str(required=True)
    product_type = ma.Str(required=True)
    category = ma.Str(required=True)
