from publication import app, db
from publication.models import Districts, Pariwisata
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormPariwisata
from flask_login import current_user, login_required

# ------------------------------------  ( Pariwisata ) --------------------------------------------
# pariwisata (Kota)
@app.route('/publikasi/pariwisata')
def pariwisata():
  data = Pariwisata.query.filter_by(district_id=None).order_by(Pariwisata.tahun).all()
  return render_template('pariwisata/pariwisata.html', data=data)

# pariwisata (Kecamatan)
@app.route('/publikasi/pariwisata/<int:district_id>')
def pariwisata_kec(district_id):
  data = Pariwisata.query.filter_by(district_id=district_id).order_by( Pariwisata.tahun).all()
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('pariwisata/pariwisata_kec.html', data=data, district_id=district_id, district_name=district_name)

# edit tabel
@app.route('/publikasi/pariwisata/add', methods=['GET', 'POST'])
@login_required
def pariwisata_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 23:
    form = FormPariwisata()
    if form.validate_on_submit():
      if form.district_id.data == 'None':
        form.district_id.data = eval(form.district_id.data)
      else:
        form.district_id.data = int(form.district_id.data)
      rows_to_create = Pariwisata(tahun=form.tahun.data,
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
                              u97=form.u97.data,
                              u98=form.u98.data,
                              u99=form.u99.data,
                              u100=form.u100.data,
                              u101=form.u101.data,
                              u102=form.u102.data,
                              u103=form.u103.data,
                              u104=form.u104.data,
                              u105=form.u105.data,
                              u106=form.u106.data,
                              u107=form.u107.data,
                              u108=form.u108.data,
                              u109=form.u109.data,
                              u110=form.u110.data,
                              u111=form.u111.data,
                              u112=form.u112.data,
                              u113=form.u113.data,
                              u114=form.u114.data,
                              u115=form.u115.data,
                              u116=form.u116.data,
                              u117=form.u117.data,
                              u118=form.u118.data,
                              u119=form.u119.data,
                              u120=form.u120.data,
                              u121=form.u121.data,
                              u122=form.u122.data,
                              u123=form.u123.data,
                              u124=form.u124.data,
                              u125=form.u125.data,
                              u126=form.u126.data,
                              u127=form.u127.data,
                              u128=form.u128.data,
                              u129=form.u129.data,
                              u130=form.u130.data,
                              u131=form.u131.data,
                              u132=form.u132.data,
                              u133=form.u133.data,
                              u134=form.u134.data,
                              u135=form.u135.data,
                              u136=form.u136.data,
                              u137=form.u137.data,
                              u138=form.u138.data,
                              u139=form.u139.data,
                              u140=form.u140.data,
                              district_id=form.district_id.data
                            )
      db.session.add(rows_to_create)
      db.session.commit()
      flash('Table Edited!', category='success')
      return redirect(url_for('pariwisata'))
  else:
    flash('Unauthorized! Pastikan Mengedit Dinas Sendiri.', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('pariwisata/pariwisata_add.html', form=form)

# hapus record
@app.route('/publikasi/pariwisata/delete/<int:id>')
@login_required
def pariwisata_delete(id):
  row_to_delete = Pariwisata.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 23 or current_user.officer_of_agency == None:
    db.session.delete(row_to_delete)
    db.session.commit()
    flash('Data Berhasil Dihapus', category='success')
    return redirect(url_for('pariwisata'))
  else:
    flash('Unauthorized! Pastikan Mengedit Dinas Sendiri.', category='danger')
    return redirect(url_for('pariwisata'))