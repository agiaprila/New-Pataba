from publication import app, db
from publication.models import Districts, Setda
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormSetda
from flask_login import current_user, login_required

# ------------------------------------  ( SETDA ) --------------------------------------------
# sekda (Kota)
@app.route('/publikasi/setda')
def setda():
  data = Setda.query.filter_by(district_id=None).order_by(Setda.tahun).all()
  return render_template('setda/setda.html', data=data)

# sekda (Kecamatan)
@app.route('/publikasi/setda/<int:district_id>')
def setda_kec(district_id):
  data = Setda.query.filter_by(district_id=district_id).order_by(Setda.tahun).all()
  # id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  # return render_template('setda/setda_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)
  return render_template('setda/setda_kec.html', data=data, district_id=district_id, district_name=district_name)

# edit tabel
@app.route('/publikasi/setda/add', methods=['GET', 'POST'])
@login_required
def setda_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 1:
    form = FormSetda()
    if form.validate_on_submit():
      if form.district_id.data == 'None':
        form.district_id.data = eval(form.district_id.data)
      else:
        form.district_id.data = int(form.district_id.data)
#      if current_user.role == 'admin' or current_user.officer_of_district == form.district_id.data:
      rows_to_create = Setda(tahun=form.tahun.data,
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
                              u141=form.u141.data,
                              u142=form.u142.data,
                              u143=form.u143.data,
                              u144=form.u144.data,
                              u145=form.u145.data,
                              u146=form.u146.data,
                              u147=form.u147.data,
                              u148=form.u148.data,
                              u149=form.u149.data,
                              u150=form.u150.data,
                              u151=form.u151.data,
                              u152=form.u152.data,
                              u153=form.u153.data,
                              u154=form.u154.data,
                              u155=form.u155.data,
                              u156=form.u156.data,
                              u157=form.u157.data,
                              u158=form.u158.data,
                              u159=form.u159.data,
                              u160=form.u160.data,
                              u161=form.u161.data,
                              u162=form.u162.data,
                              u163=form.u163.data,
                              u164=form.u164.data,
                              u165=form.u165.data,
                              u166=form.u166.data,
                              u167=form.u167.data,
                              u168=form.u168.data,
                              u169=form.u169.data,
                              u170=form.u170.data,
                              u171=form.u171.data,
                              u172=form.u172.data,
                              u173=form.u173.data,
                              u174=form.u174.data,
                              u175=form.u175.data,
                              u176=form.u176.data,
                              u177=form.u177.data,
                              u178=form.u178.data,
                              u179=form.u179.data,
                              u180=form.u180.data,
                              u181=form.u181.data,
                              u182=form.u182.data,
                              u183=form.u183.data,
                              u184=form.u184.data,
                              u185=form.u185.data,
                              u186=form.u186.data,
                              u187=form.u187.data,
                              u188=form.u188.data,
                              u189=form.u189.data,
                              u190=form.u190.data,
                              u191=form.u191.data,
                              u192=form.u192.data,
                              u193=form.u193.data,
                              u194=form.u194.data,
                              u195=form.u195.data,
                              u196=form.u196.data,
                              u197=form.u197.data,
                              u198=form.u198.data,
                              u199=form.u199.data,
                              u200=form.u200.data,
                              u201=form.u201.data,
                              u202=form.u202.data,
                              u203=form.u203.data,
                              u204=form.u204.data,
                              u205=form.u205.data,
                              u206=form.u206.data,
                              u207=form.u207.data,
                              u208=form.u208.data,
                              u209=form.u209.data,
                              u210=form.u210.data,
                              u211=form.u211.data,
                              u212=form.u212.data,
                              u213=form.u213.data,
                              u214=form.u214.data,
                              u215=form.u215.data,
                              u216=form.u216.data,
                              u217=form.u217.data,
                              u218=form.u218.data,
                              u219=form.u219.data,
                              u220=form.u220.data,
                              u221=form.u221.data,
                              u222=form.u222.data,
                              u223=form.u223.data,
                              u224=form.u224.data,
                              u225=form.u225.data,
                              u226=form.u226.data,
                              u227=form.u227.data,
                              u228=form.u228.data,
                              u229=form.u229.data,
                              u230=form.u230.data,
                              u231=form.u231.data,
                              u232=form.u232.data,
                              u233=form.u233.data,
                              u234=form.u234.data,
                              u235=form.u235.data,
                              u236=form.u236.data,
                              district_id=form.district_id.data
                            )
      print("tambahkan data selesai")
      db.session.add(rows_to_create)
      print("tambahkan data selesai 2")
      db.session.commit()
      print("commit selesai")
      flash('Table Edited!', category='success')
      return redirect(url_for('setda'))
      # else:  
      #   flash('Unauthorized', category='danger')
      #   return redirect(url_for('setda_add'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('setda/setda_add.html', form=form)

# hapus record
@app.route('/publikasi/setda/delete/<int:id>')
@login_required
def setda_delete(id):
  row_to_delete = Setda.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 1:
#    if current_user.role == 'admin' or current_user.officer_of_district == row_to_delete.district_id:
    db.session.delete(row_to_delete)
    db.session.commit()
    flash('Data Berhasil Dihapus', category='success')
    return redirect(url_for('setda'))
    # else:
    #   flash('Unauthorized', category='danger')
    #   return redirect(url_for('setda'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('setda'))

