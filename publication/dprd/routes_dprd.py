from publication import app, db
from publication.models import Districts, Dprd
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormDprd
from flask_login import current_user, login_required

# ------------------------------------  ( DPRD ) --------------------------------------------
# dprd (Kota)
@app.route('/publikasi/dprd')
def dprd():
  data = Dprd.query.filter_by(district_id=None).order_by(Dprd.tahun).all()
  return render_template('dprd/dprd.html', data=data)

# dprd (Kecamatan)
@app.route('/publikasi/dprd/<int:district_id>')
def dprd_kec(district_id):
  data = Dprd.query.filter_by(district_id=district_id).order_by(Dprd.tahun).all()
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('dprd/dprd_kec.html', data=data, district_id=district_id, district_name=district_name)

# edit tabel
@app.route('/publikasi/dprd/add', methods=['GET', 'POST'])
@login_required
def dprd_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 2:
    form = FormDprd()
    if form.validate_on_submit():
      if form.district_id.data == 'None':
        form.district_id.data = eval(form.district_id.data)
      else:
        form.district_id.data = int(form.district_id.data)
      rows_to_create = Dprd(tahun=form.tahun.data,
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
                              district_id=form.district_id.data
                            )
      db.session.add(rows_to_create)
      db.session.commit()
      flash('Table Edited!', category='success')
      return redirect(url_for('dprd'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('dprd/dprd_add.html', form=form)

# hapus record
@app.route('/publikasi/dprd/delete/<int:id>')
@login_required
def dprd_delete(id):
  row_to_delete = Dprd.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 2 or current_user.officer_of_agency == None:
    db.session.delete(row_to_delete)
    db.session.commit()
    flash('Data Berhasil Dihapus', category='success')
    return redirect(url_for('dprd'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('dprd'))