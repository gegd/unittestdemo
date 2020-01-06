import smtplib
from email.mime.text import MIMEText

class SendEmail():
    global mail_host
    global mail_user
    global mail_pwd
    mail_host = 'smtp.163.com'
    mail_user = 'mushishi666@163.com'
    mail_pwd = 'ggd84688149'

    def send_email(self,user_list,sub,content):
        sender = 'mushishi666<' + mail_user + '>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = sender
        message['To'] = ';'.join(user_list)
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            server.login(mail_user,mail_pwd)
            server.sendmail(sender,user_list,message.as_string())
            server.quit()
            print('发送邮件成功')
            
        except smtplib.SMTPException:
            print('Error: 无法发送邮件')
        

    def send_main(self,pass_list,fail_list):
        pass_count = len(pass_list)
        fail_count = len(fail_list)
        total_count = pass_count + fail_count
        pass_result = '%.2f%%' %(pass_count / total_count*100)
        fail_result = '%.2f%%' %(fail_count / total_count*100)
        print(total_count)
        print(pass_result)
        print(fail_result)
        content = '此次一共运行接口个数为%d个，通过个数为%d个，失败个数为%d个，通过率为%s，失败率为%s' %(total_count,pass_count,fail_count,pass_result,fail_result)
        user_list = ['wsggd2007@qq.com']
        self.send_email(user_list,'接口自动化测试报告',content)
        

# if __name__ == "__main__":
    # send = SendEmail()
    # send.send_main([1,2,3,4],[5,6,7,8,9])
    