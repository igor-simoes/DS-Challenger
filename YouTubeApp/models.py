from django.db import models
from datetime import date

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    sum_score = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.name

    def update_sum_score(self):
        """
        Description:
            Method to set the sum of all videos scores that contains this theme
        Params:
            None
        Return:
            None
        """
        video_list = self.video_set.all()
        sum_score = 0.0
        for video in video_list:
            video.update_score()
            sum_score += video.score

        self.sum_score = sum_score
        self.save()

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    date_uploaded = models.DateField()
    views = models.IntegerField()
    themes = models.ManyToManyField(Theme)
    score = 0

    def __unicode__(self):
        return self.title

    def get_time_factor(self):
        """
        Description:
            Method to get the time_factor value
        Params:
            None
        Return:
            The value for time_factor
        """
        today = date.today()
        days_since_upload = (date.today() - self.date_uploaded).days
        time_factor = max(0, 1 - (days_since_upload/365))
        return time_factor

    def get_good_comments(self):
        """
        Description:
            Method to get good_comments value
        Params:
            None
        Return:
            The value for good_comments
        """
        positive_comments = len(self.comment_set.filter(is_positive=True))
        negative_comments = len(self.comment_set.filter(is_positive=False))
        sum_comments = positive_comments + negative_comments
        if sum_comments:
            good_comments = positive_comments / (positive_comments + negative_comments)
        else:
            # need to check if value is not equal to zero to avoid ZeroDivisionError
            good_comments = sum_comments
        return good_comments

    def get_thumbs_up(self):
        """
        Description:
            Method to get thumbs_up value
        Params:
            None
        Return:
            The value for thumbs_up
        """
        thumbs_up = len(self.thumb_set.filter(is_positive=True))
        thumbs_down = len(self.thumb_set.filter(is_positive=False))

        sum_thumbs = (thumbs_up + thumbs_down)
        if sum_thumbs:
            # need to check if value is not equal to zero to avoid ZeroDivisionError
            thumbs_up = thumbs_up / sum_thumbs
        else:
            thumbs_up = sum_thumbs

        return thumbs_up

    def get_positivity_factor(self):
        """
        Description:
            Method to get positivity_factor value
        Params:
            None
        Return:
            The value for positivity_factor
        """
        good_comments = self.get_good_comments()
        thumbs_up = self.get_thumbs_up()
        value_good_comments = 0.7
        value_thumbs_up = 0.3
        positivity_factor = (
            value_good_comments * good_comments + value_thumbs_up * thumbs_up
        )
        return positivity_factor

    def update_score(self):
        """
        Description:
            Method to update Score value
        Params:
            None
        Return:
            None
        """
        good_comments = self.get_good_comments()
        time_factor = self.get_time_factor()
        positivity_factor = self.get_positivity_factor()
        score = self.views * time_factor * positivity_factor
        self.score = score

class Thumb(models.Model):
    id = models.AutoField(primary_key=True)
    is_positive = models.BooleanField(default=False)
    time = models.DateTimeField()
    video = models.ForeignKey(Video)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    is_positive = models.BooleanField(default=False)
    time = models.DateTimeField()
    video = models.ForeignKey(Video)
