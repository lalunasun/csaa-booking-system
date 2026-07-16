from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSAA', '0049_alter_systemsetting_updated_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampWaiver',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('signer_name', models.CharField(max_length=100)),
                ('waiver_version', models.CharField(default='2026-summer-v1', max_length=40)),
                ('signed_time', models.DateTimeField(auto_now_add=True)),
                ('signed_ip', models.CharField(blank=True, default='', max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camp_waivers', to='CSAA.user')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_waivers', to='CSAA.child')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_waivers', to='CSAA.term')),
            ],
            options={
                'db_table': 'b_camp_waiver',
                'indexes': [models.Index(fields=['term', 'student'], name='b_camp_waiver_term_student_idx')],
                'constraints': [models.UniqueConstraint(fields=('student', 'term', 'waiver_version'), name='unique_camp_waiver_student_term_version')],
            },
        ),
    ]
