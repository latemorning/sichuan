from django.db import models
from django.contrib.auth.models import User


class StageComptTime(models.Model):
    stage_no = models.SmallIntegerField(unique=True)   # 스테이지 번호
    compt_time = models.SmallIntegerField(null=True)     # 완료시간
    compt_se = models.CharField(max_length=255, null=True, default='normal')    # 완료 구분
    frst_regist_dt = models.DateTimeField(auto_now_add=True, null=True)     # 최초 등록 일시
    last_regist_dt = models.DateTimeField(auto_now=True, null=True)     # 최종 등록 일시

    def __str__(self):
        return str(self.stage_no)


class Stage(models.Model):
    stage_no = models.CharField(max_length=8, null=False, unique=True)
    stage_ty_code = models.CharField(max_length=30, null=True)
    boss_at = models.CharField(max_length=1, null=True)
    gnrl_lmtt_time = models.CharField(max_length=8, null=True)
    crown_lmtt_time = models.CharField(max_length=8, null=True)
    frst_regist_dt = models.DateTimeField(auto_now_add=True, null=True)  # 최초 등록 일시
    last_regist_dt = models.DateTimeField(auto_now=True, null=True)  # 최종 등록 일시

    def __str__(self):
        return str(self.stage_no)


class ComptTime(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    compt_se = models.CharField(max_length=255, null=True)
    compt_time = models.CharField(max_length=8, null=True)
    frst_regist_dt = models.DateTimeField(auto_now_add=True, null=True)  # 최초 등록 일시
    last_regist_dt = models.DateTimeField(auto_now=True, null=True)  # 최종 등록 일시

    def __str__(self):
        return str(self.compt_se)
