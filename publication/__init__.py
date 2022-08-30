from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bappeda.db'
app.config['SECRET_KEY'] = 'my-super-secret-key'

login_manager.login_view = 'login_page'
login_manager.login_message = 'Harap Login Dulu'
login_manager.login_message_category = 'warning'

from publication import routes
from publication.setda import routes_setda
from publication.dprd import routes_dprd
from publication.inspektorat import routes_inspektorat
from publication.pendidikan import routes_pendidikan
from publication.dinkes import routes_dinkes
from publication.anutapura import routes_anutapura
from publication.pu import routes_pu
from publication.pertanahan import routes_pertanahan
from publication.pemukiman import routes_pemukiman
from publication.satpol import routes_satpol
from publication.pemadam import routes_pemadam
from publication.sosial import routes_sosial
# umkm
from publication.umkm import routes_umkm
from publication.perdagangan import routes_perdagangan
from publication.dukcapil import routes_dukcapil
# ketahanan pangan
from publication.pangan import routes_pangan
from publication.kearsipan import routes_kearsipan
from publication.dispora import routes_dispora
from publication.pppa import routes_pppa
from publication.ppkb import routes_ppkb
from publication.lingkungan import routes_lingkungan
from publication.modal import routes_modal
from publication.pariwisata import routes_pariwisata
from publication.dishub import routes_dishub
from publication.kominfo import routes_kominfo
from publication.bappeda import routes_bappeda
from publication.kepegawaian import routes_kepegawaian
from publication.aset import routes_aset
from publication.pendapatan import routes_pendapatan
from publication.penelitian import routes_penelitian
from publication.kesatuan import routes_kesatuan
from publication.bencana import routes_bencana
from publication.kawasan import routes_kawasan

# pendapatan daerah
# penelitian dan pengembangan
# badan kesatuan bangsa dan politik
# badan penanggulangan bencana daerah
# administarator kawasan ekonomi khusus

