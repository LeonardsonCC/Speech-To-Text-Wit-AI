echo "Verificando arquivo de configuração..."
if test -f "config.ini"; then
  echo "Arquivo existe."
else
  echo "Arquivo não encontrado. Por favor, faça uma cópia de config.ini-example com suas credenciais."
fi

echo "Iniciando script..."
if test -f "$(which python3.8)"; then
  $(which python3.8) app/app.py
else
  echo "Python 3.8 não encontrado... Por favor, instale-o."
fi
