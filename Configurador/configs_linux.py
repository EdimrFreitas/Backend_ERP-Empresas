from os import getlogin
from os.path import abspath
from subprocess import call


def Linux():
    print('Checando a versão do python...')
    if call('python3 --version'):
        call('sudo apt-get update; sudo apt-get install python3')

    print("Instalando ...")
    if call('pip --version'):
        call('sudo apt install python3-pip')
    call('sudo apt install python3-venv')
    call('python3 -m venv ./venv')

    print('Instalando pacotes necessários...')
    pip3 = abspath('./venv/bin/pip3')
    call(f'sudo {pip3} install flask==2.2.2')
    call(f'sudo {pip3} install flask-bcrypt==4.0.1')
    call(f'sudo {pip3} install flask-sqlalchemy==3.0.2')
    call(f'sudo {pip3} install mysql-connector-python==8.0.31')
    call(f'sudo {pip3} install netifaces==0.11.0')

    print('Agora, vamos instalar e configurar o mysql server...')
    if call('mysql --version'):
        call('sudo apt install mysql-server')
        call('sudo systemctl enable mysql')

        print('Atribuindo uma senha ao root do mysql')
        call('sudo mysql_secure_installation')

    print('Criando serviço api-erp-empresas.service...')
    servico = '/etc/systemd/system/api-erp-empresas.service'
    usuario = getlogin()
    local = abspath('Backend_ERP-Empresas')
    call(f'sudo touch {servico}')
    with open(servico, mode='r+') as api_erp_empresas:
        api_erp_empresas.write(
            f"""[Unit]
            Description=Serviço da api para banco de dados do ERP-empresas
            
            [Service]
            User={usuario}
            WorkingDirectory={local}
            ExecStart={local}/venv/bin/python3 api_back_end.py
            Restart=always
            
            [Install]
            WantedBy=multi-user.target
            """
        )

    call('sudo systemctl start api-erp-empresas.service')
    status = call('sudo systemctl status api-erp-empresas.service')

    if not status:
        print('Serviço api-erp-empresas.service iniciado com sucesso...')
        call('wait')
