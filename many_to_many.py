# I wrote a many to many relationship model in Python with the sqlite3 module.
# the connection references a schema.sql file for constructing the rows
# the approach I took with this many to many relationship utilizes only two
# tables, and never creates a third in the middle with the common connections



import sqlite3

conn = sqlite3.connect('schema.db')
c = conn.cursor()

def add_patient():
    pat = raw_input('Patient Name: ')
    pat_stuff = [i for i in c.execute("select * from patients")]
    cur_pats = [i[1] for i in pat_stuff]
    ids = [i[0] for i in pat_stuff]
    id_n = 0
    if len(ids) > 0:
        id_n = max(ids) + 1
    if pat not in cur_pats:
        c.execute("insert into patients (id, patient_id, doctors) values (?, ?, ?)", (id_n, pat, ''))
        conn.commit()
        print "Patient added to the database."
    else:
        print "Error, the patient you entered is already in the database."



def add_doctor():
    doc = raw_input('Doctor Name: ')
    doc_stuff = [i for i in c.execute("select * from doctors")]
    cur_docs = [i[1] for i in doc_stuff]
    ids = [i[0] for i in doc_stuff]
    id_n = 0
    if len(ids) > 0:
        id_n = max(ids) + 1
    if doc not in cur_docs:
        c.execute("insert into doctors (id, doctor_id, patients) values (?, ?, ?)", (id_n, doc, ''))
        conn.commit()
        print "Doctor added to the database."
    else:
        print "Error, the doctor you entered is already in the database."


def patient_hire_doc():
    pat = raw_input('Patient Name: ')
    doc = raw_input('Doctor to hire: ')
    pat_stuff = [i for i in c.execute("select * from patients where patient_id=?", (pat,))]
    doc_stuff = [i for i in c.execute("select * from doctors where doctor_id=?", (doc,))]
    pat_doc_str = str(pat_stuff[0][2])
    doc_id_str = str(doc_stuff[0][0])
    if pat_doc_str.find(doc_id_str) >= 0:
        print doc, " was already a doctor of ", pat
    else:
        pat_doc_str += doc_id_str
        c.execute("update patients set doctors = ? where patient_id = ?", (pat_doc_str, pat))
        conn.commit()
        print "Doctor hired."

def doctor_treat_patient():
    doc = raw_input('Doctor Name: ')
    pat = raw_input('Patient to treat: ')
    doc_stuff = [i for i in c.execute("select * from doctors where doctor_id=?", (doc,))]
    pat_stuff = [i for i in c.execute("select * from patients where patient_id=?", (pat,))]
    doc_pat_str = str(doc_stuff[0][2])
    pat_id_str = str(pat_stuff[0][0])
    if doc_pat_str.find(pat_id_str) >= 0:
        print pat, " was already a patient of ", doc
    else:
        doc_pat_str += pat_id_str
        c.execute("update doctors set patients = ? where doctor_id = ?",(doc_pat_str, doc))
        conn.commit()
        print doc, " has begun treatment for ", pat


def get_patient_doctors():
    pat = raw_input('Patient name: ')
    pat_stuff = [i for i in c.execute("select * from patients where patients.patient_id = ?", (pat,))]
    doc_ids = str(pat_stuff[0][2])
    doctors_ids = [i for i in doc_ids]
    docs = []
    for i in doctors_ids:
        x = c.execute("select doctor_id from doctors where doctors.id =?", (i,))
        for e in x:
                    docs.append(e)
    for doc in docs:
        print doc


def get_doctor__patients():
    doc = raw_stuff('Doctor name: ')
    pat_stuff = [i for i in c.execute("select * from doctors where doctors.doctor_id = ?", (doc,))]
    pat_ids = str(pat_stuff[0][2])
    patient_ids = [i for i in pat_ids]
    pats = []
    for i in patient_ids:
        x = c.execute("select patient_id from patients where patient.id = ?", (i,))
        for e in x:
                pats.append(e)
    for pat in pats:
        print pat


def main():
    operation = raw_input('<ap = add_patient, ad = add doctor, ph = patient hire doc, dt = doctor treat patient, gpd = get patient doctors, gdp = get doctor patients>: ')
    if operation.lower() == 'ap':
        return add_patient()
    elif operation.lower() == 'ad':
        return add_doctor()
    elif operation.lower() == 'ph':
        return patient_hire_doc()
    elif operation.lower() == 'dt':
        return doctor_treat_patient()
    elif operation.lower() == 'gpd':
        return get_patient_doctors()
    elif operation.lower() == 'gdp':
        return get_doctor_patients()
    else:
        return "Takes as input ap, ad, ph, dt, gpd, or gdp only."

if __name__ == '__main__':
    main()

