from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact

from django.contrib import messages

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText
 
# Create your views here.

# def contact(request, sendmsg=None):
#     msg = ''
#     title = ''
#     username = ''
#     info = ''
    
#     if 'account' in request.session and 'isAlive' in request.session:
#         if request.method == 'POST':
#             title = request.POST.get('title')
#             username = request.POST.get('username')
#             info = request.POST.get('info')
            
            
            
            
            
#         if sendmsg == 'sendmsg':
#             if 'title' in request.POST and 'username' in request.POST:
#                 title = request.POST['title']
#                 info = request.POST['info']
#                 username = request.POST['username']
        
#                 data = Contact.objects.create(title = title, username = username, info = info)
#                 messages.success(request, ('您的訊息已收到'))
#                 msg = "您的訊息已收到"
                
#             elif 'title' not in request.POST:
#                 msg = "標題未輸入"
#                 messages.success(request, ('標題未輸入'))
            
#             elif 'username' not in request.POST:
#                 msg = "使用者名稱未輸入"
#                 messages.success(request, ('使用者名稱未輸入'))
                
#             return render(request, 'contact.html', locals())
#         else:
            
#             messages.success(request, ('您好!'))
            
#     else:
#         return render(request, 'login.html')
    
#     return render(request, 'contact.html')



def contact(request, sendmsg=None):
    msg = ''
    title = ''
    username = ''
    info = ''
    
    if 'account' in request.session and 'isAlive' in request.session:
        if request.method == 'POST':
            title = request.POST['title']
            username = request.POST['username']
            info = request.POST['info']
            
            data = Contact.objects.create(title = title,
                                             username = username,
                                             info = info)
            messages.success(request, ('您的訊息已收到'))
            smtp = "smtp.gmail.com:587" # Gmail 主機位置
            account = "destroyer135791@gmail.com" # 請輸入Gmail 帳號
            # password = "0956909591" # Gmail 的密碼
            password = "ltmeylbloxucqhsk"
            
            # content = "非常感謝您的訂購，我們將快速出貨！！"
            content = info
            msg = MIMEText(content) # 郵件內容
            
            # 主旨
            # msg['Subject'] = "聯成電腦購物網-訂單成立"
            msg['Subject'] = title
            
            # 寄給誰
            mailto = "destroyer135791@gmail.com" # 寄給單獨的收件者
            # mailto = request.session['account']
            
            # mailto = ["destroyer135791@gmail.com", "destroyer135791@gmail.com"] # 寄給多個
            
            # 建立SMTP 的連線
            server = SMTP(smtp)
            
            # 與SMTP 主機溝通
            server.ehlo()
            
            # 要使用 TTLS 安全認證
            server.starttls()
            
            try:
                # 登入，身分確認
                server.login(account, password)
                
                server.sendmail(account, mailto, msg.as_string()) #寄信
                
                sendMsg = "郵件已寄出"
            
            except SMTPAuthenticationError:
                sendMsg = "帳密認證錯誤"
            except:
                sendMsg = "郵件發生錯誤"
                
            # 關閉 Server 連線
            server.quit()

            
                
            return render(request, 'contact.html', locals())
        else:
            
            messages.success(request, ('您好!'))
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'contact.html')






#-----------

# def contact(request, sendmsg=None):
#     msg = ''
#     title = ''
#     username = ''
#     info = ''

#     if sendmsg == 'sendmsg':
#         if 'title' in request.POST and 'username' in request.POST:
#             title = request.POST['title']
#             info = request.POST['info']
#             username = request.POST['username']
    
#             data = Contact.objects.create(title = title, username = username, info = info)
#             messages.success(request, ('您的訊息已收到'))
#             msg = "您的訊息已收到"
            
#         elif 'title' not in request.POST:
#             msg = "標題未輸入"
#             messages.success(request, ('標題未輸入'))
        
#         elif 'username' not in request.POST:
#             msg = "使用者名稱未輸入"
#             messages.success(request, ('使用者名稱未輸入'))
            
#         return render(request, 'contact.html', locals())
#     else:
        
#         messages.success(request, ('您好!'))
#     return render(request, 'contact.html')