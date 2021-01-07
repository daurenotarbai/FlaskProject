from flask import Blueprint
from flask import Flask,request,url_for,render_template,redirect
from flask_login import login_required, current_user
from . import db
from .models import CategoryModel
from markupsafe import escape


main = Blueprint('main',__name__)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)



@main.route('/',methods=['POST','GET'])
def index():
    categories = CategoryModel.query.order_by(CategoryModel.date_created).all()
    return render_template('index.html',categories = categories)

@main.route('/remove-category/<int:id>',methods=['POST','GET'])
def removingCategory(id):
    query = CategoryModel.query.get_or_404(id)
    if query :
        db.session.delete(query)
        db.session.commit()
        return redirect('/')
    else:
        return "Some Issue"

@main.route('/update-category/<int:id>',methods=['POST','GET'])
def updateCategory(id):
    query = CategoryModel.query.get_or_404(id)
    if request.method =='POST':
        query.category_name = request.form['category_name']
        query.category_season = request.form['category_season']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Some issue "
    else:
        return render_template('update_category.html',category=query)

@main.route('/add-category',methods=['POST','GET'])
def addingCategory():
    if request.method =='POST':
        category_name = request.form['category_name']
        category_season = request.form['category_season']
        new_category = CategoryModel(category_name = category_name,category_season=category_season)
        try:
            db.session.add(new_category)
            db.session.commit()
            return redirect('/')
        except:
            return "Some issue "
    else:
        return render_template('add_category.html')








