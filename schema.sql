
drop table if exists patients;
drop table if exists doctors;

create table patients ( id integer primary key autoincrement,
    patient_id string,
    doctors string
);

create table doctors ( id integer primary key autoincrement,
    doctor_id string,
    patients string
);
