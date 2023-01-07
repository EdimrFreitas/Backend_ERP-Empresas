from os import getlogin, getcwd
from os.path import abspath
from subprocess import call


def Linux():
    print('\nChecando a versão do python3...')
    if call('python3 --version'):
        call('sudo apt-get update; sudo apt-get install python3')

    print("\nChecando a versão do pip3...")
    if call('pip --version'):
        call('sudo apt install python3-pip')

    print('\nInstalando ambiente virtual...')
    if call('find /usr/lib/python3.10/venv/'):
        call('sudo apt install python3-venv')

    print('\nConfigurando ambiente virtual...')
    call('python3 -m venv ./venv')

    print('\nInstalando pacotes necessários...')
    path_local = getcwd()
    path_venv = f'{path_local}/venv'
    pip3 = f'{path_venv}/bin/pip3'
    call(f'sudo {pip3} install flask==2.2.2')
    call(f'sudo {pip3} install flask-bcrypt==4.0.1')
    call(f'sudo {pip3} install flask-sqlalchemy==3.0.2')
    call(f'sudo {pip3} install mysql-connector-python==8.0.31')
    call(f'sudo {pip3} install netifaces==0.11.0')

    print('\nAgora, vamos instalar e configurar o mysql server...')
    if call('mysql --version'):
        call('sudo apt install mysql-server')
        call('sudo systemctl enable mysql')

        print('\nAtribuindo uma senha ao root do mysql...')
        call('sudo mysql_secure_installation')

    nome_servico = 'api-erp-empresas.service'
    print(f'\nCriando serviço {nome_servico}...')
    servico = f'/etc/systemd/system/{nome_servico}'
    with open(servico, mode='w') as api_erp_empresas:
        api_erp_empresas.write(f"""
[Unit]
Description=Serviço da api para banco de dados do ERP-empresas

[Service]
User={getlogin()}
WorkingDirectory={path_local}
ExecStart={path_venv}/bin/python3 api_back_end.py
Restart=always

[Install]
WantedBy=multi-user.target
""")

    call(f'sudo systemctl start {nome_servico}')
    status = call(f'sudo systemctl status {nome_servico}')

    if not status:
        print(f'Serviço {nome_servico} iniciado com sucesso...')

    call('wait')
