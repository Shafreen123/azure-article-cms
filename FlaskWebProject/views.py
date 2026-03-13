from datetime import datetime
6
from flask import render_template, flash, redirect, request, session, url_for
7
from werkzeug.urls import url_parse
8
from config import Config
9
from FlaskWebProject import app, db
10
from FlaskWebProject.forms import LoginForm, PostForm
11
from flask_login import current_user, login_user, logout_user, login_required
12
from FlaskWebProject.models import User, Post
13
import msal
14
import uuid
15
 
16
imageSourceUrl = 'https://'+ app.config['BLOB_ACCOUNT']  + '.blob.core.windows.net/' + app.config['BLOB_CONTAINER']  + '/'
17
 
18
@app.route('/')
19
@app.route('/home')
20
@login_required
21
def home():
22
    user = User.query.filter_by(username=current_user.username).first_or_404()
23
    posts = Post.query.all()
24
    return render_template(
25
        'index.html',
26
        title='Home Page',
27
        posts=posts
28
    )
29
 
30
@app.route('/new_post', methods=['GET', 'POST'])
31
@login_required
32
def new_post():
33
    form = PostForm(request.form)
34
    if form.validate_on_submit():
35
        post = Post()
36
        post.save_changes(form, request.files['image_path'], current_user.id, new=True)
37
        return redirect(url_for('home'))
38
    return render_template(
39
        'post.html',
40
        title='Create Post',
41
        imageSource=imageSourceUrl,
42
        form=form
43
    )
44
 
45
 
46
@app.route('/post/<int:id>', methods=['GET', 'POST'])
47
@login_required
48
def post(id):
49
    post = Post.query.get(int(id))
50
    form = PostForm(formdata=request.form, obj=post)
51
    if form.validate_on_submit():
52
        post.save_changes(form, request.files['image_path'], current_user.id)
53
        return redirect(url_for('home'))
54
    return render_template(
55
        'post.html',
56
        title='Edit Post',
57
        imageSource=imageSourceUrl,
58
        form=form
59
    )
60
 
61
@app.route('/login', methods=['GET', 'POST'])
62
def login():
63
    if current_user.is_authenticated:
64
        return redirect(url_for('home'))
65
    form = LoginForm()
66
    if form.validate_on_submit():
67
        user = User.query.filter_by(username=form.username.data).first()
68
        if user is None or not user.check_password(form.password.data):
69
            flash('Invalid username or password')
70
            return redirect(url_for('login'))
71
        login_user(user, remember=form.remember_me.data)
72
        next_page = request.args.get('next')
73
        if not next_page or url_parse(next_page).netloc != '':
74
            next_page = url_for('home')
75
        return redirect(next_page)
76
    session["state"] = str(uuid.uuid4())
77
    auth_url = _build_auth_url(scopes=Config.SCOPE, state=session["state"])
78
    return render_template('login.html', title='Sign In', form=form, auth_url=auth_url)
79
 
80
@app.route(Config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
81
def authorized():
82
    if request.args.get('state') != session.get("state"):
83
        return redirect(url_for("home"))  # No-OP. Goes back to Index page
84
    if "error" in request.args:  # Authentication/Authorization failure
85
        return render_template("auth_error.html", result=request.args)
86
    if request.args.get('code'):
87
        cache = _load_cache()
88
        # Acquire a token from a built msal app using the auth code
89
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
90
            request.args['code'],
91
            scopes=Config.SCOPE,
92
            redirect_uri=url_for('authorized', _external=True)
93
        )
94
        if "error" in result:
95
            return render_template("auth_error.html", result=result)
96
        session["user"] = result.get("id_token_claims")
97
        # Note: In a real app, we'd use the 'name' property from session["user"] below
98
        # Here, we'll use the admin username for anyone who is authenticated by MS
99
        user = User.query.filter_by(username="admin").first()
100
        login_user(user)
101
        _save_cache(cache)
102
    return redirect(url_for('home'))
103
 
104
@app.route('/logout')
105
def logout():
106
    logout_user()
107
    if session.get("user"): # Used MS Login
108
        # Wipe out user and its token cache from session
109
        session.clear()
110
        # Also logout from your tenant's web session
111
        return redirect(
112
            Config.AUTHORITY + "/oauth2/v2.0/logout" +
113
            "?post_logout_redirect_uri=" + url_for("login", _external=True))
114
 
115
    return redirect(url_for('login'))
116
 
117
def _load_cache():
118
    # Load the token cache from the session if it exists
119
    cache = msal.SerializableTokenCache()
120
    if session.get("token_cache"):
121
        cache.deserialize(session["token_cache"])
122
    return cache
123
 
124
def _save_cache(cache):
125
    # Save the token cache back to the session if it has changed
126
    if cache.has_state_changed:
127
        session["token_cache"] = cache.serialize()
128
 
129
def _build_msal_app(cache=None, authority=None):
130
    # Return a ConfidentialClientApplication using app config
131
    return msal.ConfidentialClientApplication(
132
        Config.CLIENT_ID,
133
        authority=authority or Config.AUTHORITY,
134
        client_credential=Config.CLIENT_SECRET,
135
        token_cache=cache
136
    )
137
 
138
def _build_auth_url(authority=None, scopes=None, state=None):
139
    # Return the full Auth Request URL with appropriate Redirect URI
140
    return _build_msal_app(authority=authority).get_authorization_request_url(
141
        scopes or [],
142
        state=state or str(uuid.uuid4()),
143
        redirect_uri=url_for('authorized', _external=True)
144
)
