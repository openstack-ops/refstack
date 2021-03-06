#!/usr/bin/env python
#
# Copyright (c) 2013 Piston Cloud Computing, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import os
from flask import Flask, session



#db_path = os.path.abspath(
#    os.path.join(os.path.basename(__file__), "../"))

db_path = 'tmp'

app = Flask(__name__)

app.config['MAILGUN_KEY'] = '#@#@#@#@'
app.config['MAILGUN_DOMAIN'] = 'refstack.org'
app.config['SECRET_KEY'] = '#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///%s/refstack.db' % (db_path))
app.config['DEBUG'] = True
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']
app.config['SECURITY_POST_LOGIN_VIEW'] = 'dashboard'
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_EMAIL_SENDER'] = "refstack.org"
app.config['MAIL_SERVER'] = 'smtp.refstack.org'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'postmaster@refstack.org'
app.config['MAIL_PASSWORD'] = '1234'
