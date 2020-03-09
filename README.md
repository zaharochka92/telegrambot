#Это телеграмм бот с небольшим функционалом для запускаете в докере.

Бот умеет парсить погоду, пробки, курсы валют и новости
Так же имеется скрипт для автоматического развертывания бота в облаке.

###
Все ключи хранятся в файле
создайте и скопируйте в py файл
teletokens.py :
  teletoken = '' #tokens telegram 
  
  ip_mikro_home = '' #ip mikrotik
  
  ip_mikro_dacha = ''
  
  user_mikro = '+ct80h'
  
  password_mikro = ''
  
  arubalogin = '' #aruba cloud login pass
  
  arubapassword = ''
  
  openweather_token = '' #openweather token
  
  host = '' #server with docker host
  
  hostusername = ''
  
  hostpassword = ''
  
  port =  # ssh port for netmiko
  
  gitrepo = '' #git repo in format user:password@github.com/repourl
  ###
  добавлены файлы для автоматической установки докера на сервер
  утсановка ansible:
  pip install ansible
  обновление зависимостей ansible:
  ansible-galaxy install -r requirements.yml
  установка докера:
  ansible-playbook -i 'ip_host,' docker.yml
  
