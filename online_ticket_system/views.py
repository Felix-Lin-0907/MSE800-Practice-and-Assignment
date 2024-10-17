from flask import render_template, session, request
from models import User, Concert

# 首页路由
def home():
    print(f"Session contains: {session}")
    return render_template('index.html')

def concerts():
    page = request.args.get('page', 1, type=int)
    per_page = 8  # 每页显示 20 条记录
    pagination = Concert.query.paginate(page=page, per_page=per_page)

    concerts = pagination.items
    return render_template('concerts.html', concerts=concerts, pagination=pagination)