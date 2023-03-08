# _*_coding:utf-8_*_
"""
@ Author:陈金泉
@ Date:2023/3/7 11:55
@ Description: 定义Jenkins类，驱动jenkins实现创建项目，自动打包
"""
import jenkins
from autoinstall.tools.read_ini import read_ini


class Jenkins_:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.jenkins = None

    def connect(self):
        self.jenkins = jenkins.Jenkins(self.url, self.username, self.password)

    def build(self, name, build_environment, git_branch):
        parameters_dic = {"build_environment".upper(): build_environment, "git_branch".upper(): git_branch}
        if isinstance(self.jenkins, jenkins.Jenkins) and self.jenkins.job_exists(name):
            self.jenkins.build_job(name=name, parameters=parameters_dic)
        print(name, parameters_dic)

    def delete_job(self, name):
        if isinstance(self.jenkins, jenkins.Jenkins) and self.jenkins.job_exists(name):
            self.jenkins.delete_job(name)

    def quantity_query(self):
        if isinstance(self.jenkins, jenkins.Jenkins):
            return self.jenkins.jobs_count()


if __name__ == '__main__':
    info_dic = read_ini("./config.ini", "INFO")
    jenkins_dic = read_ini("./config.ini", "JENKINS")
    jenkins_obj = Jenkins_(jenkins_dic.get("url"), username=info_dic.get("name"), password=info_dic.get("api_token"))
    jenkins_obj.connect()
    jenkins_obj.build(info_dic.get("name"), jenkins_dic.get("build_environment"), jenkins_dic.get("git_branch"))
