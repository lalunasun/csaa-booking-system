from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSAA', '0046_classpass_classpassbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampAttendance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateField()),
                ('status', models.CharField(choices=[('not_arrived', 'Not arrived'), ('signed_in', 'Signed in'), ('late', 'Late'), ('signed_out', 'Signed out'), ('early_pickup', 'Early pickup'), ('absent', 'Absent')], default='not_arrived', max_length=20)),
                ('sign_in_time', models.DateTimeField(blank=True, null=True)),
                ('sign_out_time', models.DateTimeField(blank=True, null=True)),
                ('sign_in_ip', models.CharField(blank=True, default='', max_length=100)),
                ('sign_out_ip', models.CharField(blank=True, default='', max_length=100)),
                ('note', models.TextField(blank=True, default='', max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camp_attendance_records', to='CSAA.tag')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_attendance_records', to='CSAA.child')),
                ('term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camp_attendance_records', to='CSAA.term')),
            ],
            options={
                'db_table': 'b_camp_attendance',
                'indexes': [models.Index(fields=['attendance_date', 'status'], name='b_camp_att_date_status_idx'), models.Index(fields=['student', 'attendance_date'], name='b_camp_att_student_date_idx')],
                'constraints': [models.UniqueConstraint(fields=('student', 'attendance_date'), name='unique_camp_attendance_student_date')],
            },
        ),
    ]
