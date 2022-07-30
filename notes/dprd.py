# from publication import db

# class DPRD(db.Model):
#   id = db.Column(db.Integer(), primary_key=True)
#   tahun = db.Column(db.String(length=4), nullable=False)
#   tersedia_alat_kelengkapan = db.Column(db.Integer(), nullable=True)
#   tersusun_terintegrasi = db.Column(db.Integer(), nullable=True)
#   terintegrasi = db.Column(db.Integer(), nullable=True)
#   j_fraksi_dprd = db.Column(db.Integer(), nullable=True)
#   j_keputusan_dprd = db.Column(db.Integer(), nullable=True)
#   peraturan_daerah = db.Column(db.Integer(), nullable=True)
#   keputusan_dprd = db.Column(db.Integer(), nullable=True)
#   nota = db.Column(db.Integer(), nullable=True)
#   keputusan_pimpinan_dewan = db.Column(db.Integer(), nullable=True)
#   musyawarah = db.Column(db.Integer(), nullable=True)
#   memorandum = db.Column(db.Integer(), nullable=True)
#   panitia_anggaran = db.Column(db.Integer(), nullable=True)
#   komposisi_dprd = db.Column(db.Integer(), nullable=True)
#   # 13
#   golkar_lk = db.Column(db.Integer(), nullable=True)
#   golkar_pr = db.Column(db.Integer(), nullable=True)
#   # 14
#   demokrat_lk = db.Column(db.Integer(), nullable=True)
#   demokrat_pr = db.Column(db.Integer(), nullable=True)
#   # 15
#   pks_lk = db.Column(db.Integer(), nullable=True)
#   pks_pr = db.Column(db.Integer(), nullable=True)
#   # 16
#   gerindra_lk = db.Column(db.Integer(), nullable=True)
#   gerindra_pr = db.Column(db.Integer(), nullable=True)
#   # 17
#   hanura_lk = db.Column(db.Integer(), nullable=True)
#   hanura_pr = db.Column(db.Integer(), nullable=True)
#   # 18
#   nasdem_lk = db.Column(db.Integer(), nullable=True)
#   nasdem_pr = db.Column(db.Integer(), nullable=True)
#   # 19
#   dip_lk = db.Column(db.Integer(), nullable=True)
#   dip_pr = db.Column(db.Integer(), nullable=True)
#   # 20
#   pkb_lk = db.Column(db.Integer(), nullable=True)
#   pkb_pr = db.Column(db.Integer(), nullable=True)
#   # 21
#   ai_lk = db.Column(db.Integer(), nullable=True)
#   ai_pr = db.Column(db.Integer(), nullable=True)
#   # Bidang Pemerintahan
#   # 22
#   pemerintahan_lk = db.Column(db.Integer(), nullable=True)
#   pemerintahan_pr = db.Column(db.Integer(), nullable=True)
#   # 23
#   ekonomi_lk = db.Column(db.Integer(), nullable=True)
#   ekonomi_pr = db.Column(db.Integer(), nullable=True)
#   # 24
#   pembangunan_lk = db.Column(db.Integer(), nullable=True)
#   pembangunan_pr = db.Column(db.Integer(), nullable=True)
#   # Kepanitiaan
#   # 25
#   musyawarah_lk = db.Column(db.Integer(), nullable=True)
#   musyawarah_pr = db.Column(db.Integer(), nullable=True)
#   # 26
#   anggaran_lk = db.Column(db.Integer(), nullable=True)
#   anggaran_pr = db.Column(db.Integer(), nullable=True)
#   # 27
#   kehormatan_lk = db.Column(db.Integer(), nullable=True)
#   kehormatan_pr = db.Column(db.Integer(), nullable=True)
#   # 28
#   legislasi_lk = db.Column(db.Integer(), nullable=True)
#   legislasi_pr = db.Column(db.Integer(), nullable=True)
#   # ---
#   district_id = db.Column(db.Integer(), nullable=True)
