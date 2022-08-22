from publication import app, db
from publication.models import Districts, Pertanahan
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormPertanahan
from flask_login import current_user, login_required

# ------------------------------------  ( Penataan Ruang dan Pertanahan ) --------------------------------------------
# pertanahan (Kota)
@app.route('/publikasi/pertanahan')
def pertanahan():
  data = Pertanahan.query.filter_by(district_id=None).order_by(Pertanahan.tahun).all()
  return render_template('pertanahan/pertanahan.html', data=data)

# pertanahan (Kecamatan)
@app.route('/publikasi/pertanahan/<int:district_id>')
def pertanahan_kec(district_id):
  data = Pertanahan.query.filter_by(district_id=district_id).order_by( Pertanahan.tahun).all()
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('pertanahan/pertanahan_kec.html', data=data, district_id=district_id, district_name=district_name)

# edit tabel
@app.route('/publikasi/pertanahan/add', methods=['GET', 'POST'])
@login_required
def pertanahan_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 8:
    form = FormPertanahan()
    if form.validate_on_submit():
      if form.district_id.data == 'None':
        form.district_id.data = eval(form.district_id.data)
      else:
        form.district_id.data = int(form.district_id.data)
      rows_to_create = Pertanahan(tahun=form.tahun.data,
                              u1=form.u1.data,
                              u2=form.u2.data,
                              u3=form.u3.data,
                              u4=form.u4.data,
                              u5=form.u5.data,
                              u6=form.u6.data,
                              u7=form.u7.data,
                              u8=form.u8.data,
                              u9=form.u9.data,
                              u10=form.u10.data,
                              u11=form.u11.data,
                              u12=form.u12.data,
                              u13=form.u13.data,
                              u14=form.u14.data,
                              u15=form.u15.data,
                              u16=form.u16.data,
                              u17=form.u17.data,
                              u18=form.u18.data,
                              u19=form.u19.data,
                              u20=form.u20.data,
                              u21=form.u21.data,
                              u22=form.u22.data,
                              u23=form.u23.data,
                              u24=form.u24.data,
                              u25=form.u25.data,
                              u26=form.u26.data,
                              u27=form.u27.data,
                              u28=form.u28.data,
                              u29=form.u29.data,
                              u30=form.u30.data,
                              u31=form.u31.data,
                              u32=form.u32.data,
                              u33=form.u33.data,
                              u34=form.u34.data,
                              u35=form.u35.data,
                              u36=form.u36.data,
                              u37=form.u37.data,
                              u38=form.u38.data,
                              u39=form.u39.data,
                              u40=form.u40.data,
                              u41=form.u41.data,
                              u42=form.u42.data,
                              u43=form.u43.data,
                              u44=form.u44.data,
                              u45=form.u45.data,
                              u46=form.u46.data,
                              u47=form.u47.data,
                              u48=form.u48.data,
                              u49=form.u49.data,
                              u50=form.u50.data,
                              u51=form.u51.data,
                              u52=form.u52.data,
                              u53=form.u53.data,
                              u54=form.u54.data,
                              u55=form.u55.data,
                              u56=form.u56.data,
                              u57=form.u57.data,
                              u58=form.u58.data,
                              u59=form.u59.data,
                              u60=form.u60.data,
                              u61=form.u61.data,
                              u62=form.u62.data,
                              u63=form.u63.data,
                              u64=form.u64.data,
                              u65=form.u65.data,
                              u66=form.u66.data,
                              u67=form.u67.data,
                              u68=form.u68.data,
                              u69=form.u69.data,
                              u70=form.u70.data,
                              u71=form.u71.data,
                              u72=form.u72.data,
                              u73=form.u73.data,
                              u74=form.u74.data,
                              u75=form.u75.data,
                              u76=form.u76.data,
                              u77=form.u77.data,
                              u78=form.u78.data,
                              u79=form.u79.data,
                              u80=form.u80.data,
                              u81=form.u81.data,
                              u82=form.u82.data,
                              u83=form.u83.data,
                              u84=form.u84.data,
                              u85=form.u85.data,
                              u86=form.u86.data,
                              u87=form.u87.data,
                              u88=form.u88.data,
                              u89=form.u89.data,
                              u90=form.u90.data,
                              u91=form.u91.data,
                              u92=form.u92.data,
                              u93=form.u93.data,
                              u94=form.u94.data,
                              u95=form.u95.data,
                              u96=form.u96.data,


                              district_id=form.district_id.data
                            )
      db.session.add(rows_to_create)
      db.session.commit()
      flash('Table Edited!', category='success')
      return redirect(url_for('pertanahan'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('pertanahan/pertanahan_add.html', form=form)

# hapus record
@app.route('/publikasi/pertanahan/delete/<int:id>')
@login_required
def pertanahan_delete(id):
  row_to_delete = Pertanahan.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 8 or current_user.officer_of_agency == None:
    db.session.delete(row_to_delete)
    db.session.commit()
    flash('Data Berhasil Dihapus', category='success')
    return redirect(url_for('pertanahan'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('pertanahan'))