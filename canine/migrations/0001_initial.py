# Generated by Django 4.2.1 on 2023-08-05 12:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'AdminHOD'), (2, 'Pharmacist'), (3, 'Doctor'), (4, 'Clerk'), (5, 'Handler'), (6, 'Incharge')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='admin.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_employed', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ControlledTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlled', models.CharField(blank=True, max_length=30, null=True, verbose_name='Controlled Training')),
                ('false_run', models.CharField(blank=True, max_length=30, null=True, verbose_name='False Run')),
                ('attack', models.CharField(blank=True, max_length=30, null=True, verbose_name='Attack')),
                ('search_and_attack', models.CharField(blank=True, max_length=30, null=True, verbose_name='Search and Attack')),
                ('standoff', models.CharField(blank=True, max_length=30, null=True, verbose_name='Stand Off')),
                ('effort', models.CharField(blank=True, max_length=30, null=True, verbose_name='Effort')),
                ('daily_training_rating', models.CharField(blank=True, choices=[('Satisfactory', 'Satisfactory'), ('Unsatisfactory', 'Unsatisfactory')], max_length=30, null=True, verbose_name='Daily Training Rating')),
                ('date', models.DateTimeField(null=True)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.IntegerField(blank=True, null=True, verbose_name='Course Code')),
                ('course_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Course Name')),
                ('location', models.CharField(blank=True, max_length=30, null=True, verbose_name='Location')),
                ('course_start_date', models.DateField(auto_now=True)),
                ('course_completion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deworming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name of Deworming')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='doctor.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('dog_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dog Name')),
                ('dog_color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Colour')),
                ('svc_age', models.IntegerField(blank=True, null=True, verbose_name='Service Age')),
                ('svc_no', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Service Number')),
                ('reorder_level', models.IntegerField(blank=True, null=True, verbose_name='Kennel Number')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('valid_from', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('dog_description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Dog Description')),
                ('dog_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='', verbose_name='Canine Dog Image')),
                ('emp_id', models.CharField(default='773', max_length=70, verbose_name='Service Number')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcode')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.category', verbose_name='Breed')),
                ('dog_imprint', models.ForeignKey(blank=True, max_length=45, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.classification', verbose_name='Classification')),
            ],
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='patient.jpg', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=10, null=True)),
                ('date_admitted', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('dog_picture', models.ImageField(upload_to='')),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=45, null=True, verbose_name='Address ')),
                ('tele_phone', models.IntegerField(blank=True, null=True, verbose_name='Telephone Number')),
                ('title', models.CharField(blank=True, max_length=45, null=True, verbose_name='Title')),
                ('foreman', models.CharField(blank=True, max_length=45, null=True, verbose_name='Foreman')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Type of Vaccination')),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Type of Vaccination')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.CharField(blank=True, max_length=30, null=True, verbose_name='Utilization Training')),
                ('building', models.CharField(blank=True, max_length=30, null=True, verbose_name='Building Search')),
                ('gunfire_handler', models.CharField(blank=True, max_length=30, null=True, verbose_name='Gunfire Handler')),
                ('gunfire_decoy', models.CharField(blank=True, max_length=30, null=True, verbose_name='Gunfire Decoy')),
                ('tracking', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tracking')),
                ('daily_training_rating', models.CharField(blank=True, choices=[('Satisfactory', 'Satisfactory'), ('Unsatisfactory', 'Unsatisfactory')], max_length=30, null=True, verbose_name='Daily Training Rating')),
                ('date', models.DateTimeField(null=True)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
                ('dog', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vaccine Name')),
                ('manufacture', models.CharField(blank=True, max_length=30, null=True, verbose_name='Manufacturer')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('valid_from', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('receive_quantity', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('drug_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='', verbose_name='Drug Image')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('batch_no', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vaccine Batch Number')),
                ('reorder_level', models.IntegerField(blank=True, null=True, verbose_name='Add Reorder Level Number')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.vaccinationcategory', verbose_name='Vaccine Category')),
            ],
        ),
        migrations.CreateModel(
            name='Utilization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilization', models.CharField(blank=True, max_length=30, null=True, verbose_name='Utilization Training')),
                ('combat_support', models.CharField(blank=True, max_length=30, null=True, verbose_name='Combat Support Operations')),
                ('patrol_law_enforcement', models.CharField(blank=True, max_length=30, null=True, verbose_name='Patrol law Enforcement')),
                ('patrol_security', models.CharField(blank=True, max_length=30, null=True, verbose_name='Patrol Security')),
                ('daily_training_ratings', models.CharField(blank=True, choices=[('Satisfactory', 'Satisfactory'), ('Unsatisfactory', 'Unsatisfactory')], max_length=30, null=True, verbose_name='Daily Training Rating')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
                ('dog', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog', verbose_name='Dog Name')),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_deworming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.CharField(blank=True, max_length=30, null=True, verbose_name='Product Name')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Amount')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('valid_to', models.DateField(null=True)),
                ('dog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog', verbose_name='Canine Dog')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.deworming', verbose_name='Type of Deworming')),
            ],
        ),
        migrations.CreateModel(
            name='Training_day_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('num_of_activities', models.IntegerField(blank=True, null=True)),
                ('num_of_hours', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=30, null=True)),
                ('dog', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
                ('handler', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canine.handler')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_number', models.IntegerField(blank=True, null=True)),
                ('passed_out_no', models.IntegerField(blank=True, null=True)),
                ('authorized', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.doctor', verbose_name='Authorized by')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.course', verbose_name='Course Name')),
                ('dog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Name of The Dog')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.handler', verbose_name='Trainers Name')),
            ],
        ),
        migrations.CreateModel(
            name='SkillTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(blank=True, choices=[('Sniffing Test', 'Sniffing Test'), ('Sentries Test', 'Sentries Test')], max_length=50, null=True, verbose_name='Acceptance')),
                ('criteria_detail', models.CharField(blank=True, max_length=50, null=True, verbose_name='Criteria Details')),
                ('competent', models.CharField(blank=True, choices=[('Good', 'Good'), ('Very Good', 'Very Good'), ('Outstanding', 'Outstanding')], max_length=50, null=True, verbose_name='Acceptance')),
                ('comments', models.TextField(blank=True, null=True)),
                ('dog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Canine Dog')),
            ],
        ),
        migrations.CreateModel(
            name='ScoutingTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scounting', models.CharField(blank=True, max_length=30, null=True, verbose_name='Scounting Training')),
                ('scent_detection', models.CharField(blank=True, max_length=30, null=True, verbose_name='Scent Detection')),
                ('sight_detection', models.CharField(blank=True, max_length=30, null=True, verbose_name='Sight Detection')),
                ('sound_detection', models.CharField(blank=True, max_length=30, null=True, verbose_name='Sound Detection')),
                ('vehicle_patrol', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vehicle Patrol')),
                ('daily_training_rating', models.CharField(blank=True, choices=[('Satisfactory', 'Satisfactory'), ('Unsatisfactory', 'Unsatisfactory')], max_length=30, null=True, verbose_name='Daily Training Rating')),
                ('date', models.DateTimeField(null=True)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
                ('dog', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True, verbose_name='Condition of the Dog')),
                ('prescribe', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=50, null=True, verbose_name='Status')),
                ('vac_batch_no', models.IntegerField(blank=True, null=True, verbose_name='Vaccination Batch Number')),
                ('vet_remarks', models.TextField(blank=True, max_length=100, null=True, verbose_name='Veterinary Remarks')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('valid_from', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('dog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Name of The Dog')),
                ('vaccination_id', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.vaccination', verbose_name='Type of Vaccine')),
                ('veterinary_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='canine.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mwt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(blank=True, null=True)),
                ('team_specialization', models.CharField(blank=True, max_length=50, null=True)),
                ('team_leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='canine.handler')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('dog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Canine Dog')),
            ],
        ),
        migrations.CreateModel(
            name='LeashTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leash', models.CharField(blank=True, max_length=30, null=True, verbose_name='Leash Training')),
                ('onleash', models.CharField(blank=True, max_length=30, null=True, verbose_name='On leash Obedience')),
                ('offleash', models.CharField(blank=True, max_length=30, null=True, verbose_name='Off leash Obedience')),
                ('obedience_course', models.CharField(blank=True, max_length=30, null=True, verbose_name='Obedience Course')),
                ('daily_training_rating', models.CharField(blank=True, choices=[('Satisfactory', 'Satisfactory'), ('Unsatisfactory', 'Unsatisfactory')], max_length=30, null=True, verbose_name='Daily Training Rating')),
                ('date', models.DateTimeField(null=True)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
                ('dog', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.IntegerField()),
                ('inventory', models.CharField(choices=[('Expandable', 'Expandable'), ('Consumable', 'Consumable')], max_length=30)),
                ('data_received', models.DateField(auto_now_add=True)),
                ('serviceability_status', models.CharField(choices=[('Serviceable', 'Serviceable'), ('Unserviceable', 'Unserviceable')], max_length=30)),
                ('notes', models.TextField(blank=True)),
                ('assigned_to', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.handler')),
            ],
        ),
        migrations.CreateModel(
            name='Incharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='patient.jpg', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=10, null=True)),
                ('date_admitted', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HandlerScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, max_length=20, null=True, verbose_name='Handlers Remarks')),
                ('controlled', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.controlledtraining', verbose_name='Controlled Training')),
                ('dog', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog', verbose_name='Dog Name')),
                ('leash', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.leashtraining', verbose_name='Leash Training')),
                ('scounting', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.scoutingtraining', verbose_name='Scounting Training')),
                ('utilization', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.utilization', verbose_name='Dog Name')),
                ('weapon', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.weapontraining', verbose_name='Weapon Training')),
            ],
        ),
        migrations.CreateModel(
            name='HandlerFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField(null=True)),
                ('feedback_reply', models.TextField(null=True)),
                ('admin_created_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='canine.adminhod')),
                ('handler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canine.handler')),
                ('pharmacist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='canine.pharmacist')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_deployment', models.CharField(blank=True, choices=[('Within the Country', 'Within the Country'), ('Outside the Country', 'Outside the Country')], max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_of_start', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=30, null=True)),
                ('dog', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
                ('team', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.mwt')),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='manufacture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.owner', verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='dog',
            name='vetinary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.doctor', verbose_name='Veterinary'),
        ),
        migrations.CreateModel(
            name='Dispense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispense_svc_age', models.PositiveIntegerField(default='1', null=True, verbose_name='Age')),
                ('taken', models.CharField(blank=True, max_length=300, null=True)),
                ('dog_ref_no', models.CharField(blank=True, max_length=300, null=True)),
                ('instructions', models.TextField(max_length=300, null=True)),
                ('dispense_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Canine Dog')),
                ('handler_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.handler')),
            ],
        ),
        migrations.AddField(
            model_name='controlledtraining',
            name='dog',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog'),
        ),
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_number', models.IntegerField(blank=True, null=True)),
                ('certification_date', models.DateField(auto_now_add=True)),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canine.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_evaluation', models.CharField(blank=True, max_length=30, null=True)),
                ('veterinary_evaluation', models.CharField(blank=True, max_length=30, null=True)),
                ('vaccination', models.CharField(blank=True, max_length=30, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('veterinary_reccomendation', models.CharField(blank=True, max_length=30, null=True)),
                ('casting_reason', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('casting_authority', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='canine.doctor')),
                ('dog', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.DO_NOTHING, to='canine.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessor', models.CharField(max_length=50, null=True, verbose_name='Assessor')),
                ('date_of_assessment', models.DateField(auto_now=True, verbose_name='Assessment Date')),
                ('discipline_criteria', models.CharField(blank=True, max_length=50, null=True, verbose_name='Discipline Cretiria')),
                ('requirements', models.CharField(blank=True, max_length=50, null=True, verbose_name='Requirements')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('acceptance', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=50, null=True, verbose_name='Acceptance')),
                ('dog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canine.dog', verbose_name='Canine Dog')),
            ],
        ),
    ]
