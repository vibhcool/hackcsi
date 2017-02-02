from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=80,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    pwd= models.CharField(max_length=80)
    no_of_topics=models.IntegerField(default=0)
    type=models.IntegerField(default=0) #simple=0 org=1
    def __str__(self):
        return self.user_name


class Topic(models.Model):
    tags = models.ForeignKey(Tag, on_delete = models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topic_text = models.CharField(max_length=250)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.topic_text


class Tag(models.Model):
    tag_name= models.CharField(max_length=50)
    tag_desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.tag_name

class Opinion(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    opinion_text=models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    foragainst=models.IntegerField(default=0) #for=1 against=0
    def __str__(self):
        return self.user.user_name