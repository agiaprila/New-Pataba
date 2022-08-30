from publication import app, db
from publication.models import Districts, Dinkes
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormDinkes
from flask_login import current_user, login_required

# ------------------------------------  (   Dinkes ) --------------------------------------------
# dinkes (Kota)
@app.route('/publikasi/dinkes')
def dinkes():
  data = Dinkes.query.filter_by(district_id=None).order_by(Dinkes.tahun).all()
  return render_template('dinkes/dinkes.html', data=data)

# dinkes (Kecamatan)
@app.route('/publikasi/dinkes/<int:district_id>')
def dinkes_kec(district_id):
  data = Dinkes.query.filter_by(district_id=district_id).order_by(Dinkes.tahun).all()
  # id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  # return render_template('dinkes/dinkes_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)
  return render_template('dinkes/dinkes_kec.html', data=data, district_id=district_id, district_name=district_name)

# edit tabel
@app.route('/publikasi/dinkes/add', methods=['GET', 'POST'])
@login_required
def dinkes_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 5:
    form = FormDinkes()
    if form.validate_on_submit():
      if form.district_id.data == 'None':
        form.district_id.data = eval(form.district_id.data)
      else:
        form.district_id.data = int(form.district_id.data)
#      if current_user.role == 'admin' or current_user.officer_of_district == form.district_id.data:
      rows_to_create = Dinkes(tahun=form.tahun.data,
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
                              u229=form.229.data,
                              u230=form.u230.data,
                              u231=form.u231.data,
                              U232=form.u232.data,
                              u233=form.u233.data,
                              u234=form.u234.data,
                              u235=form.u235.data,
                              u236=form.u236.data,
                              u237=form.u237.data,
                              u238=form.u238.data,
                              u239=form.u239.data,
                              u240=form.u240.data,
                              u241=form.u241.data,
                              u242=form.u242.data,
                              u243=form.u243.data,
                              u244=form.u244.data,
                              u245=form.u245.data,
                              u246=form.u246.data,
                              u247=form.u247.data,
                              u248=form.u248.data,
                              u249=form.u249.data,
                              u250=form.u250.data,
                              u251=form.u251.data,
                              u252=form.u252.data,
                              u253=form.u253.data,
                              u254=form.u254.data,
                              u255=form.u255.data,
                              u256=form.u256.data,
                              u257=form.u257.data,
                              u258=form.u258.data,
                              u259=form.u259.data,
                              u260=form.u260.data,
                              u261=form.u261.data,
                              u262=form.u262.data,
                              u263=form.u263.data,
                              u264=form.u264.data,
                              u265=form.u265.data,
                              u266=form.u266.data,
                              u267=form.u267.data,
                              u268=form.u268.data,
                              u269=form.u269.data,
                              u270=form.u270.data,
                              u271=form.u271.data,
                              u272=form.u272.data,
                              u273=form.u273.data,
                              u274=form.u274.data,
                              u275=form.u275.data,
                              u276=form.u276.data,
                              u277=form.u277.data,
                              u278=form.u278.data,
                              u279=form.u279.data,
                              u280=form.u280.data,
                              u281=form.u281.data,
                              u282=form.u282.data,
                              u283=form.u283.data,
                              u284=form.u284.data,
                              u285=form.u285.data,
                              u286=form.u286.data,
                              u287=form.u287.data,
                              u288=form.u288.data,
                              u289=form.u289.data,
                              u290=form.u290.data,
                              u291=form.u291.data,
                              u292=form.u292.data,
                              u293=form.u293.data,
                              u294=form.u294.data,
                              u295=form.u295.data,
                              u296=form.u296.data,
                              u297=form.u297.data,
                              u298=form.u298.data,
                              u299=form.u299.data,
                              u300=form.u300.data,
                              u301=form.u301.data,
                              u302=form.u302.data,
                              u303=form.u303.data,
                              u304=form.u304.data,
                              u305=form.u305.data,
                              u306=form.u306.data,
                              u307=form.u307.data,
                              u308=form.u308.data,
                              u309=form.u309.data,
                              u310=form.u310.data,
                              u311=form.u311.data,
                              u312=form.u312.data,
                              u313=form.u313.data,
                              u314=form.u314.data,
                              u315=form.u315.data,
                              u316=form.u316.data,
                              u317=form.u317.data,
                              u318=form.u318.data,
                              u319=form.u319.data,
                              u320=form.u320.data,
                              u321=form.u321.data,
                              u322=form.u322.data,
                              u323=form.u323.data,
                              u324=form.u324.data,
                              u325=form.u325.data,
                              u326=form.u326.data,
                              u327=form.u327.data,
                              u328=form.u328.data,
                              u329=form.u329.data,
                              u330=form.u330.data,
                              u331=form.u331.data,
                              u332=form.u332.data,
                              u333=form.u333.data,
                              u334=form.u334.data,
                              u335=form.u335.data,
                              u336=form.u336.data,
                              u337=form.u337.data,
                              u338=form.u338.data,
                              u339=form.u339.data,
                              u340=form.u340.data,
                              u341=form.u341.data,
                              u342=form.u342.data,
                              u343=form.u343.data,
                              u344=form.u344.data,
                              u345=form.u345.data,
                              u346=form.u346.data,
                              u347=form.u347.data,
                              u348=form.u338.data,
                              u349=form.u339.data,
                              u350=form.u340.data,
                              u351=form.u341.data,
                              u352=form.u342.data,
                              u353=form.u343.data,
                              u354=form.u344.data,
                              u355=form.u345.data,
                              district_id=form.district_id.data
                            )
      print("tambahkan data selesai")
      db.session.add(rows_to_create)
      print("tambahkan data selesai 2")
      db.session.commit()
      print("commit selesai")
      flash('Table Edited!', category='success')
      return redirect(url_for('dinkes'))
      # else:  
      #   flash('Unauthorized', category='danger')
      #   return redirect(url_for('dinkes_add'))
  else:
    flash('Unauthorized! Pastikan Mengedit Dinas Sendiri.', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('dinkes/dinkes_add.html', form=form)

# hapus record
@app.route('/publikasi/dinkes/delete/<int:id>')
@login_required
def dinkes_delete(id):
  row_to_delete = Dinkes.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 5:
#    if current_user.role == 'admin' or current_user.officer_of_district == row_to_delete.district_id:
    db.session.delete(row_to_delete)
    db.session.commit()
    flash('Data Berhasil Dihapus', category='success')
    return redirect(url_for('dinkes'))
    # else:
    #   flash('Unauthorized', category='danger')
    #   return redirect(url_for('dukcapil'))
  else:
    flash('Unauthorized! Pastikan Mengedit Dinas Sendiri.', category='danger')
    return redirect(url_for('dinkes'))
