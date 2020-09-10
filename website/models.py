from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField
# Create your models here.
  
class AboutMe(models.Model):
    mainHeading = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    text1 = models.CharField(max_length=200, null=True, blank=True)
    Birthday = models.CharField(max_length=100, null=True, blank=True)
    Website = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Age = models.CharField(max_length=100, null=True, blank=True)
    Degree = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Freelance = models.CharField(max_length=100, null=True, blank=True) 
    text2 = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title_tag= models.CharField(max_length=250,default='Web developer | Kuwait')
    def __str__(self):
        return self.mainHeading

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Me"


class Skills(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    percentage = models.CharField(max_length=100, null=True, blank=True)
    valuenow = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    sname = models.CharField(max_length=100, null=True, blank=True)
    stext = models.CharField(max_length=150, null=True, blank=True)
    icon = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.sname

class Contact(models.Model):
    c_address = models.CharField(max_length=100, null=True, blank=True)
    c_email = models.CharField(max_length=150, null=True, blank=True)
    c_phone = models.CharField(max_length=150, null=True, blank=True)

# Create your models here.
class Brand(models.Model):    
    image = models.ImageField(null=True, blank=True)
    brand_title = models.CharField(max_length=100, null=True, blank=True)
    brand_subtitle = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.brand_title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio_Brands"
 


class Photo(models.Model):     
    image = models.ImageField(null=True, blank=True)
    photo_title = models.CharField(max_length=100, null=True, blank=True)
    photo_subtitle = models.CharField(max_length=100, null=True, blank=True)
    photo_url = models.URLField(blank=True, null=True, max_length=100)
  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio_photogallery"


class Web(models.Model):
    image = models.ImageField(null=True, blank=True)
    web_title = models.CharField(max_length=100, null=True, blank=True)
    web_subtitle = models.CharField(max_length=100, null=True, blank=True)
    web_url = models.URLField(blank=True, null=True, max_length=100)
    def __str__(self):
        return self.web_subtitle

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio_website"

class Print(models.Model):     
    image = models.ImageField(null=True, blank=True)
    prints_title = models.CharField(max_length=100, null=True, blank=True)
    prints_subtitle = models.CharField(max_length=100, null=True, blank=True)
    print_url = models.URLField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.prints_subtitle

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio_Print"


class Summary(models.Model): 
    summary = models.CharField(max_length=100, null=True, blank=True)
    summary_title = models.CharField(max_length=100, null=True, blank=True)
    summary_paragraph = models.CharField(max_length=450, null=True, blank=True)
    summary_address = models.CharField(max_length=100, null=True, blank=True)
    language  = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
       return self.summary
     
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "My Summary"
	
    
class Education(models.Model):
    CATEGORY =(
        ('B.Sc. Computer Science','B.Sc. Computer Science'),
        ('Diploma in Web Designing','Diploma in Web Designing'),
        )

    UNIVERSITY =(
        ('University of Kerala','University of Kerala'),
        ('Arena Multimedia Kochi','Arena Multimedia Kochi'),
        )

    education = models.CharField(max_length=100, null=True, blank=True) 
    education_title = models.CharField(max_length=100, null=True, blank=True,choices=CATEGORY)    
    education_date = models.CharField(max_length=100, null=True, blank=True)
    education_university = models.CharField(max_length=100, null=True, blank=True ,choices=UNIVERSITY)
    education_paragraph = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
       return self.education_title
     
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "My Education"
        
class EexperienceMore(models.Model):      
    more_details1 =models.CharField(max_length=200, null=True)
     
    def __str__(self):
       return self.more_details1

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
   
	def __str__(self):
		return self.name  

    
 


class Experience(models.Model):   
    experience = models.CharField(max_length=100, null=True, blank=True)
    experience_title = models.CharField(max_length=100, null=True, blank=True)
    experience_year = models.CharField(max_length=100, null=True, blank=True)
    experience_company = models.CharField(max_length=100, null=True, blank=True)     
    #experience_summary = models.ManyToManyField(EexperienceMore, null=True, blank=True)
    tags = models.ManyToManyField(Tag,max_length=150, null=True, blank=True)
    def __str__(self):
        return self.experience_company
     

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "My Experience"


class Socialiconlink(models.Model):
    behance = models.URLField(null=True, blank=True, max_length=100)
    fb = models.URLField(null=True, blank=True, max_length=100)
    insta = models.URLField(null=True, blank=True, max_length=100)
    yotube = models.URLField(null=True, blank=True, max_length=100)
    link = models.URLField(null=True, blank=True, max_length=100)
    addr=models.CharField(null=True, blank=True, max_length=150)
    mob=models.CharField(null=True, blank=True, max_length=100)
    email=models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = "contactus"
        verbose_name_plural = "contact & Social Icons"

    def __str__(self):
        return self.email + self.mob + self.addr

class HappyCustomer(models.Model):
    hometext= models.CharField(null=True, blank=True, max_length=100)
    clients = models.CharField(null=True, blank=True, max_length=100)
    projects = models.CharField(null=True, blank=True, max_length=100)
    hours  = models.CharField(null=True, blank=True, max_length=100)
    workers = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.clients
     

    class Meta:
        verbose_name = "HappyCustomer"
        verbose_name_plural = "My Customer"


class Intrest(models.Model):
    icon = models.CharField(null=True, blank=True, max_length=100)
    intrest = models.CharField(null=True, blank=True, max_length=100)   
    color = ColorField(default='#FFE600', null=True, blank=True,max_length=100)
    colors=models.CharField(null=True, blank=True, max_length=100)


    def __str__(self):
        return self.intrest

    
    class Meta:
        verbose_name = "Intrest"
        verbose_name_plural = "My Intrest"

class Testimonial(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(null=True, blank=True, max_length=100)
    designation  = models.CharField(null=True, blank=True, max_length=100)
    name  = models.CharField(null=True, blank=True, max_length=100)
    def __str__(self):
        return self.name
     

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "My Testimonial"


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
