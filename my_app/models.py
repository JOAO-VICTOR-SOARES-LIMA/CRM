from django.db import models
import uuid

class Oportcontract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)

class Oportunitychance (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=50)
    factor = models.IntegerField()

class Oportloss(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=50)

class Oportstage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=50)
    factor = models.IntegerField()

class Bu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    bu_name = models.TextField(max_length=200)
    bu_cod = models.TextField(max_length=20)
    bu_linkfolder = models.TextField(max_length=200)
    
class Customersegment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=200, unique=True)

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    companyname = models.TextField(max_length=200, unique=True)
    name = models.TextField(max_length=200, unique=True)
    teamsname = models.TextField(max_length=200, unique=True)
    cnpj = models.TextField(max_length=20, unique=True)
    ie = models.TextField(max_length=20, null=True, unique=True)
    province = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    country = models.CharField(max_length=20)
    zipcoud = models.TextField(max_length=20)
    site = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    fk_customer_segment_id = models.ForeignKey(Customersegment, on_delete=models.CASCADE, to_field='id' ) 

class Departament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=200, unique=True)

class Teammember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50, unique=True)
    position = models.TextField(max_length=50)

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=100, unique=True)
    phone = models.TextField(max_length=50)
    celphone = models.TextField(max_length=50)
    fk_contact_customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id' ) 
    fk_contact_departament_id = models.ForeignKey(Departament, on_delete=models.CASCADE, to_field='id' ) 
    fk_contact_teammember = models.ForeignKey(Teammember, on_delete=models.CASCADE, to_field='id' ) 

class Lead(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    estimatedprice = models.FloatField()
    name = models.TextField(max_length=200)
    description = models.TextField()
    duedate = models.DateField()
    created = models.DateField()
    createdby = models.IntegerField()
    fk_lead_contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE, to_field='id' ) 

class Oporestimator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    fk_oporestimator_teammember= models.ForeignKey(Teammember, on_delete=models.CASCADE, to_field='id' ) 

class Oportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    uid = models.IntegerField(unique=True)
    cod = models.TextField(max_length=20, default='default_value')
    name = models.TextField(max_length=200)
    mustwin = models.BooleanField(null=True)
    estimatedagreement = models.DateField()
    serviceprice = models.FloatField()
    materialprice = models.FloatField()
    softwareprice = models.FloatField()
    expenseprice = models.FloatField()
    taxes = models.FloatField()
    totalprice = models.FloatField()
    potentialprice = models.FloatField()
    extrascope = models.BooleanField()
    linkfolder = models.TextField(max_length=200, unique=True, null=True)
    finisheddate = models.DateField(null=True)
    finishedprice = models.FloatField(null=True)
    supplyregister = models.CharField(max_length=50, null=True)
    fk_oportunity_bu_id = models.ForeignKey(Bu, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_oporstage_id = models.ForeignKey(Oportstage, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_oporchance_id = models.ForeignKey(Oportunitychance, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_oporloss_id = models.ForeignKey(Oportloss, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE ,to_field='id')
    fk_oportunity_oporestimator_id = models.ForeignKey(Oporestimator, on_delete=models.CASCADE ,to_field='id', null=True)
    fk_oportunity_oporcontract_id = models.ForeignKey(Oportcontract, on_delete=models.CASCADE ,to_field='id', null=True)
    fk_oportunity_lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE ,to_field='id', null=True)
    def __str__(self):
        return self.name
    

class Pm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    fk_pm_teammember_id = models.ForeignKey(Teammember, on_delete=models.CASCADE ,to_field='id')

class Timelife(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    description = models.TextField()
    date = models.DateField()
    fk_timelife_oportunity_id = models.ForeignKey(Oportunity, on_delete=models.CASCADE, to_field='id' )

class Followup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    duedate = models.DateField()
    objective = models.TextField()
    date = models.DateField()
    report = models.TextField()
    fk_followup_oportunity_id = models.ForeignKey(Oportunity, on_delete=models.CASCADE, to_field='id' ) 

class OPortags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.TextField(max_length=200)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    cod = models.TextField(max_length=20, unique=True)
    desc = models.TextField(max_length=200)
    start = models.DateField()
    finish = models.DateField()
    contract = models.CharField(max_length=200)
    constcenter = models.BooleanField()
    linkfoldermanagement = models.TextField(max_length=200)
    linkfoldertech = models.TextField(max_length=200)
    linkfolderbackup = models.TextField(max_length=200)
    fk_project_customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id' ) 
    fk_project_bu_id = models.ForeignKey(Bu, on_delete=models.CASCADE, to_field='id' ) 
    fk_project_pm_id = models.ForeignKey(Pm, on_delete=models.CASCADE, to_field='id' ) 

class Purchaseorder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    cod = models.TextField(max_length=20)
    name = models.TextField(max_length=50)
    iss = models.FloatField()
    icms = models.FloatField()
    ipi = models.FloatField()
    pis = models.FloatField()
    confins = models.FloatField()
    totalservice = models.FloatField()
    totalproduct = models.FloatField()
    totalexpense = models.FloatField()
    totalsoftware = models.FloatField()
    linkfolder = models.TextField(max_length=200)
    fk_purchaseorder_oportunity_id = models.ForeignKey(Oportunity, on_delete=models.CASCADE, to_field='id' ) 
    fk_purchaseorder_project_id = models.ForeignKey(Project, on_delete=models.CASCADE, to_field='id' ) 











