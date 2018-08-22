from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import UserProfile
import re

def keyword(comment):
    pattern1 = re.compile(r'mmp')
    pattern2 = re.compile(r'辣鸡')

    if re.findall(pattern1,comment) or re.findall(pattern2,comment):
        raise ValidationError('请不要输入敏感词，如mmp')

def lessword(comment):
    if len(comment) < 2 :
        raise ValidationError('不得少于2个字符～～')

def bigword(name):
    if len(name) > 40:
        raise ValidationError('用户名不能超过40个字符')

# 修改用户名,性别，头像的表单
class ProfileForm(forms.Form):
    name = forms.CharField(
        label = '你的昵称',
        max_length=40,
        error_messages = {'require':'昵称不能为空哦～～',},
        widget = forms.TextInput(attrs={'placeholder':'新的昵称'}),
        validators = [bigword,lessword]
        )
    CHOICES = (('男生', '男生',), ('女生', '女生',))
    sexy = forms.ChoiceField(choices=CHOICES,widget=forms.Select,label='你的性别')
    avatar = forms.ImageField(label='上传新头像')


class CommentForm(forms.Form):

    comment = forms.CharField(
        widget = forms.Textarea(attrs={'placeholder':'添加一条评论吧～'}),
        error_messages = {
            'require':'亲～这是必填项哟',
        },
        validators=[keyword,lessword]
        )

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')
    email = forms.CharField()


class ArticleForm(forms.Form):

    title = forms.CharField(
        label='作品名称',
        max_length=100,
        error_messages = {'required':'亲～一定要有标题哟'},
        validators = [keyword,lessword]
        )


    content = forms.CharField(
        label='作品描述',
        error_messages = {'required':'亲～一定要有标题哟'},
        validators = [lessword],
        widget = forms.Textarea(),
    )


    MY_CHOICES = (
    ('hot', '画作'),
    ('best', '书法'),
                    )

    category = forms.ChoiceField(choices=MY_CHOICES,
                            label = '选择作品分类',
                            widget=forms.RadioSelect,
                                )


    pic = forms.FileField(label="选择图片",required=False ,error_messages = {'required':'选择图片哦'},)
    price = forms.CharField(
        label='价格',
        max_length=100,
        error_messages={'required': '亲～一定要有标题哟'},
        validators=[keyword, lessword]
    )


class BuyForm(forms.Form):

    name = forms.CharField(
        label='收货人',
        max_length=100,
        error_messages = {'required':'！'},
        validators = [keyword,lessword]
        )


    address = forms.CharField(
        label='收货地址',
        error_messages = {'required':'亲～一定要有标题哟'},
        validators = [lessword],
        widget = forms.Textarea(),
    )


    MY_CHOICES = (
    ('hot', '货到付款'),

                    )

    category = forms.ChoiceField(choices=MY_CHOICES,
                            label = '选择购买方式',
                            widget=forms.RadioSelect,
                                )


    phone = forms.CharField(
        label='收货人电话',
        max_length=11,
        error_messages={'required': '亲～一定要有标题哟'},
        validators=[keyword, lessword]
    )