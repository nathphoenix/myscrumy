from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=350)
    # def __str__(self):
    #     return self.status_name     #this method returns the input field status_name

class ScrumyGoals(models.Model):
    goal_id = models.CharField(max_length=340)
    goal_name = models.CharField(max_length=340)
    created_by = models.CharField(max_length=340)
    moved_by = models.CharField(max_length=340)
    user = models.ForeignKey(User, related_name='scrumy_goals', on_delete=models.CASCADE)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    owner = models.CharField(max_length=340)
    def __str__(self):
        return self.goal_id

class ScrumyHistory(models.Model):
    moved_from = models.CharField(max_length=340)
    moved_to = models.CharField(max_length=340)
    created_by = models.CharField(max_length=340)
    moved_by = models.CharField(max_length=340)
    time_of_action = models.TimeField(max_length=340)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)


class Post(models.Model):
    name = models.CharField(max_length=340)
    message = models.CharField(max_length=340)
    created_by = models.DateField()

class Comment(models.Model):
    comment = models.CharField(max_length=340)
    created_by = models.DateField()
# DateField
# class Profile(Model):
#     user = models.OneToOneField(
#         to=settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='profile', )

# @models.permalink
    # def get_absolute_url(self):
    #     return ('blog_post_detail', (),
    #             {
    #                'slug': self.slug,
    #             })

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(ScrumyGoals, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ['created_on']

    #     def __unicode__(self):
    #         return self.title




#for api purposes


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('User must have an email address')

#         user = self.model(
#             email = self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password=password)
#         user.is_admin = True
#         user.save()
#         return user


# class User(AbstractBaseUser):
#     objects = UserManager()
#     email = models.EmailField(unique=True, db_index=True)
#     created = models.DateTimeField('created', auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     is_active = models.BooleanField('active', default=True)
#     is_admin = models.BooleanField('admin', default=False)

#     USERNAME_FIELD = 'email'

#     ordering = ('created',)

#     def is_staff(self):
#         return self.is_admin

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     def get_short_name(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def __unicode__(self):
#         return self.email


# class Profile(models.Model):
#     GENDER = (
#         ('M', 'Homme'),
#         ('F', 'Femme'),
#     )

#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     first_name = models.CharField(max_length=120, blank=False)
#     last_name = models.CharField(max_length=120, blank=False)
#     gender = models.CharField(max_length=1, choices=GENDER)
#     zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], blank=False)
#     def __unicode__(self):
#         return u'Profile of user: {0}'.format(self.user.email)


# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# post_save.connect(create_profile, sender=User)


# def delete_user(sender, instance=None, **kwargs):
#     try:
#         instance.user
#     except User.DoesNotExist:
#         pass
#     else:
#         instance.user.delete()
# post_delete.connect(delete_user, sender=Profile)