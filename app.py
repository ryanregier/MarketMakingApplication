from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import Market as mrkt

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///markets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class MarketModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    asset_type = db.Column(db.String(100), nullable=False)
    ticker = db.Column(db.String(100), nullable=False)


# db.create_all() # only run this line once and then comment out or it will delete the db

markets = {}

market_put_args = reqparse.RequestParser()
market_put_args.add_argument("name", type=str, help="Name of the market is required", required=True)
market_put_args.add_argument("asset_type", type=str, help="Asset type of the market is required", required=True)
market_put_args.add_argument("ticker", type=str, help="Ticker of the market is required", required=True)

market_update_arg = reqparse.RequestParser()
market_update_arg.add_argument("name", type=str, help="Name of the market")
market_update_arg.add_argument("asset_type", type=str, help="Asset type of the market")
market_update_arg.add_argument("ticker", type=str, help="Ticker of the market")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'asset_type': fields.String,
    'ticker': fields.String
}


class Market(Resource):
    @marshal_with(resource_fields)
    def get(self, market_id):
        result = MarketModel.query.filter_by(id=market_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, market_id):
        args = market_put_args.parse_args()
        result = MarketModel.query.filter_by(id=market_id).first()
        if result:
            abort(409, message="Market id already exists")
        market = MarketModel(id=market_id, name=args['name'], asset_type=args['asset_type'], ticker=args['ticker'])
        db.session.add(market)
        db.session.commit()
        return market, 201

    @marshal_with(resource_fields)
    def patch(self, market_id):
        args = market_update_arg.parse_args()
        result = MarketModel.query.filter_by(id=market_id).first()
        if not result:
            abort(404, message="Market does not exist with that id")
        if args['name']:
            result.name = args['name']
        if args["asset_type"]:
            result.asset_type = args['views']
        if args["ticker"]:
            result.ticker = args['ticker']
        db.session.commit()
        return result, 204

    @marshal_with(resource_fields)
    def delete(self, market_id):
        result = MarketModel.query.filter_by(id=market_id)
        if not result:
            abort(404, message="Could not find the market id to delete")
        result.delete()
        db.session.commit()
        return '', 204


api.add_resource(Market, "/market/<int:market_id>")

if __name__ == '__main__':
    app.run(port=80, debug=True)
