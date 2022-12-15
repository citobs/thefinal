from django.db import models


# # Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateField()


class Post(models.Model):
    
    mainphoto = models.ImageField(blank=True, null=True)
    postname = models.CharField(max_length=50)
    contents = models.TextField()


    def __str__(self):
        return self.postname

class resultall(models.Model):
    restaurant = models.CharField(max_length=300)
    menu = models.CharField(max_length=300)
    emotion = models.CharField(max_length=300, null=True, default='')
    season = models.CharField(max_length=300, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"({self.season},{self.emotion})"



class fullist(models.Model):
    emot = models.CharField(max_length=300, null=True)
    sea = models.CharField(max_length=300, null=True)
    first= models.CharField(max_length=300, null=True)
    second= models.CharField(max_length=300, null=True)
    third = models.CharField(max_length=300, null=True)
    cr_at = models.DateTimeField(auto_now_add=True, null=True)
    fourth = models.CharField(max_length=300, null=True)
    fifth = models.CharField(max_length=300, null=True)
    wea = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return f"({self.emot},{self.sea})"
    

#음식점 정보만 있는 것
class RestaurantMenu(models.Model):
    restaurant = models.CharField(max_length=300,null=True)
    menu = models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return f"({self.restaurant},{self.menu})"

# 선택의 결과값 저장
class choice(models.Model):
    res = models.CharField(max_length=300,null=True)
    menu = models.CharField(max_length=300,null=True)
    emotion = models.CharField(max_length=300,null=True)
    weather = models.CharField(max_length=300,null=True)
    season = models.CharField(max_length=300,null=True)
    comment = models.CharField(max_length=300,null=True)
    
    cr_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return f"({self.res})"
    
    


class MenuScoreAll(models.Model):
    menu = models.TextField(blank=True, null=True)
    restaurant = models.TextField(blank=True, null=True)
    happy_winter = models.FloatField(blank=True, null=True)
    happy_winter_snow = models.FloatField(blank=True, null=True)
    happy_winter_rain = models.FloatField(blank=True, null=True)
    happy_fall = models.FloatField(blank=True, null=True)
    happy_fall_rain = models.FloatField(blank=True, null=True)
    happy_summer = models.FloatField(blank=True, null=True)
    happy_summer_rain = models.FloatField(blank=True, null=True)
    happy_spring = models.FloatField(blank=True, null=True)
    happy_spring_rain = models.FloatField(blank=True, null=True)
    sad_spring_rain = models.FloatField(blank=True, null=True)
    sad_spring = models.FloatField(blank=True, null=True)
    sad_summer_rain = models.FloatField(blank=True, null=True)
    sad_summer = models.FloatField(blank=True, null=True)
    sad_fall_rain = models.FloatField(blank=True, null=True)
    sad_fall = models.FloatField(blank=True, null=True)
    sad_winter_rain = models.FloatField(blank=True, null=True)
    sad_winter = models.FloatField(blank=True, null=True)
    sad_winter_snow = models.FloatField(blank=True, null=True)
    angry_winter = models.FloatField(blank=True, null=True)
    angry_winter_snow = models.FloatField(blank=True, null=True)
    angry_winter_rain = models.FloatField(blank=True, null=True)
    angry_fall = models.FloatField(blank=True, null=True)
    angry_fall_rain = models.FloatField(blank=True, null=True)
    angry_summer = models.FloatField(blank=True, null=True)
    angry_summer_rain = models.FloatField(blank=True, null=True)
    angry_spring = models.FloatField(blank=True, null=True)
    angry_spring_rain = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_score_all'